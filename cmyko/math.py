from .constants import RGB_PRECISION


def lerp(v1: float, v2: float, factor: float) -> float:
    return v1 + ((v2 - v1) * factor)


def float_to_rgb_value(value) -> float:
    return round(value, RGB_PRECISION)


def sum_of_max_and_min(a, b, c):
    if c < b:
        b, c = c, b
    if b < a:
        a, b = b, a
    if c < b:
        b, c = c, b
    return a + c
