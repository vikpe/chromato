from chromato import spaces


def test_color():
    color = spaces.Color(255, 0, 0)

    assert color.rgb == spaces.RGB(255, 0, 0)
    assert color.hex == spaces.HEX("ff0000")
    assert color.cmyk == spaces.CMYK(0, 100, 100, 0)
    assert color.hls == spaces.HLS(0, 0.5, 1)
    assert color.hsv == spaces.HSV(0, 1, 1)
    assert color == spaces.Color("ff0000")
    assert color != "255 0 0"
