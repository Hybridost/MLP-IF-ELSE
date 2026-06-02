# import torch
# import torch.nn as nn
# import torch.optim as optim
# import random

# # IF-ELSE АЛГОРИТМ
# def rule_based(x):
#     distance_front, speed, speed_front, left, right, can_change = x

#     if distance_front < 10:
#         return 3

#     elif distance_front < 20 and left > 20 and can_change:
#         return 1

#     elif distance_front < 20 and right > 20 and can_change:
#         return 2

#     else:
#         return 0

# # ГЕНЕРАЦИЯ ДАННЫХ

# def generate_data(n=1000):

#     X = []
#     y = []

#     for _ in range(n):

#         sample = [

#             random.uniform(0, 100),   # distance_front
#             random.uniform(0, 120),   # speed
#             random.uniform(0, 120),   # speed_front
#             random.uniform(0, 100),   # left
#             random.uniform(0, 100),   # right
#             random.randint(0, 1)      # can_change

#         ]

#         label = rule_based(sample)

#         X.append(sample)
#         y.append(label)

#     return (
#         torch.tensor(X, dtype=torch.float32),
#         torch.tensor(y, dtype=torch.long)
#     )


# # MLP

# class MLP(nn.Module):

#     def __init__(self):

#         super().__init__()

#         self.model = nn.Sequential(

#             nn.Linear(6, 32),
#             nn.ReLU(),

#             nn.Linear(32, 32),
#             nn.ReLU(),

#             nn.Linear(32, 4)

#         )

#     def forward(self, x):
#         return self.model(x)

# # ОБУЧЕНИЕ

# X_train, y_train = generate_data(1000)

# model = MLP()

# criterion = nn.CrossEntropyLoss()

# optimizer = optim.Adam(
#     model.parameters(),
#     lr=0.001
# )

# print("Начало обучения...\n")

# for epoch in range(50):

#     optimizer.zero_grad()

#     output = model(X_train)

#     loss = criterion(output, y_train)

#     loss.backward()

#     optimizer.step()

#     if epoch % 10 == 0:

#         print(
#             f"Epoch {epoch} | Loss = {loss.item():.4f}"
#         )

# print("\nОбучение завершено.\n")

# # РУЧНЫЕ ТЕСТЫ

# print("РУЧНЫЕ ТЕСТЫ\n")

# test_cases = [

#     ([5, 60, 20, 100, 100, 1], 3),
#     ([15, 60, 40, 100, 10, 1], 1),
#     ([15, 60, 40, 10, 100, 1], 2),
#     ([15, 60, 40, 5, 5, 1], 0),
#     ([100, 60, 60, 100, 100, 1], 0)

# ]

# model.eval()

# for i, (x, expected) in enumerate(test_cases):

#     x_tensor = torch.tensor(
#         x,
#         dtype=torch.float32
#     )

#     output = model(x_tensor)

#     pred = torch.argmax(output).item()

#     print(f"Тест {i+1}")

#     print(f"Вход: {x}")

#     print(f"Ожидалось: {expected}")

#     print(f"MLP предсказала: {pred}")

#     if pred == expected:
#         print("Результат: SUCCESS")
#     else:
#         print("Результат: FAIL")

#     print("-" * 40)

# # МАССОВОЕ ТЕСТИРОВАНИЕ

# print("\nМАССОВОЕ ТЕСТИРОВАНИЕ\n")

# X_test, y_test = generate_data(300)

# correct = 0

# for i in range(len(X_test)):

#     output = model(X_test[i])

#     pred = torch.argmax(output).item()

#     if pred == y_test[i].item():
#         correct += 1

# accuracy = correct / len(X_test)

# print(f"Количество тестов: {len(X_test)}")

# print(f"Правильных ответов: {correct}")

# print(f"Accuracy: {accuracy:.2f}")

# # ТЕСТ УСТОЙЧИВОСТИ

# print("\nТЕСТ УСТОЙЧИВОСТИ\n")

# x = [15, 60, 40, 50, 50, 1]

# for delta in [-2, 0, 2]:

#     x_mod = x.copy()

#     x_mod[0] += delta

#     pred = torch.argmax(
#         model(
#             torch.tensor(
#                 x_mod,
#                 dtype=torch.float32
#             )
#         )
#     ).item()

#     print(f"{x_mod} -> {pred}")


test_cases = [

    # 1
    {

        "name": "Опасное сближение на трассе",

        "expected": 3,

        "params": {

            "distance_front": 6,
            "speed": 120,
            "speed_front": 20,

            "left_distance": 10,
            "right_distance": 10,

            "left_speed": 100,
            "right_speed": 100,

            "can_change": 1,

            "weather": "dry",
            "road_type": "highway",
            "road_damage": "good",

            "visibility": 500,

            "traffic_density": "medium"

        }

    },

    # 2
    {

        "name": "Безопасное перестроение",

        "expected": 1,

        "params": {

            "distance_front": 30,
            "speed": 90,
            "speed_front": 50,

            "left_distance": 60,
            "right_distance": 15,

            "left_speed": 80,
            "right_speed": 100,

            "can_change": 1,

            "weather": "dry",
            "road_type": "city",
            "road_damage": "good",

            "visibility": 500,

            "traffic_density": "low"

        }

    },

    # 3
    {

        "name": "Туман в сельской местности",

        "expected": 3,

        "params": {

            "distance_front": 25,
            "speed": 80,
            "speed_front": 60,

            "left_distance": 40,
            "right_distance": 40,

            "left_speed": 70,
            "right_speed": 70,

            "can_change": 1,

            "weather": "fog",
            "road_type": "rural",
            "road_damage": "good",

            "visibility": 20,

            "traffic_density": "low"

        }

    }

]


correct = 0

for test in test_cases:

    x = list(test["params"].values())

    # преобразование строк в числа
    weather_map = {
        "dry": 0,
        "rain": 1,
        "fog": 2,
        "snow": 3
    }

    road_map = {
        "city": 0,
        "highway": 1,
        "rural": 2
    }

    damage_map = {
        "good": 0,
        "bad": 1
    }

    traffic_map = {
        "low": 0,
        "medium": 1,
        "high": 2
    }

    x = [

        test["params"]["distance_front"],
        test["params"]["speed"],
        test["params"]["speed_front"],

        test["params"]["left_distance"],
        test["params"]["right_distance"],

        test["params"]["left_speed"],
        test["params"]["right_speed"],

        test["params"]["can_change"],

        weather_map[
            test["params"]["weather"]
        ],

        road_map[
            test["params"]["road_type"]
        ],

        damage_map[
            test["params"]["road_damage"]
        ],

        test["params"]["visibility"],

        traffic_map[
            test["params"]["traffic_density"]
        ]

    ]

    x_tensor = torch.tensor(
        x,
        dtype=torch.float32
    )

    output = model(x_tensor)

    pred = torch.argmax(output).item()

    print("\n====================")
    print(test["name"])

    print(f"Ожидалось: {test['expected']}")
    print(f"MLP: {pred}")

    if pred == test["expected"]:

        print("SUCCESS")
        correct += 1

    else:

        print("FAIL")

accuracy = correct / len(test_cases)

print("\n====================")
print(f"MLP ACCURACY: {accuracy:.2f}")