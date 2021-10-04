from cmyko import cmyko, spaces

RGB_RED = spaces.RGB(255, 0, 0)
HEX_RED = spaces.HEX("ff0000")


def test_color():
    color = cmyko.Color(RGB_RED)
    assert color == cmyko.Color.from_hex(HEX_RED)
    assert color.rgb == RGB_RED
    assert color.hex == HEX_RED
    assert color.cmyk == spaces.CMYK(0, 100, 100, 0)
    assert color.hls == spaces.HLS(0, 0.5, 1)
    assert color.hsv == spaces.HSV(0, 1, 1)
