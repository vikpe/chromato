from cmyko import math


def test_lerp():
    assert math.lerp(10, 0, 0) == 10
    assert math.lerp(0, 10, 0.5) == 5
    assert math.lerp(10, 1, 0.5) == 5.5
    assert math.lerp(1, 2, 0.5) == 1.5
    assert math.lerp(1, 2, 1) == 2