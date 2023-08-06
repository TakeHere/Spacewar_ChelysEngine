import math
import random

from Utils.Vector2 import Vector2


def random_direction():
    return Vector2(random.randint(-1000, 1000), random.randint(-1000, 1000)).normalize()


def get_forward_vector(rotation):
    radian_rotation = math.radians(rotation)
    forward_vector = Vector2(math.sin(radian_rotation), -math.cos(radian_rotation))
    return forward_vector


def map_range(value, from_min, from_max, to_min, to_max):
    value = max(from_min, min(from_max, value))

    return (value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)
