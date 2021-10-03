from cmyko import cmyko, spaces

RGB_RED = spaces.RGB(255, 0, 0)
HEX_RED = spaces.HEX("ff0000")
CMYK_RED = spaces.CMYK(0, 100, 100, 0)


# classes
def test_color():
    color = cmyko.Color(RGB_RED)
    assert color == cmyko.Color.from_hex(HEX_RED)
    assert color.rgb == RGB_RED
    assert color.hex == HEX_RED
    assert color.cmyk == CMYK_RED
    assert color.hls == spaces.HLS(0, 127.5, -1.007905138339921)
    assert color.hsv == spaces.HSV(0, 1, 255)
    assert color.yiq == spaces.YIQ(76.5, 152.745, 54.315)
