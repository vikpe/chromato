from chromato import utils


def test_lerp():
    assert utils.lerp(10, 0, 0) == 10
    assert utils.lerp(0, 10, 0.5) == 5
    assert utils.lerp(10, 1, 0.5) == 5.5
    assert utils.lerp(1, 2, 0.5) == 1.5
    assert utils.lerp(1, 2, 1) == 2


def test_dict_has_keys():
    rgb_dict = {
        "r": 255,
        "g": 255,
        "b": 255,
    }
    assert utils.dict_has_keys(rgb_dict, "r")
    assert utils.dict_has_keys(rgb_dict, "rgb")
    assert not utils.dict_has_keys(rgb_dict, "rgbA")
