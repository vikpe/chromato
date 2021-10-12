from chromato.spaces import Color, CMYK, HEX, HLS, HSV, RGB


def test_hex():
    assert "ff0000" == HEX("f00") == HEX(HEX("f00"))


def test_construct():
    red_hex = HEX("f00")
    red_cmyk = CMYK(0, 100, 100, 0)
    red_hls = HLS(0, 0.5, 1)
    red_hsv = HSV(0, 1, 1)
    red_rgb = RGB(255, 0, 0)
    assert (
        Color(red_hex)
        == Color(red_cmyk)
        == Color(red_hls)
        == Color(red_hsv)
        == Color(red_rgb)
    )


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
