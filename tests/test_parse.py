import pytest

from chromato import parse, spaces


def test_parse_hex():
    assert parse.parse_hex(spaces.CMYK(0, 100, 100, 0)) == "ff0000"
    assert parse.parse_hex(spaces.HEX("ff0000")) == "ff0000"
    assert parse.parse_hex(spaces.HLS(0, 0.5, 1)) == "ff0000"
    assert parse.parse_hex(spaces.HSV(0, 1, 1)) == "ff0000"
    assert parse.parse_hex(spaces.RGB(255, 0, 0)) == "ff0000"
    assert parse.parse_hex("ff33ff") == "ff33ff"
    assert parse.parse_hex("#ff33ff") == "ff33ff"
    assert parse.parse_hex(3) == "333333"
    assert parse.parse_hex(333) == "333333"
    assert parse.parse_hex(333333) == "333333"
    assert parse.parse_hex("f") == "ffffff"
    assert parse.parse_hex("#f") == "ffffff"
    assert parse.parse_hex("f3f") == "ff33ff"
    assert parse.parse_hex("#f3f") == "ff33ff"
    assert parse.parse_hex(" f3f") == "ff33ff"
    assert parse.parse_hex(" f3f ") == "ff33ff"
    assert parse.parse_hex("f3f ") == "ff33ff"
    assert parse.parse_hex("") == "000000"
    assert parse.parse_hex(False) == "000000"
    assert parse.parse_hex(None) == "000000"

    # invalid
    invalid_values = [
        "fox",
        "ab",
        "abcd",
        "abcde",
        "abcdefg",
        12,
        1234,
        12345,
        1234567,
        (255, 0, 0),
    ]

    for value in invalid_values:
        with pytest.raises(ValueError):
            parse.parse_hex(value)


def test_parse_hsv():
    assert parse.parse_hsv(spaces.CMYK(0, 100, 100, 0)) == (0, 1, 1)
    assert parse.parse_hsv(spaces.HEX("ff0000")) == (0, 1, 1)
    assert parse.parse_hsv(spaces.HLS(0, 0.5, 1)) == (0, 1, 1)
    assert parse.parse_hsv(spaces.HSV(0, 1, 1)) == (0, 1, 1)
    assert parse.parse_hsv(spaces.RGB(255, 0, 0)) == (0, 1, 1)
    assert parse.parse_hsv(0) == (0, 0, 0)
    assert parse.parse_hsv(1) == (1, 0, 0)
    assert parse.parse_hsv(1, 0.5) == (1, 0.5, 0)
    assert parse.parse_hsv(1, 0.5, 0.2) == (1, 0.5, 0.2)
    assert parse.parse_hsv(1, 0.5, 0.2) == (1, 0.5, 0.2)
    assert parse.parse_hsv("1", "0.5", "0.2") == (1, 0.5, 0.2)
    assert parse.parse_hsv((1, 0.5, 0.2)) == (1, 0.5, 0.2)
    assert parse.parse_hsv([1, 0.5, 0.2]) == (1, 0.5, 0.2)
    assert parse.parse_hsv("") == (0, 0, 0)
    assert parse.parse_hsv(False) == (0, 0, 0)
    assert parse.parse_hsv(None) == (0, 0, 0)

    # invalid
    invalid_values = ["a", (255, 0, 0)]

    for value in invalid_values:
        with pytest.raises(ValueError):
            parse.parse_hsv(value)


def test_parse_hls():
    assert parse.parse_hls(spaces.CMYK(0, 100, 100, 0)) == (0, 0.5, 1)
    assert parse.parse_hls(spaces.HEX("ff0000")) == (0, 0.5, 1)
    assert parse.parse_hls(spaces.HLS(0, 0.5, 1)) == (0, 0.5, 1)
    assert parse.parse_hls(spaces.HSV(0, 1, 1)) == (0, 0.5, 1)
    assert parse.parse_hls(spaces.RGB(255, 0, 0)) == (0, 0.5, 1)
    assert parse.parse_hls(0) == (0, 0, 0)
    assert parse.parse_hls(1) == (1, 0, 0)
    assert parse.parse_hls(1, 0.5) == (1, 0.5, 0)
    assert parse.parse_hls(1, 0.5, 0.2) == (1, 0.5, 0.2)
    assert parse.parse_hls(1, 0.5, 0.2) == (1, 0.5, 0.2)
    assert parse.parse_hls("1", "0.5", "0.2") == (1, 0.5, 0.2)
    assert parse.parse_hls((1, 0.5, 0.2)) == (1, 0.5, 0.2)
    assert parse.parse_hls("") == (0, 0, 0)
    assert parse.parse_hls(False) == (0, 0, 0)
    assert parse.parse_hls(None) == (0, 0, 0)

    # invalid
    invalid_values = ["a", (255, 0, 0)]

    for value in invalid_values:
        with pytest.raises(ValueError):
            parse.parse_hls(value)


def test_parse_cmyk():
    assert parse.parse_cmyk(spaces.CMYK(0, 100, 100, 0)) == (0, 0.5, 1)
    assert parse.parse_cmyk(spaces.HEX("ff0000")) == (0, 0.5, 1)
    assert parse.parse_cmyk(spaces.HLS(0, 0.5, 1)) == (0, 0.5, 1)
    assert parse.parse_cmyk(spaces.HSV(0, 1, 1)) == (0, 0.5, 1)
    assert parse.parse_cmyk(spaces.RGB(255, 0, 0)) == (0, 0.5, 1)
    assert parse.parse_cmyk(0) == (0, 0, 0, 100)
    assert parse.parse_cmyk(50) == (50, 0, 0, 100)
    assert parse.parse_cmyk(50, 20) == (50, 20, 0, 100)
    assert parse.parse_cmyk(50, 20, 10) == (50, 20, 10, 100)
    assert parse.parse_cmyk(50, 20, 10, 5) == (50, 20, 10, 5)
    assert parse.parse_cmyk("50", "20", "10", "5") == (50, 20, 10, 5)
    assert parse.parse_cmyk((50, 20, 10, 5)) == (50, 20, 10, 5)
    assert parse.parse_cmyk([50, 20, 10, 5]) == (50, 20, 10, 5)
    assert parse.parse_cmyk("") == (0, 0, 0, 100)
    assert parse.parse_cmyk(False) == (0, 0, 0, 100)
    assert parse.parse_cmyk(None) == (0, 0, 0, 100)

    # invalid
    invalid_values = ["a", (255, 0, 0)]

    for value in invalid_values:
        with pytest.raises(ValueError):
            parse.parse_cmyk(value)


def test_parse_rgb():
    # valid
    assert parse.parse_rgb(spaces.CMYK(0, 100, 100, 0)) == (255, 0, 0)
    assert parse.parse_rgb(spaces.HEX("ff0000")) == (0, 0.5, 1)
    assert parse.parse_rgb(spaces.HLS(0, 0.5, 1)) == (255, 0, 0)
    assert parse.parse_rgb(spaces.HSV(0, 1, 1)) == (255, 0, 0)
    assert parse.parse_rgb(spaces.RGB(255, 0, 0)) == (255, 0, 0)
    assert parse.parse_rgb() == (0, 0, 0)
    assert parse.parse_rgb(255) == (255, 0, 0)
    assert parse.parse_rgb(254.5) == (255, 0, 0)
    assert parse.parse_rgb(255, 50) == (255, 50, 0)
    assert parse.parse_rgb(255, 50, 100) == (255, 50, 100)
    assert parse.parse_rgb((255, 0, 0)) == (255, 0, 0)
    assert parse.parse_rgb([255, 0, 0]) == (255, 0, 0)
    assert parse.parse_rgb((0, 0, 0)) == (0, 0, 0)
    assert parse.parse_rgb(("255", "50", "100")) == (255, 50, 100)
    assert parse.parse_rgb(["255", "50", "100"]) == (255, 50, 100)
    assert parse.parse_rgb("") == (0, 0, 0)
    assert parse.parse_rgb(False) == (0, 0, 0)
    assert parse.parse_rgb(None) == (0, 0, 0)

    # invalid
    invalid_values = ["x", "f00f", "_"]

    for value in invalid_values:
        with pytest.raises(ValueError):
            parse.parse_rgb(value)


def test_parse():
    # valid
    assert parse.parse_value() == (0, 0, 0)
    assert parse.parse_value(255) == (255, 0, 0)
    assert parse.parse_value(255.0) == (255, 0, 0)
    assert parse.parse_value(255, 50) == (255, 50, 0)
    assert parse.parse_value(255, 50, 100) == (255, 50, 100)
    assert parse.parse_value((255, 0, 0)) == (255, 0, 0)
    assert parse.parse_value([255, 0, 0]) == (255, 0, 0)
    assert parse.parse_value((0, 0, 0)) == (0, 0, 0)
    assert parse.parse_value(("255", "50", "100")) == (255, 50, 100)
    assert parse.parse_value(["254.5", 50, 99.5]) == (255, 50, 100)
    assert parse.parse_value(spaces.RGB(255, 50, 100)) == (255, 50, 100)
    assert parse.parse_value(spaces.CMYK(100, 0, 0, 0)) == (0, 255, 255)
    assert parse.parse_value(spaces.HSV(0, 1, 1)) == (255, 0, 0)
    assert parse.parse_value(spaces.HLS(0, 0.5, 1)) == (255, 0, 0)
    assert parse.parse_value(spaces.HEX("ff0000")) == (255, 0, 0)
    assert parse.parse_value("ff0000") == (255, 0, 0)
    assert parse.parse_value("#ff0000") == (255, 0, 0)
    assert parse.parse_value("#f00") == (255, 0, 0)
    assert parse.parse_value("f00") == (255, 0, 0)
    assert parse.parse_value("") == (0, 0, 0)
    assert parse.parse_value(False) == (0, 0, 0)
    assert parse.parse_value(None) == (0, 0, 0)

    # invalid
    invalid_values = ["x", "f00f", "_"]

    for value in invalid_values:
        with pytest.raises(ValueError):
            parse.parse_value(value)
