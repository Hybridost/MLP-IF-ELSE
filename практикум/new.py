import math
import random
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# КОНСТАНТЫ

ACTION_STRAIGHT = 0
ACTION_LEFT = 1
ACTION_RIGHT = 2
ACTION_BRAKE = 3

WEATHER = {
    "dry": 0,
    "rain": 1,
    "fog": 2,
    "snow": 3
}

ROAD_TYPE = {
    "city": 0,
    "highway": 1,
    "rural": 2
}

ROAD_DAMAGE = {
    "good": 0,
    "bad": 1
}

TRAFFIC = {
    "low": 0,
    "medium": 1,
    "high": 2
}



def smart_rule_based(
    distance_front,
    speed,
    speed_front,
    left_distance,
    right_distance,
    left_speed,
    right_speed,
    can_change,
    weather,
    road_type,
    road_damage,
    visibility,
    traffic_density
):

    speed_ms = speed / 3.6
    speed_front_ms = speed_front / 3.6

    relative_speed = speed_ms - speed_front_ms

    safe_distance = 20
    lane_change_distance = 20
    emergency_distance = 8
    collision_time_limit = 1.5

    if weather == WEATHER["rain"]:
        safe_distance += 10
        lane_change_distance += 10

    elif weather == WEATHER["snow"]:
        safe_distance += 20
        lane_change_distance += 20
        collision_time_limit += 1

    elif weather == WEATHER["fog"]:
        safe_distance += 15
        collision_time_limit += 1

    if road_type == ROAD_TYPE["highway"]:
        safe_distance += 15

    elif road_type == ROAD_TYPE["rural"]:
        safe_distance += 10

    if road_damage == ROAD_DAMAGE["bad"]:
        lane_change_distance += 15

    if visibility < 50:
        safe_distance += 20
        collision_time_limit += 1

    elif visibility < 100:
        safe_distance += 10

    if traffic_density == TRAFFIC["high"]:
        lane_change_distance += 15

    elif traffic_density == TRAFFIC["medium"]:
        lane_change_distance += 5

    if relative_speed < 1:
        collision_time = math.inf
    else:
        collision_time = distance_front / relative_speed

    if (
        distance_front < emergency_distance
        or collision_time < collision_time_limit
    ):
        return ACTION_BRAKE

    low_danger = (
        distance_front < safe_distance
        or collision_time < 4
    )

    medium_danger = (
        distance_front < safe_distance * 0.7
        or collision_time < 2.5
    )

    left_safe = (
        left_distance > lane_change_distance
        and abs(left_speed - speed) < 15
    )

    right_safe = (
        right_distance > lane_change_distance
        and abs(right_speed - speed) < 15
    )

    if medium_danger:
        return ACTION_BRAKE

    if low_danger and can_change:

        if left_safe:
            return ACTION_LEFT

        elif right_safe:
            return ACTION_RIGHT

    return ACTION_STRAIGHT


# ГЕНЕРАЦИЯ ДАННЫХ

def generate_data(n=2000):

    X = []
    y = []

    for _ in range(n):

        sample = [

            random.uniform(1, 100),
            random.uniform(0, 130),
            random.uniform(0, 130),

            random.uniform(0, 100),
            random.uniform(0, 100),

            random.uniform(0, 130),
            random.uniform(0, 130),

            random.randint(0, 1),

            random.randint(0, 3),
            random.randint(0, 2),
            random.randint(0, 1),

            random.uniform(20, 500),

            random.randint(0, 2)
        ]

        label = smart_rule_based(*sample)

        X.append(sample)
        y.append(label)

    return X, y


# MLP

class MLP(nn.Module):

    def __init__(self):

        super().__init__()

        self.model = nn.Sequential(

            nn.Linear(13, 64),
            nn.ReLU(),

            nn.Linear(64, 64),
            nn.ReLU(),

            nn.Linear(64, 32),
            nn.ReLU(),

            nn.Linear(32, 4)

        )

    def forward(self, x):
        return self.model(x)


# ПОДГОТОВКА ДАННЫХ

X, y = generate_data(5000)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=1000,
    random_state=42
)

X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)

y_train = torch.tensor(y_train, dtype=torch.long)
y_test = torch.tensor(y_test, dtype=torch.long)


# ОБУЧЕНИЕ

model = MLP()

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

print("Начало обучения\n")

for epoch in range(100):

    optimizer.zero_grad()

    output = model(X_train)

    loss = criterion(output, y_train)

    loss.backward()

    optimizer.step()

    if epoch % 10 == 0:

        print(
            f"Epoch {epoch} | Loss = {loss.item():.4f}"
        )

print("\nОбучение завершено\n")


# ТЕСТИРОВАНИЕ

model.eval()

correct = 0
predictions = []

with torch.no_grad():

    for i in range(len(X_test)):

        output = model(X_test[i])

        pred = torch.argmax(output).item()

        predictions.append(pred)

        if pred == y_test[i].item():
            correct += 1

accuracy = correct / len(X_test)

print("МАССОВОЕ ТЕСТИРОВАНИЕ")

print(f"Количество тестов: {len(X_test)}")
print(f"Правильных ответов: {correct}")
print(f"Accuracy: {accuracy:.4f}")


# МАТРИЦА ОШИБОК

cm = confusion_matrix(
    y_test.numpy(),
    predictions
)

print("\nМатрица ошибок:\n")
print(cm)


# РУЧНОЙ ТЕСТ

test_case = [

    30,
    90,
    50,

    60,
    15,

    80,
    100,

    1,

    WEATHER["dry"],
    ROAD_TYPE["city"],
    ROAD_DAMAGE["good"],

    500,

    TRAFFIC["low"]
]

with torch.no_grad():

    output = model(
        torch.tensor(
            test_case,
            dtype=torch.float32
        )
    )

    probabilities = torch.softmax(
        output,
        dim=0
    )

    pred = torch.argmax(output).item()

print("Предсказанный манёвр:", pred)

print("\nВероятности:")

actions = [
    "Прямо",
    "Влево",
    "Вправо",
    "Торможение"
]

for i in range(4):

    print(
        f"{actions[i]}: "
        f"{probabilities[i].item()*100:.2f}%"
    )
