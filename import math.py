import math

# ------------------------------------------------
# МАНЕВРЫ
# 0 = прямо
# 1 = влево
# 2 = вправо
# 3 = торможение
# ------------------------------------------------

def smart_rule_based(

    distance_front,      # м
    speed,               # км/ч
    speed_front,         # км/ч

    left_distance,       # м
    right_distance,      # м

    left_speed,          # км/ч
    right_speed,         # км/ч

    can_change,          # 0/1

    weather              # "dry" или "rain"

):

    # ------------------------------------------------
    # ПЕРЕВОД СКОРОСТИ В м/с
    # ------------------------------------------------

    speed_ms = speed / 3.6
    speed_front_ms = speed_front / 3.6

    relative_speed = speed_ms - speed_front_ms

    # ------------------------------------------------
    # ТОРМОЗНОЙ ПУТЬ
    # ------------------------------------------------

    reaction_time = 1.0

    if weather == "dry":
        friction = 7.0

    elif weather == "rain":
        friction = 4.0

    else:
        friction = 5.0

    braking_distance = (
        speed_ms * reaction_time
        + (speed_ms ** 2) / (2 * friction)
    )

    # ------------------------------------------------
    # ВРЕМЯ ДО СТОЛКНОВЕНИЯ
    # ------------------------------------------------

    if relative_speed > 0:

        collision_time = (
            distance_front / relative_speed
        )

    else:

        collision_time = math.inf

    # ------------------------------------------------
    # КРИТИЧЕСКАЯ СИТУАЦИЯ
    # ------------------------------------------------

    if (
        distance_front < braking_distance
        or collision_time < 2
    ):

        return 3

    # ------------------------------------------------
    # ПРОВЕРКА ЛЕВОЙ ПОЛОСЫ
    # ------------------------------------------------

    left_safe = (

        left_distance > 20
        and left_speed < speed + 30

    )

    # ------------------------------------------------
    # ПРОВЕРКА ПРАВОЙ ПОЛОСЫ
    # ------------------------------------------------

    right_safe = (

        right_distance > 20
        and right_speed < speed + 30

    )

    # ------------------------------------------------
    # ПЕРЕСТРОЕНИЕ
    # ------------------------------------------------

    if (
        distance_front < 25
        and can_change
    ):

        if left_safe:
            return 1

        elif right_safe:
            return 2

    # ------------------------------------------------
    # ОБЫЧНОЕ ДВИЖЕНИЕ
    # ------------------------------------------------

    return 0