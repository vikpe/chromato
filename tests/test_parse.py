import pytest

from chromato import parse, spaces


def test_parse_hex():
    assert parse.parse_hex("ff00ff") == "ff00ff"
    assert parse.parse_hex("#ff00ff") == "ff00ff"
    assert parse.parse_hex("f0f") == "ff00ff"
    assert parse.parse_hex("#f0f") == "ff00ff"

    # invalid
    invalid_values = [None, False, " ", "fox", spaces.RGB(255, 0, 0)]

    for value in invalid_values:
        with pytest.raises(ValueError):
            parse.parse_hex(value)


def test_parse_hsv():
    hsv_black = spaces.HSV()

    assert parse.parse_hsv(0) == hsv_black
    assert parse.parse_hsv(False) == hsv_black
    assert parse.parse_hsv(1) == spaces.HSV(1, 0, 0)
    assert parse.parse_hsv(1, 0.5) == spaces.HSV(1, 0.5, 0)
    assert parse.parse_hsv(1, 0.5, 0.2) == spaces.HSV(1, 0.5, 0.2)
    assert parse.parse_hsv(1, 0.5, 0.2) == spaces.HSV(1, 0.5, 0.2)
    assert parse.parse_hsv("1", "0.5", "0.2") == spaces.HSV(1, 0.5, 0.2)
    assert parse.parse_hsv((1, 0.5, 0.2)) == spaces.HSV(1, 0.5, 0.2)
    assert parse.parse_hsv([1, 0.5, 0.2]) == spaces.HSV(1, 0.5, 0.2)
    assert parse.parse_hsv(spaces.HSV(0, 1, 0)) == spaces.HSV(0, 1, 0)

    # invalid
    invalid_values = [None, "a", spaces.RGB(255, 0, 0)]

    for value in invalid_values:
        with pytest.raises(ValueError):
            parse.parse_hsv(value)


def test_parse_hls():
    hls_black = spaces.HLS()

    assert parse.parse_hls(0) == hls_black
    assert parse.parse_hls(False) == hls_black
    assert parse.parse_hls(1) == spaces.HLS(1, 0, 0)
    assert parse.parse_hls(1, 0.5) == spaces.HLS(1, 0.5, 0)
    assert parse.parse_hls(1, 0.5, 0.2) == spaces.HLS(1, 0.5, 0.2)
    assert parse.parse_hls(1, 0.5, 0.2) == spaces.HLS(1, 0.5, 0.2)
    assert parse.parse_hls("1", "0.5", "0.2") == spaces.HLS(1, 0.5, 0.2)
    assert parse.parse_hls((1, 0.5, 0.2)) == spaces.HLS(1, 0.5, 0.2)
    assert parse.parse_hls([1, 0.5, 0.2]) == spaces.HLS(1, 0.5, 0.2)
    assert parse.parse_hls(spaces.HLS(0, 1, 0)) == spaces.HLS(0, 1, 0)

    # invalid
    invalid_values = [None, "a", spaces.RGB(255, 0, 0)]

    for value in invalid_values:
        with pytest.raises(ValueError):
            parse.parse_hls(value)


def test_parse_cmyk():
    cmyk_black = spaces.CMYK()

    assert parse.parse_cmyk(0) == cmyk_black
    assert parse.parse_cmyk(False) == cmyk_black
    assert parse.parse_cmyk(50) == spaces.CMYK(50, 0, 0, 100)
    assert parse.parse_cmyk(50, 20) == spaces.CMYK(50, 20, 0, 100)
    assert parse.parse_cmyk(50, 20, 10) == spaces.CMYK(50, 20, 10, 100)
    assert parse.parse_cmyk(50, 20, 10, 5) == spaces.CMYK(50, 20, 10, 5)
    assert parse.parse_cmyk("50", "20", "10", "5") == spaces.CMYK(50, 20, 10, 5)
    assert parse.parse_cmyk((50, 20, 10, 5)) == spaces.CMYK(50, 20, 10, 5)
    assert parse.parse_cmyk([50, 20, 10, 5]) == spaces.CMYK(50, 20, 10, 5)
    assert parse.parse_cmyk(spaces.CMYK(0, 50, 0, 50)) == spaces.CMYK(0, 50, 0, 50)

    # invalid
    invalid_values = [None, "a", spaces.RGB(255, 0, 0)]

    for value in invalid_values:
        with pytest.raises(ValueError):
            parse.parse_cmyk(value)


def test_parse():
    rgb_red = spaces.RGB(255, 0, 0)
    rgb_black = spaces.RGB()

    # valid
    assert parse.parse_value() == rgb_black
    assert parse.parse_value(None) == rgb_black
    assert parse.parse_value("") == rgb_black
    assert parse.parse_value(255) == rgb_red
    assert parse.parse_value(255, 50) == spaces.RGB(255, 50, 0)
    assert parse.parse_value(255, 50, 100) == spaces.RGB(255, 50, 100)
    assert parse.parse_value((255, 0, 0)) == rgb_red
    assert parse.parse_value([255, 0, 0]) == rgb_red
    assert parse.parse_value((0, 0, 0)) == rgb_black
    assert parse.parse_value((None, None, None)) == rgb_black
    assert parse.parse_value(("", "", "")) == rgb_black
    assert parse.parse_value(("255", "50", "100")) == spaces.RGB(255, 50, 100)
    assert parse.parse_value(["255", "50", "100"]) == spaces.RGB(255, 50, 100)
    assert parse.parse_value(spaces.RGB(255, 50, 100)) == spaces.RGB(255, 50, 100)
    assert parse.parse_value(spaces.CMYK(100, 0, 0, 0)) == spaces.RGB(0, 255, 255)
    assert parse.parse_value(spaces.HSV(0, 1, 1)) == rgb_red
    assert parse.parse_value(spaces.HLS(0, 0.5, 1)) == rgb_red
    assert parse.parse_value(spaces.HEX("ff0000")) == rgb_red
    assert parse.parse_value("ff0000") == rgb_red
    assert parse.parse_value("#ff0000") == rgb_red
    assert parse.parse_value("#f00") == rgb_red
    assert parse.parse_value("f00") == rgb_red

    # invalid
    invalid_values = ["x", "f00f", "_"]

    for value in invalid_values:
        with pytest.raises(ValueError):
            parse.parse_value(value)
