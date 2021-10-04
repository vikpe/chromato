from cmyko import convert, spaces

RGB_WHITE = spaces.RGB(255, 255, 255)
RGB_GRAY = spaces.RGB(127.5, 127.5, 127.5)
RGB_BLACK = spaces.RGB(0, 0, 0)
RGB_RED = spaces.RGB(255, 0, 0)
RGB_GREEN = spaces.RGB(0, 255, 0)
RGB_BLUE = spaces.RGB(0, 0, 255)

# HEX
HEX_WHITE = "ffffff"
HEX_GRAY = "7f7f7f"
HEX_BLACK = "000000"
HEX_RED = "ff0000"
HEX_GREEN = "00ff00"
HEX_BLUE = "0000ff"


def test_hex_to_rgb():
    assert convert.hex_to_rgb(HEX_WHITE) == RGB_WHITE
    assert convert.hex_to_rgb(HEX_GRAY) == spaces.RGB(127, 127, 127)
    assert convert.hex_to_rgb(HEX_BLACK) == RGB_BLACK
    assert convert.hex_to_rgb(HEX_RED) == RGB_RED
    assert convert.hex_to_rgb(HEX_GREEN) == RGB_GREEN
    assert convert.hex_to_rgb(HEX_BLUE) == RGB_BLUE


def test_rgb_to_hex():
    assert convert.rgb_to_hex(RGB_WHITE) == HEX_WHITE
    assert convert.rgb_to_hex(RGB_GRAY) == HEX_GRAY
    assert convert.rgb_to_hex(RGB_BLACK) == HEX_BLACK
    assert convert.rgb_to_hex(RGB_RED) == HEX_RED
    assert convert.rgb_to_hex(RGB_GREEN) == HEX_GREEN
    assert convert.rgb_to_hex(RGB_BLUE) == HEX_BLUE


# CMYK
CMYK_WHITE = spaces.CMYK(0, 0, 0, 0)
CMYK_GRAY = spaces.CMYK(0, 0, 0, 50)
CMYK_BLACK = spaces.CMYK(0, 0, 0, 100)
CMYK_RED = spaces.CMYK(0, 100, 100, 0)
CMYK_GREEN = spaces.CMYK(100, 0, 100, 0)
CMYK_BLUE = spaces.CMYK(100, 100, 0, 0)


def test_rgb_to_cmyk():
    assert convert.rgb_to_cmyk(RGB_WHITE) == CMYK_WHITE
    assert convert.rgb_to_cmyk(RGB_GRAY) == CMYK_GRAY
    assert convert.rgb_to_cmyk(RGB_BLACK) == CMYK_BLACK
    assert convert.rgb_to_cmyk(RGB_RED) == CMYK_RED
    assert convert.rgb_to_cmyk(RGB_GREEN) == CMYK_GREEN
    assert convert.rgb_to_cmyk(RGB_BLUE) == CMYK_BLUE


def test_cmyk_to_rgb():
    assert convert.cmyk_to_rgb(CMYK_WHITE) == RGB_WHITE
    assert convert.cmyk_to_rgb(CMYK_GRAY) == RGB_GRAY
    assert convert.cmyk_to_rgb(CMYK_BLACK) == RGB_BLACK
    assert convert.cmyk_to_rgb(CMYK_RED) == RGB_RED
    assert convert.cmyk_to_rgb(CMYK_GREEN) == RGB_GREEN
    assert convert.cmyk_to_rgb(CMYK_BLUE) == RGB_BLUE


# HLS
HLS_WHITE = spaces.HLS(0, 1, 0)
HLS_GRAY = spaces.HLS(0, 0.5, 0)
HLS_BLACK = spaces.HLS(0, 0, 0)
HLS_RED = spaces.HLS(0, 0.5, 1)
HLS_GREEN = spaces.HLS(1 / 3, 0.5, 1)
HLS_BLUE = spaces.HLS(2 / 3, 0.5, 1)


def test_rgb_to_hls():
    assert convert.rgb_to_hls(RGB_WHITE) == HLS_WHITE
    assert convert.rgb_to_hls(RGB_GRAY) == HLS_GRAY
    assert convert.rgb_to_hls(RGB_BLACK) == HLS_BLACK
    assert convert.rgb_to_hls(RGB_RED) == HLS_RED
    assert convert.rgb_to_hls(RGB_GREEN) == HLS_GREEN
    assert convert.rgb_to_hls(RGB_BLUE) == HLS_BLUE


def test_hls_to_rgb():
    assert convert.hls_to_rgb(HLS_WHITE) == RGB_WHITE
    assert convert.hls_to_rgb(HLS_GRAY) == RGB_GRAY
    assert convert.hls_to_rgb(HLS_BLACK) == RGB_BLACK
    assert convert.hls_to_rgb(HLS_RED) == RGB_RED
    assert convert.hls_to_rgb(HLS_GREEN) == RGB_GREEN
    assert convert.hls_to_rgb(HLS_BLUE) == RGB_BLUE


# HSV
HSV_WHITE = spaces.HSV(0, 0, 1)
HSV_GRAY = spaces.HSV(0, 0, 0.5)
HSV_BLACK = spaces.HSV(0, 0, 0)
HSV_RED = spaces.HSV(0, 1, 1)
HSV_GREEN = spaces.HSV(1 / 3, 1, 1)
HSV_BLUE = spaces.HSV(2 / 3, 1, 1)


def test_rgb_to_hsv():
    assert convert.rgb_to_hsv(RGB_WHITE) == HSV_WHITE
    assert convert.rgb_to_hsv(RGB_GRAY) == HSV_GRAY
    assert convert.rgb_to_hsv(RGB_BLACK) == HSV_BLACK
    assert convert.rgb_to_hsv(RGB_RED) == HSV_RED
    assert convert.rgb_to_hsv(RGB_GREEN) == HSV_GREEN
    assert convert.rgb_to_hsv(RGB_BLUE) == HSV_BLUE


def test_hsv_to_rgb():
    assert convert.hsv_to_rgb(HSV_WHITE) == RGB_WHITE
    assert convert.hsv_to_rgb(HSV_GRAY) == RGB_GRAY
    assert convert.hsv_to_rgb(HSV_BLACK) == RGB_BLACK
    assert convert.hsv_to_rgb(HSV_RED) == RGB_RED
    assert convert.hsv_to_rgb(HSV_GREEN) == RGB_GREEN
    assert convert.hsv_to_rgb(HSV_BLUE) == RGB_BLUE
