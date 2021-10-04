from cmyko import parse, spaces
import pytest


def test_parse_hex():
    assert parse.parse_hex("ff00ff") == "ff00ff"
    assert parse.parse_hex("#ff00ff") == "ff00ff"
    assert parse.parse_hex("f0f") == "ff00ff"
    assert parse.parse_hex("#f0f") == "ff00ff"


def test_parse():
    rgb_red = spaces.RGB(255, 0, 0)
    rgb_black = spaces.RGB(0, 0, 0)

    # valid
    assert parse.parse() == rgb_black
    assert parse.parse(None) == rgb_black
    assert parse.parse("") == rgb_black
    assert parse.parse(255) == rgb_red
    assert parse.parse(255, 50) == spaces.RGB(255, 50, 0)
    assert parse.parse(255, 50, 100) == spaces.RGB(255, 50, 100)
    assert parse.parse((255, 0, 0)) == rgb_red
    assert parse.parse([255, 0, 0]) == rgb_red
    assert parse.parse((0, 0, 0)) == rgb_black
    assert parse.parse((None, None, None)) == rgb_black
    assert parse.parse(("", "", "")) == rgb_black
    assert parse.parse(("255", "50", "100")) == spaces.RGB(255, 50, 100)
    assert parse.parse(["255", "50", "100"]) == spaces.RGB(255, 50, 100)
    assert parse.parse(spaces.RGB(255, 50, 100)) == spaces.RGB(255, 50, 100)
    assert parse.parse(spaces.CMYK(100, 0, 0, 0)) == spaces.RGB(0, 255, 255)
    assert parse.parse(spaces.HSV(0, 1, 1)) == rgb_red
    assert parse.parse(spaces.HLS(0, 0.5, 1)) == rgb_red
    assert parse.parse(spaces.HEX("ff0000")) == rgb_red
    assert parse.parse("ff0000") == rgb_red
    assert parse.parse("#ff0000") == rgb_red
    assert parse.parse("#f00") == rgb_red
    assert parse.parse("f00") == rgb_red

    # invalid
    invalid_values = ["x", "f00f", "_"]

    for value in invalid_values:
        with pytest.raises(ValueError):
            parse.parse(value)
