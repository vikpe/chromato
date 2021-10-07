from chromato import validation
from helpers import assert_all_true, assert_all_false

NON_VALUES = [False, None, "", [], (), {}]


def test_is_valid_hex():
    valid = ["ff00ff", "#ff00ff", 111, 112233, "#f0ff0f"]
    assert_all_true(validation.is_valid_hex, valid)

    invalid = ["f0x", "a", "ab", "abcd", "abcde"]
    assert_all_false(validation.is_valid_hex, invalid)


def test_is_valid_rgb_value():
    valid = [0, 127.5, 255, "255", "255.0"]
    assert_all_true(validation.is_valid_rgb_value, valid)

    invalid = [-0.1, 255.1, "a"] + NON_VALUES
    assert_all_false(validation.is_valid_rgb_value, invalid)


def test_is_valid_rgb():
    assert validation.is_valid_rgb(0, 0, 0) is True
    assert validation.is_valid_rgb("255", 0, 0.5) is True

    assert validation.is_valid_rgb("a", 0, 0) is False
    assert validation.is_valid_rgb(255, -0.1, 0) is False


def test_is_valid_cmyk_value():
    valid = [0, 50.1, 100, "100", "100.0"]
    assert_all_true(validation.is_valid_cmyk_value, valid)

    invalid = [-0.1, 100.1, "a"] + NON_VALUES
    assert_all_false(validation.is_valid_cmyk_value, invalid)


def test_is_valid_cmyk():
    assert validation.is_valid_cmyk(0, 0, 0, 0) is True
    assert validation.is_valid_cmyk("100", 0, 0.5, 0) is True

    assert validation.is_valid_cmyk(0, 0, 0, "a") is False
    assert validation.is_valid_cmyk(0, 0, -0.1, 0) is False


def test_is_valid_hls_value():
    valid = [0, 0.5, 1, "1", "1.0"]
    assert_all_true(validation.is_valid_hls_value, valid)

    invalid = [-0.1, 1.1, "a"] + NON_VALUES
    assert_all_false(validation.is_valid_hls_value, invalid)


def test_is_valid_hls():
    assert validation.is_valid_hls(0, 0, 0) is True
    assert validation.is_valid_hls("1", 0, 0.5) is True

    assert validation.is_valid_hls(0, 0, "a") is False
    assert validation.is_valid_hls(0, -0.1, 0) is False


def test_is_valid_hsv_value():
    valid = [0, 0.5, 1, "1", "1.0"]
    assert_all_true(validation.is_valid_hsv_value, valid)

    invalid = [-0.1, 1.1, "a"] + NON_VALUES
    assert_all_false(validation.is_valid_hsv_value, invalid)


def test_is_valid_hsv():
    assert validation.is_valid_hsv(0, 0, 0) is True
    assert validation.is_valid_hsv("1", 0, 0.5) is True

    assert validation.is_valid_hsv(0, 0, "a") is False
    assert validation.is_valid_hsv(0, -0.1, 0) is False
