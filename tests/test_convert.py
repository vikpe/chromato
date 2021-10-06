from chromato import convert, spaces

# CMYK
CMYK_WHITE = spaces.CMYK(0, 0, 0, 0)
CMYK_GRAY = spaces.CMYK(0, 0, 0, 100 * 2 / 3)
CMYK_BLACK = spaces.CMYK(0, 0, 0, 100)
CMYK_RED = spaces.CMYK(0, 100, 100, 0)
CMYK_GREEN = spaces.CMYK(100, 0, 100, 0)
CMYK_BLUE = spaces.CMYK(100, 100, 0, 0)

# HEX
HEX_WHITE = spaces.HEX("ffffff")
HEX_GRAY = spaces.HEX("555555")
HEX_BLACK = spaces.HEX("000000")
HEX_RED = spaces.HEX("ff0000")
HEX_GREEN = spaces.HEX("00ff00")
HEX_BLUE = spaces.HEX("0000ff")

# HLS
HLS_WHITE = spaces.HLS(0, 1, 0)
HLS_GRAY = spaces.HLS(0, 1 / 3, 0)
HLS_BLACK = spaces.HLS(0, 0, 0)
HLS_RED = spaces.HLS(0, 0.5, 1)
HLS_GREEN = spaces.HLS(1 / 3, 0.5, 1)
HLS_BLUE = spaces.HLS(2 / 3, 0.5, 1)

# HSV
HSV_WHITE = spaces.HSV(0, 0, 1)
HSV_GRAY = spaces.HSV(0, 0, 1 / 3)
HSV_BLACK = spaces.HSV(0, 0, 0)
HSV_RED = spaces.HSV(0, 1, 1)
HSV_GREEN = spaces.HSV(1 / 3, 1, 1)
HSV_BLUE = spaces.HSV(2 / 3, 1, 1)

# RGB
RGB_WHITE = spaces.RGB(255, 255, 255)
RGB_GRAY = spaces.RGB(85, 85, 85)
RGB_BLACK = spaces.RGB(0, 0, 0)
RGB_RED = spaces.RGB(255, 0, 0)
RGB_GREEN = spaces.RGB(0, 255, 0)
RGB_BLUE = spaces.RGB(0, 0, 255)


def test_cmyk_to_rgb():
    assert convert.cmyk_to_rgb(CMYK_WHITE) == RGB_WHITE
    assert convert.cmyk_to_rgb(CMYK_GRAY) == RGB_GRAY
    assert convert.cmyk_to_rgb(CMYK_BLACK) == RGB_BLACK
    assert convert.cmyk_to_rgb(CMYK_RED) == RGB_RED
    assert convert.cmyk_to_rgb(CMYK_GREEN) == RGB_GREEN
    assert convert.cmyk_to_rgb(CMYK_BLUE) == RGB_BLUE

    assert convert.cmyk_to_rgb(*CMYK_WHITE) == RGB_WHITE
    assert convert.cmyk_to_rgb(0, 0, 0, 0) == RGB_WHITE
    assert convert.cmyk_to_rgb((0, 0, 0, 0)) == RGB_WHITE
    assert convert.cmyk_to_rgb([0, 0, 0, 0]) == RGB_WHITE


def test_cmyk_to_hex():
    assert convert.cmyk_to_hex(CMYK_WHITE) == HEX_WHITE
    assert convert.cmyk_to_hex(CMYK_GRAY) == HEX_GRAY
    assert convert.cmyk_to_hex(CMYK_BLACK) == HEX_BLACK
    assert convert.cmyk_to_hex(CMYK_RED) == HEX_RED
    assert convert.cmyk_to_hex(CMYK_GREEN) == HEX_GREEN
    assert convert.cmyk_to_hex(CMYK_BLUE) == HEX_BLUE

    assert convert.cmyk_to_hex(*CMYK_WHITE) == HEX_WHITE
    assert convert.cmyk_to_hex(0, 0, 0, 0) == HEX_WHITE
    assert convert.cmyk_to_hex((0, 0, 0, 0)) == HEX_WHITE
    assert convert.cmyk_to_hex([0, 0, 0, 0]) == HEX_WHITE


def test_cmyk_to_hls():
    assert convert.cmyk_to_hls(CMYK_WHITE) == HLS_WHITE
    assert convert.cmyk_to_hls(CMYK_GRAY) == HLS_GRAY
    assert convert.cmyk_to_hls(CMYK_BLACK) == HLS_BLACK
    assert convert.cmyk_to_hls(CMYK_RED) == HLS_RED
    assert convert.cmyk_to_hls(CMYK_GREEN) == HLS_GREEN
    assert convert.cmyk_to_hls(CMYK_BLUE) == HLS_BLUE

    assert convert.cmyk_to_hls(*CMYK_WHITE) == HLS_WHITE
    assert convert.cmyk_to_hls(0, 0, 0, 0) == HLS_WHITE
    assert convert.cmyk_to_hls((0, 0, 0, 0)) == HLS_WHITE
    assert convert.cmyk_to_hls([0, 0, 0, 0]) == HLS_WHITE


def test_cmyk_to_hsv():
    assert convert.cmyk_to_hsv(CMYK_WHITE) == HSV_WHITE
    assert convert.cmyk_to_hsv(CMYK_GRAY) == HSV_GRAY
    assert convert.cmyk_to_hsv(CMYK_BLACK) == HSV_BLACK
    assert convert.cmyk_to_hsv(CMYK_RED) == HSV_RED
    assert convert.cmyk_to_hsv(CMYK_GREEN) == HSV_GREEN
    assert convert.cmyk_to_hsv(CMYK_BLUE) == HSV_BLUE

    assert convert.cmyk_to_hsv(*CMYK_WHITE) == HSV_WHITE
    assert convert.cmyk_to_hsv(0, 0, 0, 0) == HSV_WHITE
    assert convert.cmyk_to_hsv((0, 0, 0, 0)) == HSV_WHITE
    assert convert.cmyk_to_hsv([0, 0, 0, 0]) == HSV_WHITE


def test_hex_to_cmyk():
    assert convert.hex_to_cmyk(HEX_WHITE) == CMYK_WHITE
    assert convert.hex_to_cmyk(HEX_GRAY) == CMYK_GRAY
    assert convert.hex_to_cmyk(HEX_BLACK) == CMYK_BLACK
    assert convert.hex_to_cmyk(HEX_RED) == CMYK_RED
    assert convert.hex_to_cmyk(HEX_GREEN) == CMYK_GREEN
    assert convert.hex_to_cmyk(HEX_BLUE) == CMYK_BLUE

    assert convert.hex_to_cmyk("fff") == CMYK_WHITE
    assert convert.hex_to_cmyk("#fff") == CMYK_WHITE
    assert convert.hex_to_cmyk("ffffff") == CMYK_WHITE
    assert convert.hex_to_cmyk("#ffffff") == CMYK_WHITE


def test_hex_to_hls():
    assert convert.hex_to_hls(HEX_WHITE) == HLS_WHITE
    assert convert.hex_to_hls(HEX_GRAY) == HLS_GRAY
    assert convert.hex_to_hls(HEX_BLACK) == HLS_BLACK
    assert convert.hex_to_hls(HEX_RED) == HLS_RED
    assert convert.hex_to_hls(HEX_GREEN) == HLS_GREEN
    assert convert.hex_to_hls(HEX_BLUE) == HLS_BLUE

    assert convert.hex_to_hls("fff") == HLS_WHITE
    assert convert.hex_to_hls("#fff") == HLS_WHITE
    assert convert.hex_to_hls("ffffff") == HLS_WHITE
    assert convert.hex_to_hls("#ffffff") == HLS_WHITE


def test_hex_to_hsv():
    assert convert.hex_to_hsv(HEX_WHITE) == HSV_WHITE
    assert convert.hex_to_hsv(HEX_GRAY) == HSV_GRAY
    assert convert.hex_to_hsv(HEX_BLACK) == HSV_BLACK
    assert convert.hex_to_hsv(HEX_RED) == HSV_RED
    assert convert.hex_to_hsv(HEX_GREEN) == HSV_GREEN
    assert convert.hex_to_hsv(HEX_BLUE) == HSV_BLUE

    assert convert.hex_to_hsv("fff") == HSV_WHITE
    assert convert.hex_to_hsv("#fff") == HSV_WHITE
    assert convert.hex_to_hsv("ffffff") == HSV_WHITE
    assert convert.hex_to_hsv("#ffffff") == HSV_WHITE


def test_hex_to_rgb():
    assert convert.hex_to_rgb(HEX_WHITE) == RGB_WHITE
    assert convert.hex_to_rgb(HEX_GRAY) == RGB_GRAY
    assert convert.hex_to_rgb(HEX_BLACK) == RGB_BLACK
    assert convert.hex_to_rgb(HEX_RED) == RGB_RED
    assert convert.hex_to_rgb(HEX_GREEN) == RGB_GREEN
    assert convert.hex_to_rgb(HEX_BLUE) == RGB_BLUE

    assert convert.hex_to_rgb("fff") == RGB_WHITE
    assert convert.hex_to_rgb("#fff") == RGB_WHITE
    assert convert.hex_to_rgb("ffffff") == RGB_WHITE
    assert convert.hex_to_rgb("#ffffff") == RGB_WHITE


def test_rgb_to_hex():
    assert convert.rgb_to_hex(RGB_WHITE) == HEX_WHITE
    assert convert.rgb_to_hex(RGB_GRAY) == HEX_GRAY
    assert convert.rgb_to_hex(RGB_BLACK) == HEX_BLACK
    assert convert.rgb_to_hex(RGB_RED) == HEX_RED
    assert convert.rgb_to_hex(RGB_GREEN) == HEX_GREEN
    assert convert.rgb_to_hex(RGB_BLUE) == HEX_BLUE

    assert convert.rgb_to_hex(*RGB_WHITE) == HEX_WHITE
    assert convert.rgb_to_hex(255, 255, 255) == HEX_WHITE
    assert convert.rgb_to_hex((255, 255, 255)) == HEX_WHITE
    assert convert.rgb_to_hex([255, 255, 255]) == HEX_WHITE


def test_rgb_to_cmyk():
    assert convert.rgb_to_cmyk(RGB_WHITE) == CMYK_WHITE
    assert convert.rgb_to_cmyk(RGB_GRAY) == CMYK_GRAY
    assert convert.rgb_to_cmyk(RGB_BLACK) == CMYK_BLACK
    assert convert.rgb_to_cmyk(RGB_RED) == CMYK_RED
    assert convert.rgb_to_cmyk(RGB_GREEN) == CMYK_GREEN
    assert convert.rgb_to_cmyk(RGB_BLUE) == CMYK_BLUE

    assert convert.rgb_to_cmyk(*RGB_WHITE) == CMYK_WHITE
    assert convert.rgb_to_cmyk(255, 255, 255) == CMYK_WHITE
    assert convert.rgb_to_cmyk((255, 255, 255)) == CMYK_WHITE
    assert convert.rgb_to_cmyk([255, 255, 255]) == CMYK_WHITE


def test_rgb_to_hls():
    assert convert.rgb_to_hls(RGB_WHITE) == HLS_WHITE
    assert convert.rgb_to_hls(RGB_GRAY) == HLS_GRAY
    assert convert.rgb_to_hls(RGB_BLACK) == HLS_BLACK
    assert convert.rgb_to_hls(RGB_RED) == HLS_RED
    assert convert.rgb_to_hls(RGB_GREEN) == HLS_GREEN
    assert convert.rgb_to_hls(RGB_BLUE) == HLS_BLUE

    assert convert.rgb_to_hls(*RGB_WHITE) == HLS_WHITE
    assert convert.rgb_to_hls(255, 255, 255) == HLS_WHITE
    assert convert.rgb_to_hls((255, 255, 255)) == HLS_WHITE
    assert convert.rgb_to_hls([255, 255, 255]) == HLS_WHITE


def test_hls_to_rgb():
    assert convert.hls_to_rgb(HLS_WHITE) == RGB_WHITE
    assert convert.hls_to_rgb(HLS_GRAY) == RGB_GRAY
    assert convert.hls_to_rgb(HLS_BLACK) == RGB_BLACK
    assert convert.hls_to_rgb(HLS_RED) == RGB_RED
    assert convert.hls_to_rgb(HLS_GREEN) == RGB_GREEN
    assert convert.hls_to_rgb(HLS_BLUE) == RGB_BLUE

    assert convert.hls_to_rgb(*HLS_WHITE) == RGB_WHITE
    assert convert.hls_to_rgb(0, 1, 0) == RGB_WHITE
    assert convert.hls_to_rgb((0, 1, 0)) == RGB_WHITE
    assert convert.hls_to_rgb([0, 1, 0]) == RGB_WHITE


def test_rgb_to_hsv():
    assert convert.rgb_to_hsv(RGB_WHITE) == HSV_WHITE
    assert convert.rgb_to_hsv(RGB_GRAY) == HSV_GRAY
    assert convert.rgb_to_hsv(RGB_BLACK) == HSV_BLACK
    assert convert.rgb_to_hsv(RGB_RED) == HSV_RED
    assert convert.rgb_to_hsv(RGB_GREEN) == HSV_GREEN
    assert convert.rgb_to_hsv(RGB_BLUE) == HSV_BLUE

    assert convert.rgb_to_hsv(*RGB_WHITE) == HSV_WHITE
    assert convert.rgb_to_hsv(255, 255, 255) == HSV_WHITE
    assert convert.rgb_to_hsv((255, 255, 255)) == HSV_WHITE
    assert convert.rgb_to_hsv([255, 255, 255]) == HSV_WHITE


def test_hsv_to_rgb():
    assert convert.hsv_to_rgb(HSV_WHITE) == RGB_WHITE
    assert convert.hsv_to_rgb(HSV_GRAY) == RGB_GRAY
    assert convert.hsv_to_rgb(HSV_BLACK) == RGB_BLACK
    assert convert.hsv_to_rgb(HSV_RED) == RGB_RED
    assert convert.hsv_to_rgb(HSV_GREEN) == RGB_GREEN
    assert convert.hsv_to_rgb(HSV_BLUE) == RGB_BLUE

    assert convert.hsv_to_rgb(*HSV_WHITE) == RGB_WHITE
    assert convert.hsv_to_rgb(0, 0, 1) == RGB_WHITE
    assert convert.hsv_to_rgb((0, 0, 1)) == RGB_WHITE
    assert convert.hsv_to_rgb([0, 0, 1]) == RGB_WHITE
