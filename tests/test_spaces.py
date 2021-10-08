from chromato import spaces


def test_color_class_methods():
    c_hex = spaces.Color.from_hex("f00")
    c_cmyk = spaces.Color.from_cmyk(0, 100, 100, 0)
    c_hls = spaces.Color.from_hls(0, 0.5, 1)
    c_hsv = spaces.Color.from_hsv(0, 1, 1)
    c_rgb = spaces.Color.from_rgb(255, 0, 0)
    assert c_hex == c_cmyk == c_hls == c_hsv == c_rgb


def test_color_properties():
    color = spaces.Color(255, 0, 0)
    assert color.rgb == spaces.RGB(255, 0, 0)
    assert color.hex == spaces.HEX("ff0000")
    assert color.cmyk == spaces.CMYK(0, 100, 100, 0)
    assert color.hls == spaces.HLS(0, 0.5, 1)
    assert color.hsv == spaces.HSV(0, 1, 1)
    assert color == spaces.Color("ff0000")
    assert color != "255 0 0"
