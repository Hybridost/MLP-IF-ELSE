import math

# МАНЕВРЫ
# 0 = прямо
# 1 = влево
# 2 = вправо
# 3 = торможение

def smart_rule_based(

    # ОСНОВНЫЕ ПАРАМЕТРЫ

    distance_front,      
    speed,               
    speed_front,         

    left_distance,       
    right_distance,      

    left_speed,          
    right_speed,         

    can_change,

    weather,             # dry/rain/fog/snow
    road_type,           # city/highway/rural
    road_damage,         # good/bad
    visibility,          
    traffic_density      # low/medium/high

):

    # ПЕРЕВОД В м/с

    speed_ms = speed / 3.6
    speed_front_ms = speed_front / 3.6

    relative_speed = speed_ms - speed_front_ms

    # БАЗОВЫЕ НАСТРОЙКИ

    safe_distance = 20

    lane_change_distance = 20

    emergency_distance = 8

    collision_time_limit = 1.5

    # ПОГОДА

    if weather == "rain":

        safe_distance += 10
        lane_change_distance += 10

    elif weather == "snow":

        safe_distance += 20
        lane_change_distance += 20

        collision_time_limit += 1

    elif weather == "fog":

        safe_distance += 15

        collision_time_limit += 1

    # ДОРОГА

    if road_type == "highway":

        safe_distance += 15

    elif road_type == "rural":
        safe_distance += 10


    # ПОВРЕЖДЕНИЯ ДОРОГИ

    if road_damage == "bad":
        lane_change_distance += 15

    # ВИДИМОСТЬ

    if visibility < 50:

        safe_distance += 20

        collision_time_limit += 1

    elif visibility < 100:

        safe_distance += 10


    # ПЛОТНОСТЬ ТРАФИКА

    if traffic_density == "high":

        lane_change_distance += 15

    elif traffic_density == "medium":

        lane_change_distance += 5


    # ВРЕМЯ ДО СТОЛКНОВЕНИЯ

    if relative_speed > 0:

        collision_time = (
            distance_front / relative_speed
        )

    else:

        collision_time = math.inf

    # ЭКСТРЕННОЕ ТОРМОЖЕНИЕ

    if (
        distance_front < emergency_distance
        or collision_time < collision_time_limit
    ):

        return 3

# УРОВЕНЬ ОПАСНОСТИ

    low_danger = (

        distance_front < safe_distance

        or collision_time < 4

    )

    medium_danger = (

        distance_front < safe_distance * 0.7

        or collision_time < 2.5

    )

    high_danger = (

        distance_front < emergency_distance

        or collision_time < collision_time_limit

    )

    # БЕЗОПАСНОСТЬ ЛЕВОЙ ПОЛОСЫ

    left_safe = (

        left_distance > lane_change_distance

        and left_speed < speed + 20

    )

    # БЕЗОПАСНОСТЬ ПРАВОЙ ПОЛОСЫ

    right_safe = (

        right_distance > lane_change_distance

        and right_speed < speed + 20

    )

# ПЕРЕСТРОЕНИЕ

    if low_danger and can_change:

        if left_safe:

            return 1

        elif right_safe:

            return 2

    # ТОРМОЖЕНИЕ

    if medium_danger:

        return 3

    # ОБЫЧНОЕ ДВИЖЕНИЕ

    return 0

# ТЕСТЫ

# print(

#     smart_rule_based(

#         distance_front = 30,
#         speed = 100,
#         speed_front = 60,

#         left_distance = 50,
#         right_distance = 50,

#         left_speed = 80,
#         right_speed = 80,

#         can_change = 1,

#         weather = "dry",
#         road_type = "city",
#         road_damage = "good",

#         visibility = 500,

#         traffic_density = "low"

#     )

# )

# print(

#     smart_rule_based(

#         distance_front = 30,
#         speed = 100,
#         speed_front = 60,

#         left_distance = 25,
#         right_distance = 25,

#         left_speed = 90,
#         right_speed = 90,

#         can_change = 1,

#         weather = "snow",
#         road_type = "highway",
#         road_damage = "good",

#         visibility = 40,

#         traffic_density = "high"

#     )

# )


result = smart_rule_based(

    distance_front = 30,
    speed = 90,
    speed_front = 50,

    left_distance = 60,
    right_distance = 15,

    left_speed = 80,
    right_speed = 100,

    can_change = 1,

    weather = "dry",
    road_type = "city",
    road_damage = "good",

    visibility = 500,

    traffic_density = "low"

)

print(result)