from cmyko import validation


def test_is_valid_hex():
    # valid
    assert validation.is_valid_hex("ff00ff") is True
    assert validation.is_valid_hex("#ff00ff") is True
    assert validation.is_valid_hex(111) is True
    assert validation.is_valid_hex(112233) is True
    assert validation.is_valid_hex("#f0f") is True
    assert validation.is_valid_hex("f0f") is True

    # invalid
    assert validation.is_valid_hex("") is False
    assert validation.is_valid_hex("f0x") is False
    assert validation.is_valid_hex("a") is False
    assert validation.is_valid_hex("ab") is False
    assert validation.is_valid_hex("abcd") is False
    assert validation.is_valid_hex("abcde") is False


def test_is_valid_rgb_value():
    # valid
    assert validation.is_valid_rgb_value(0) is True
    assert validation.is_valid_rgb_value(127.5) is True
    assert validation.is_valid_rgb_value(255) is True
    assert validation.is_valid_rgb_value("255") is True
    assert validation.is_valid_rgb_value("255.0") is True

    # invalid
    assert validation.is_valid_rgb_value(-0.1) is False
    assert validation.is_valid_rgb_value(256) is False
    assert validation.is_valid_rgb_value("a") is False
    assert validation.is_valid_rgb_value(None) is False
    assert validation.is_valid_rgb_value([]) is False
    assert validation.is_valid_rgb_value(()) is False
