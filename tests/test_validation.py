from chromato import validation

NON_VALUES = [
    False, None, "", [], (), {}
]


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

    for v in NON_VALUES:
        assert validation.is_valid_rgb_value(v) is False


def test_is_valid_rgb_value():
    # valid
    assert validation.is_valid_rgb_value(0) is True
    assert validation.is_valid_rgb_value(127.5) is True
    assert validation.is_valid_rgb_value(255) is True
    assert validation.is_valid_rgb_value("255") is True
    assert validation.is_valid_rgb_value("255.0") is True

    # invalid
    assert validation.is_valid_rgb_value(-0.1) is False
    assert validation.is_valid_rgb_value(255.1) is False
    assert validation.is_valid_rgb_value("a") is False

    for v in NON_VALUES:
        assert validation.is_valid_rgb_value(v) is False


def test_is_valid_rgb():
    assert validation.is_valid_rgb(0, 0, 0) is True
    assert validation.is_valid_rgb("255", 0, 0.5) is True

    assert validation.is_valid_rgb("a", 0, 0) is False
    assert validation.is_valid_rgb(255, -0.1, 0) is False


def test_is_valid_cmyk_value():
    # valid
    assert validation.is_valid_cmyk_value(0) is True
    assert validation.is_valid_cmyk_value(50.1) is True
    assert validation.is_valid_cmyk_value(100) is True
    assert validation.is_valid_cmyk_value("100") is True
    assert validation.is_valid_cmyk_value("100.0") is True

    # invalid
    assert validation.is_valid_cmyk_value(-0.1) is False
    assert validation.is_valid_cmyk_value(100.5) is False
    assert validation.is_valid_cmyk_value("a") is False

    for v in NON_VALUES:
        assert validation.is_valid_cmyk_value(v) is False


def test_is_valid_cmyk():
    assert validation.is_valid_cmyk(0, 0, 0, 0) is True
    assert validation.is_valid_cmyk("100", 0, 0.5, 0) is True

    assert validation.is_valid_cmyk(0, 0, 0, "a") is False
    assert validation.is_valid_cmyk(0, 0, -0.1, 0) is False


def test_is_valid_hls_value():
    # valid
    assert validation.is_valid_hls_value(0) is True
    assert validation.is_valid_hls_value(0.5) is True
    assert validation.is_valid_hls_value(1) is True
    assert validation.is_valid_hls_value("1") is True
    assert validation.is_valid_hls_value("1.0") is True

    # invalid
    assert validation.is_valid_hls_value(-0.1) is False
    assert validation.is_valid_hls_value(1.1) is False
    assert validation.is_valid_hls_value("a") is False

    for v in NON_VALUES:
        assert validation.is_valid_hls_value(v) is False


def test_is_valid_hls():
    assert validation.is_valid_hls(0, 0, 0) is True
    assert validation.is_valid_hls("1", 0, 0.5) is True

    assert validation.is_valid_hls(0, 0, "a") is False
    assert validation.is_valid_hls(0, -0.1, 0) is False


def test_is_valid_hsv_value():
    # valid
    assert validation.is_valid_hsv_value(0) is True
    assert validation.is_valid_hsv_value(0.5) is True
    assert validation.is_valid_hsv_value(1) is True
    assert validation.is_valid_hsv_value("1") is True
    assert validation.is_valid_hsv_value("1.0") is True

    # invalid
    assert validation.is_valid_hsv_value(-0.1) is False
    assert validation.is_valid_hsv_value(1.1) is False
    assert validation.is_valid_hsv_value("a") is False

    for v in NON_VALUES:
        assert validation.is_valid_hsv_value(v) is False


def test_is_valid_hsv():
    assert validation.is_valid_hsv(0, 0, 0) is True
    assert validation.is_valid_hsv("1", 0, 0.5) is True

    assert validation.is_valid_hsv(0, 0, "a") is False
    assert validation.is_valid_hsv(0, -0.1, 0) is False
