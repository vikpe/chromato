from chromato import validation
from helpers import assert_all_true, assert_all_false

NON_VALUES = [False, None, "", [], (), {}]


def test_is_number():
    valid = [0, 0.5, 1]
    assert_all_true(validation.is_number, valid)

    invalid = ["0", "0.5", "1"] + NON_VALUES
    assert_all_false(validation.is_number, invalid)


def test_is_number_in_range():
    assert validation.is_number_in_range(0.5, 0, 1) is True
    assert validation.is_number_in_range(0.5, 0, 0.5) is True

    assert validation.is_number_in_range(0.5, 0, 0.4) is False
    assert validation.is_number_in_range("0.5", 0, 0.4) is False
    assert validation.is_number_in_range(False, 0, 0.4) is False


def test_is_hex():
    valid = ["000000", "ffffff", "ff00ff", "112233"]
    assert_all_true(validation.is_hex, valid)

    invalid = [
        "#ff00ff",
        112233,
        "#112233",
        "f0x",
        "a",
        "ab",
        "abcd",
        "abcde",
        "abcdefg",
    ] + NON_VALUES
    assert_all_false(validation.is_hex, invalid)


def test_is_rgb_value():
    valid = [0, 128, 255]
    assert_all_true(validation.is_rgb_value, valid)

    invalid = [0.1, "255", "255.0", -0.1, 255.1, "a"] + NON_VALUES
    assert_all_false(validation.is_rgb_value, invalid)


def test_is_rgb():
    assert validation.is_rgb(0, 50, 255) is True

    assert validation.is_rgb(255.1, 0, 0) is False
    assert validation.is_rgb("255", 0, 0.5) is False
    assert validation.is_rgb("a", 0, 0) is False
    assert validation.is_rgb(255, -0.1, 0) is False


def test_is_cmyk_value():
    valid = [0, 50.1, 100]
    assert_all_true(validation.is_cmyk_value, valid)

    invalid = ["50.1", -0.1, 100.1, "a"] + NON_VALUES
    assert_all_false(validation.is_cmyk_value, invalid)


def test_is_cmyk():
    assert validation.is_cmyk(0, 50, 100, 0) is True

    assert validation.is_cmyk("100", 0, 0.5, 0) is False
    assert validation.is_cmyk(0, 0, 0, "a") is False
    assert validation.is_cmyk(0, 0, -0.1, 0) is False


def test_is_hsl_value():
    valid = [0, 1, 0.5]
    assert_all_true(validation.is_hsl_value, valid)

    invalid = ["0.5", -0.1, 1.1, "a"] + NON_VALUES
    assert_all_false(validation.is_hsl_value, invalid)


def test_is_hsl():
    assert validation.is_hsl(0, 0.5, 0) is True

    assert validation.is_hsl("1", 0, 0.5) is False
    assert validation.is_hsl(0, 0, "a") is False
    assert validation.is_hsl(0, -0.1, 0) is False


def test_is_hsv_value():
    valid = [0, 0.5, 1]
    assert_all_true(validation.is_hsv_value, valid)

    invalid = ["0.5", -0.1, 1.1, "a"] + NON_VALUES
    assert_all_false(validation.is_hsv_value, invalid)


def test_is_hsv():
    assert validation.is_hsv(0, 0.5, 0) is True

    assert validation.is_hsv("1", 0, 0.5) is False
    assert validation.is_hsv(0, 0, "a") is False
    assert validation.is_hsv(0, -0.1, 0) is False
