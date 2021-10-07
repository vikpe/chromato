from chromato import validation
from helpers import assert_all_true, assert_all_false

NON_VALUES = [False, None, "", [], (), {}]


def test_is_valid_number():
    valid = [0, 0.5, 1]
    assert_all_true(validation.is_valid_number, valid)

    invalid = ["0", "0.5", "1"] + NON_VALUES
    assert_all_false(validation.is_valid_number, invalid)


def test_is_in_range():
    assert validation.is_in_range(0.5, 0, 1) is True
    assert validation.is_in_range(0.5, 0, 0.5) is True

    assert validation.is_in_range(0.5, 0, 0.4) is False
    assert validation.is_in_range("0.5", 0, 0.4) is False
    assert validation.is_in_range(False, 0, 0.4) is False


def test_is_valid_hex():
    valid = ["000000", "ffffff", "ff00ff", "112233"]
    assert_all_true(validation.is_valid_hex, valid)

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
    assert_all_false(validation.is_valid_hex, invalid)


def test_is_valid_rgb_value():
    valid = [0, 127.5, 255]
    assert_all_true(validation.is_valid_rgb_value, valid)

    invalid = ["255", "255.0", -0.1, 255.1, "a"] + NON_VALUES
    assert_all_false(validation.is_valid_rgb_value, invalid)


def test_is_valid_rgb():
    assert validation.is_valid_rgb(0, 50, 255) is True

    assert validation.is_valid_rgb("255", 0, 0.5) is False
    assert validation.is_valid_rgb("a", 0, 0) is False
    assert validation.is_valid_rgb(255, -0.1, 0) is False


def test_is_valid_cmyk_value():
    valid = [0, 50.1, 100]
    assert_all_true(validation.is_valid_cmyk_value, valid)

    invalid = ["50.1", -0.1, 100.1, "a"] + NON_VALUES
    assert_all_false(validation.is_valid_cmyk_value, invalid)


def test_is_valid_cmyk():
    assert validation.is_valid_cmyk(0, 50, 100, 0) is True

    assert validation.is_valid_cmyk("100", 0, 0.5, 0) is False
    assert validation.is_valid_cmyk(0, 0, 0, "a") is False
    assert validation.is_valid_cmyk(0, 0, -0.1, 0) is False


def test_is_valid_hls_value():
    valid = [0, 0.5, 1]
    assert_all_true(validation.is_valid_hls_value, valid)

    invalid = ["0.5", -0.1, 1.1, "a"] + NON_VALUES
    assert_all_false(validation.is_valid_hls_value, invalid)


def test_is_valid_hls():
    assert validation.is_valid_hls(0, 0.5, 0) is True

    assert validation.is_valid_hls("1", 0, 0.5) is False
    assert validation.is_valid_hls(0, 0, "a") is False
    assert validation.is_valid_hls(0, -0.1, 0) is False


def test_is_valid_hsv_value():
    valid = [0, 0.5, 1]
    assert_all_true(validation.is_valid_hsv_value, valid)

    invalid = ["0.5", -0.1, 1.1, "a"] + NON_VALUES
    assert_all_false(validation.is_valid_hsv_value, invalid)


def test_is_valid_hsv():
    assert validation.is_valid_hsv(0, 0.5, 0) is True

    assert validation.is_valid_hsv("1", 0, 0.5) is False
    assert validation.is_valid_hsv(0, 0, "a") is False
    assert validation.is_valid_hsv(0, -0.1, 0) is False
