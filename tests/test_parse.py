import pytest

from chromato import parse, spaces

NON_COLOR_VALUES = [".", "f0x", (666, 0, 0), {"x": 1, "y": 1}]


def test_parse_hex():
    # valid
    assert parse.parse_hex(spaces.Color(255, 0, 0)) == "ff0000"
    assert parse.parse_hex(spaces.CMYK(0, 100, 100, 0)) == "ff0000"
    assert parse.parse_hex(spaces.HEX("ff0000")) == "ff0000"
    assert parse.parse_hex(spaces.HSL(0, 1, 0.5)) == "ff0000"
    assert parse.parse_hex(spaces.HSV(0, 1, 1)) == "ff0000"
    assert parse.parse_hex(spaces.RGB(255, 0, 0)) == "ff0000"
    assert parse.parse_hex({"hex": "ff0000"}) == "ff0000"
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
        "ab",
        "abcd",
        "abcde",
        "abcdefg",
        12,
        1234,
        12345,
        1234567,
    ] + NON_COLOR_VALUES

    for value in invalid_values:
        with pytest.raises(ValueError):
            parse.parse_hex(value)


def test_parse_hsv():
    # valid
    assert parse.parse_hsv(spaces.Color(255, 0, 0)) == (0, 1, 1)
    assert parse.parse_hsv(spaces.CMYK(0, 100, 100, 0)) == (0, 1, 1)
    assert parse.parse_hsv(spaces.HEX("ff0000")) == (0, 1, 1)
    assert parse.parse_hsv(spaces.HSL(0, 1, 0.5)) == (0, 1, 1)
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
    assert parse.parse_hsv({"h": 1, "s": 0.5, "v": 0.2}) == (1, 0.5, 0.2)
    assert parse.parse_hsv("ff0000") == (0, 1, 1)
    assert parse.parse_hsv("#ff0000") == (0, 1, 1)
    assert parse.parse_hsv("#f00") == (0, 1, 1)
    assert parse.parse_hsv("f00") == (0, 1, 1)
    assert parse.parse_hsv("") == (0, 0, 0)
    assert parse.parse_hsv(False) == (0, 0, 0)
    assert parse.parse_hsv(None) == (0, 0, 0)

    # invalid
    for value in NON_COLOR_VALUES:
        with pytest.raises(ValueError):
            parse.parse_hsv(value)


def test_parse_hsl():
    # valid
    assert parse.parse_hsl(spaces.Color(255, 0, 0)) == (0, 1, 0.5)
    assert parse.parse_hsl(spaces.CMYK(0, 100, 100, 0)) == (0, 1, 0.5)
    assert parse.parse_hsl(spaces.HEX("ff0000")) == (0, 1, 0.5)
    assert parse.parse_hsl(spaces.HSL(0, 1, 0.5)) == (0, 1, 0.5)
    assert parse.parse_hsl(spaces.HSV(0, 1, 1)) == (0, 1, 0.5)
    assert parse.parse_hsl(spaces.RGB(255, 0, 0)) == (0, 1, 0.5)
    assert parse.parse_hsl(0) == (0, 0, 0)
    assert parse.parse_hsl(1) == (1, 0, 0)
    assert parse.parse_hsl(1, 0.5) == (1, 0.5, 0)
    assert parse.parse_hsl(1, 0.5, 0.2) == (1, 0.5, 0.2)
    assert parse.parse_hsl(1, 0.5, 0.2) == (1, 0.5, 0.2)
    assert parse.parse_hsl("1", "0.5", "0.2") == (1, 0.5, 0.2)
    assert parse.parse_hsl((1, 0.5, 0.2)) == (1, 0.5, 0.2)
    assert parse.parse_hsl({"h": 1, "s": 0.5, "l": 0.2}) == (1, 0.5, 0.2)
    assert parse.parse_hsl("ff0000") == (0, 1, 0.5)
    assert parse.parse_hsl("#ff0000") == (0, 1, 0.5)
    assert parse.parse_hsl("#f00") == (0, 1, 0.5)
    assert parse.parse_hsl("f00") == (0, 1, 0.5)
    assert parse.parse_hsl("") == (0, 0, 0)
    assert parse.parse_hsl(False) == (0, 0, 0)
    assert parse.parse_hsl(None) == (0, 0, 0)

    # invalid
    invalid_values = ["f0x", (1.1, 0, 0), {"x": 1, "y": 1}]

    for value in invalid_values:
        with pytest.raises(ValueError):
            parse.parse_hsl(value)


def test_parse_cmyk():
    # valid
    assert parse.parse_cmyk(spaces.Color(255, 0, 0)) == (0, 100, 100, 0)
    assert parse.parse_cmyk(spaces.CMYK(0, 100, 100, 0)) == (0, 100, 100, 0)
    assert parse.parse_cmyk(spaces.HEX("ff0000")) == (0, 100, 100, 0)
    assert parse.parse_cmyk(spaces.HSL(0, 1, 0.5)) == (0, 100, 100, 0)
    assert parse.parse_cmyk(spaces.HSV(0, 1, 1)) == (0, 100, 100, 0)
    assert parse.parse_cmyk(spaces.RGB(255, 0, 0)) == (0, 100, 100, 0)
    assert parse.parse_cmyk(0) == (0, 0, 0, 100)
    assert parse.parse_cmyk(50) == (50, 0, 0, 100)
    assert parse.parse_cmyk(50, 20) == (50, 20, 0, 100)
    assert parse.parse_cmyk(50, 20, 10) == (50, 20, 10, 100)
    assert parse.parse_cmyk(50, 20, 10, 5) == (50, 20, 10, 5)
    assert parse.parse_cmyk("50", "20", "10", "5") == (50, 20, 10, 5)
    assert parse.parse_cmyk((50, 20, 10, 5)) == (50, 20, 10, 5)
    assert parse.parse_cmyk([50, 20, 10, 5]) == (50, 20, 10, 5)
    assert parse.parse_cmyk({"c": 50, "m": 20, "y": 10, "k": 5}) == (50, 20, 10, 5)
    assert parse.parse_cmyk("ff0000") == (0, 100, 100, 0)
    assert parse.parse_cmyk("#ff0000") == (0, 100, 100, 0)
    assert parse.parse_cmyk("#f00") == (0, 100, 100, 0)
    assert parse.parse_cmyk("f00") == (0, 100, 100, 0)
    assert parse.parse_cmyk("") == (0, 0, 0, 100)
    assert parse.parse_cmyk(False) == (0, 0, 0, 100)
    assert parse.parse_cmyk(None) == (0, 0, 0, 100)

    # invalid
    for value in NON_COLOR_VALUES:
        with pytest.raises(ValueError):
            parse.parse_cmyk(value)


def test_parse_rgb():
    # valid
    assert parse.parse_rgb(spaces.Color(255, 0, 0)) == (255, 0, 0)
    assert parse.parse_rgb(spaces.CMYK(0, 100, 100, 0)) == (255, 0, 0)
    assert parse.parse_rgb(spaces.HEX("ff0000")) == (255, 0, 0)
    assert parse.parse_rgb(spaces.HSL(0, 1, 0.5)) == (255, 0, 0)
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
    assert parse.parse_rgb({"r": 255, "g": 50, "b": 100}) == (255, 50, 100)
    assert parse.parse_rgb("ff0000") == (255, 0, 0)
    assert parse.parse_rgb("#ff0000") == (255, 0, 0)
    assert parse.parse_rgb("#f00") == (255, 0, 0)
    assert parse.parse_rgb("f00") == (255, 0, 0)
    assert parse.parse_rgb("") == (0, 0, 0)
    assert parse.parse_rgb(False) == (0, 0, 0)
    assert parse.parse_rgb(None) == (0, 0, 0)

    # invalid
    for value in NON_COLOR_VALUES:
        with pytest.raises(ValueError):
            parse.parse_rgb(value)
