from cmyko import math


def test_lerp():
    assert math.lerp(10, 0, 0) == 10
    assert math.lerp(0, 10, 0.5) == 5
    assert math.lerp(10, 1, 0.5) == 5.5
    assert math.lerp(1, 2, 0.5) == 1.5
    assert math.lerp(1, 2, 1) == 2


def test_float_to_rgb_value():
    assert math.float_to_rgb_value(1 / 3) == 0.3333


def test_sum_of_max_and_min():
    assert math.sum_of_max_and_min(10, 5, 8) == 15
