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
