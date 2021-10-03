from cmyko import parse


def test_parse_hex():
    assert parse.parse_hex("ff00ff") == "ff00ff"
    assert parse.parse_hex("#ff00ff") == "ff00ff"
    assert parse.parse_hex("f0f") == "ff00ff"
    assert parse.parse_hex("#f0f") == "ff00ff"
