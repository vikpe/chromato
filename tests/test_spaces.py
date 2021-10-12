from chromato.spaces import Color, CMYK, HEX, HLS, HSV, RGB


def test_hex():
    assert "ff0000" == HEX("f00") == HEX(HEX("f00"))


def test_color_class_methods():
    c_hex = Color.from_hex("f00")
    c_cmyk = Color.from_cmyk(0, 100, 100, 0)
    c_hls = Color.from_hls(0, 0.5, 1)
    c_hsv = Color.from_hsv(0, 1, 1)
    c_rgb = Color.from_rgb(255, 0, 0)
    assert c_hex == c_cmyk == c_hls == c_hsv == c_rgb


def test_color_properties():
    color = Color(255, 0, 0)
    assert color.rgb == RGB(255, 0, 0)
    assert color.hex == HEX("ff0000")
    assert color.cmyk == CMYK(0, 100, 100, 0)
    assert color.hls == HLS(0, 0.5, 1)
    assert color.hsv == HSV(0, 1, 1)
    assert color == Color("ff0000")
    assert color != "255 0 0"
    assert repr(color) == "Color(r=255, g=0, b=0)"
