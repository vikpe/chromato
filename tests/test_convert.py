from chromato import convert, spaces

# Constants
CMYK_WHITE = spaces.CMYK(0, 0, 0, 0)
CMYK_GRAY = spaces.CMYK(0, 0, 0, 100 * 2 / 3)
CMYK_BLACK = spaces.CMYK(0, 0, 0, 100)
CMYK_RED = spaces.CMYK(0, 100, 100, 0)
CMYK_GREEN = spaces.CMYK(100, 0, 100, 0)
CMYK_BLUE = spaces.CMYK(100, 100, 0, 0)
CMYK_CYAN = spaces.CMYK(100, 0, 0, 0)
CMYK_MAGENTA = spaces.CMYK(0, 100, 0, 0)
CMYK_YELLOW = spaces.CMYK(0, 0, 100, 0)

HEX_WHITE = spaces.HEX("ffffff")
HEX_GRAY = spaces.HEX("555555")
HEX_BLACK = spaces.HEX("000000")
HEX_RED = spaces.HEX("ff0000")
HEX_GREEN = spaces.HEX("00ff00")
HEX_BLUE = spaces.HEX("0000ff")
HEX_CYAN = spaces.HEX("00ffff")
HEX_MAGENTA = spaces.HEX("ff00ff")
HEX_YELLOW = spaces.HEX("ffff00")

HLS_WHITE = spaces.HLS(0, 1, 0)
HLS_GRAY = spaces.HLS(0, 1 / 3, 0)
HLS_BLACK = spaces.HLS(0, 0, 0)
HLS_RED = spaces.HLS(0, 0.5, 1)
HLS_GREEN = spaces.HLS(1 / 3, 0.5, 1)
HLS_BLUE = spaces.HLS(2 / 3, 0.5, 1)
HLS_CYAN = spaces.HLS(1 / 2, 0.5, 1)
HLS_MAGENTA = spaces.HLS(5 / 6, 0.5, 1)
HLS_YELLOW = spaces.HLS(1 / 6, 0.5, 1)

HSV_WHITE = spaces.HSV(0, 0, 1)
HSV_GRAY = spaces.HSV(0, 0, 1 / 3)
HSV_BLACK = spaces.HSV(0, 0, 0)
HSV_RED = spaces.HSV(0, 1, 1)
HSV_GREEN = spaces.HSV(1 / 3, 1, 1)
HSV_BLUE = spaces.HSV(2 / 3, 1, 1)
HSV_CYAN = spaces.HSV(1 / 2, 1, 1)
HSV_MAGENTA = spaces.HSV(5 / 6, 1, 1)
HSV_YELLOW = spaces.HSV(1 / 6, 1, 1)

RGB_WHITE = spaces.RGB(255, 255, 255)
RGB_GRAY = spaces.RGB(85, 85, 85)
RGB_BLACK = spaces.RGB(0, 0, 0)
RGB_RED = spaces.RGB(255, 0, 0)
RGB_GREEN = spaces.RGB(0, 255, 0)
RGB_BLUE = spaces.RGB(0, 0, 255)
RGB_CYAN = spaces.RGB(0, 255, 255)
RGB_MAGENTA = spaces.RGB(255, 0, 255)
RGB_YELLOW = spaces.RGB(255, 255, 0)


# CMYK conversion
def test_cmyk_to_rgb():
    assert convert.cmyk_to_rgb(CMYK_WHITE) == RGB_WHITE
    assert convert.cmyk_to_rgb(CMYK_GRAY) == RGB_GRAY
    assert convert.cmyk_to_rgb(CMYK_BLACK) == RGB_BLACK
    assert convert.cmyk_to_rgb(CMYK_RED) == RGB_RED
    assert convert.cmyk_to_rgb(CMYK_GREEN) == RGB_GREEN
    assert convert.cmyk_to_rgb(CMYK_BLUE) == RGB_BLUE
    assert convert.cmyk_to_rgb(CMYK_CYAN) == RGB_CYAN
    assert convert.cmyk_to_rgb(CMYK_MAGENTA) == RGB_MAGENTA
    assert convert.cmyk_to_rgb(CMYK_YELLOW) == RGB_YELLOW

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
    assert convert.cmyk_to_hex(CMYK_CYAN) == HEX_CYAN
    assert convert.cmyk_to_hex(CMYK_MAGENTA) == HEX_MAGENTA
    assert convert.cmyk_to_hex(CMYK_YELLOW) == HEX_YELLOW

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
    assert convert.cmyk_to_hls(CMYK_CYAN) == HLS_CYAN
    assert convert.cmyk_to_hls(CMYK_MAGENTA) == HLS_MAGENTA
    assert convert.cmyk_to_hls(CMYK_YELLOW) == HLS_YELLOW

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
    assert convert.cmyk_to_hsv(CMYK_CYAN) == HSV_CYAN
    assert convert.cmyk_to_hsv(CMYK_MAGENTA) == HSV_MAGENTA
    assert convert.cmyk_to_hsv(CMYK_YELLOW) == HSV_YELLOW

    assert convert.cmyk_to_hsv(*CMYK_WHITE) == HSV_WHITE
    assert convert.cmyk_to_hsv(0, 0, 0, 0) == HSV_WHITE
    assert convert.cmyk_to_hsv((0, 0, 0, 0)) == HSV_WHITE
    assert convert.cmyk_to_hsv([0, 0, 0, 0]) == HSV_WHITE


# HEX conversion
def test_hex_to_cmyk():
    assert convert.hex_to_cmyk(HEX_WHITE) == CMYK_WHITE
    assert convert.hex_to_cmyk(HEX_GRAY) == CMYK_GRAY
    assert convert.hex_to_cmyk(HEX_BLACK) == CMYK_BLACK
    assert convert.hex_to_cmyk(HEX_RED) == CMYK_RED
    assert convert.hex_to_cmyk(HEX_GREEN) == CMYK_GREEN
    assert convert.hex_to_cmyk(HEX_BLUE) == CMYK_BLUE
    assert convert.hex_to_cmyk(HEX_CYAN) == CMYK_CYAN
    assert convert.hex_to_cmyk(HEX_MAGENTA) == CMYK_MAGENTA
    assert convert.hex_to_cmyk(HEX_YELLOW) == CMYK_YELLOW

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
    assert convert.hex_to_hls(HEX_CYAN) == HLS_CYAN
    assert convert.hex_to_hls(HEX_MAGENTA) == HLS_MAGENTA
    assert convert.hex_to_hls(HEX_YELLOW) == HLS_YELLOW

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
    assert convert.hex_to_hsv(HEX_CYAN) == HSV_CYAN
    assert convert.hex_to_hsv(HEX_MAGENTA) == HSV_MAGENTA
    assert convert.hex_to_hsv(HEX_YELLOW) == HSV_YELLOW

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
    assert convert.hex_to_rgb(HEX_CYAN) == RGB_CYAN
    assert convert.hex_to_rgb(HEX_MAGENTA) == RGB_MAGENTA
    assert convert.hex_to_rgb(HEX_YELLOW) == RGB_YELLOW

    assert convert.hex_to_rgb("fff") == RGB_WHITE
    assert convert.hex_to_rgb("#fff") == RGB_WHITE
    assert convert.hex_to_rgb("ffffff") == RGB_WHITE
    assert convert.hex_to_rgb("#ffffff") == RGB_WHITE


# HLS conversion
def test_hls_to_rgb():
    assert convert.hls_to_rgb(HLS_WHITE) == RGB_WHITE
    assert convert.hls_to_rgb(HLS_GRAY) == RGB_GRAY
    assert convert.hls_to_rgb(HLS_BLACK) == RGB_BLACK
    assert convert.hls_to_rgb(HLS_RED) == RGB_RED
    assert convert.hls_to_rgb(HLS_GREEN) == RGB_GREEN
    assert convert.hls_to_rgb(HLS_BLUE) == RGB_BLUE
    assert convert.hls_to_rgb(HLS_CYAN) == RGB_CYAN
    assert convert.hls_to_rgb(HLS_MAGENTA) == RGB_MAGENTA
    assert convert.hls_to_rgb(HLS_YELLOW) == RGB_YELLOW

    assert convert.hls_to_rgb(*HLS_WHITE) == RGB_WHITE
    assert convert.hls_to_rgb(0, 1, 0) == RGB_WHITE
    assert convert.hls_to_rgb((0, 1, 0)) == RGB_WHITE
    assert convert.hls_to_rgb([0, 1, 0]) == RGB_WHITE


def test_hls_to_cmyk():
    assert convert.hls_to_cmyk(HLS_WHITE) == CMYK_WHITE
    assert convert.hls_to_cmyk(HLS_GRAY) == CMYK_GRAY
    assert convert.hls_to_cmyk(HLS_BLACK) == CMYK_BLACK
    assert convert.hls_to_cmyk(HLS_RED) == CMYK_RED
    assert convert.hls_to_cmyk(HLS_GREEN) == CMYK_GREEN
    assert convert.hls_to_cmyk(HLS_BLUE) == CMYK_BLUE
    assert convert.hls_to_cmyk(HLS_CYAN) == CMYK_CYAN
    assert convert.hls_to_cmyk(HLS_MAGENTA) == CMYK_MAGENTA
    assert convert.hls_to_cmyk(HLS_YELLOW) == CMYK_YELLOW

    assert convert.hls_to_cmyk(*HLS_WHITE) == CMYK_WHITE
    assert convert.hls_to_cmyk(0, 1, 0) == CMYK_WHITE
    assert convert.hls_to_cmyk((0, 1, 0)) == CMYK_WHITE
    assert convert.hls_to_cmyk([0, 1, 0]) == CMYK_WHITE


def test_hls_to_hex():
    assert convert.hls_to_hex(HLS_WHITE) == HEX_WHITE
    assert convert.hls_to_hex(HLS_GRAY) == HEX_GRAY
    assert convert.hls_to_hex(HLS_BLACK) == HEX_BLACK
    assert convert.hls_to_hex(HLS_RED) == HEX_RED
    assert convert.hls_to_hex(HLS_GREEN) == HEX_GREEN
    assert convert.hls_to_hex(HLS_BLUE) == HEX_BLUE
    assert convert.hls_to_hex(HLS_CYAN) == HEX_CYAN
    assert convert.hls_to_hex(HLS_MAGENTA) == HEX_MAGENTA
    assert convert.hls_to_hex(HLS_YELLOW) == HEX_YELLOW

    assert convert.hls_to_hex(*HLS_WHITE) == HEX_WHITE
    assert convert.hls_to_hex(0, 1, 0) == HEX_WHITE
    assert convert.hls_to_hex((0, 1, 0)) == HEX_WHITE
    assert convert.hls_to_hex([0, 1, 0]) == HEX_WHITE


def test_hls_to_hsv():
    assert convert.hls_to_hsv(HLS_WHITE) == HSV_WHITE
    assert convert.hls_to_hsv(HLS_GRAY) == HSV_GRAY
    assert convert.hls_to_hsv(HLS_BLACK) == HSV_BLACK
    assert convert.hls_to_hsv(HLS_RED) == HSV_RED
    assert convert.hls_to_hsv(HLS_GREEN) == HSV_GREEN
    assert convert.hls_to_hsv(HLS_BLUE) == HSV_BLUE
    assert convert.hls_to_hsv(HLS_CYAN) == HSV_CYAN
    assert convert.hls_to_hsv(HLS_MAGENTA) == HSV_MAGENTA
    assert convert.hls_to_hsv(HLS_YELLOW) == HSV_YELLOW

    assert convert.hls_to_hsv(*HLS_WHITE) == HSV_WHITE
    assert convert.hls_to_hsv(0, 1, 0) == HSV_WHITE
    assert convert.hls_to_hsv((0, 1, 0)) == HSV_WHITE
    assert convert.hls_to_hsv([0, 1, 0]) == HSV_WHITE


# HSV conversion
def test_hsv_to_cmyk():
    assert convert.hsv_to_cmyk(HSV_WHITE) == CMYK_WHITE
    assert convert.hsv_to_cmyk(HSV_GRAY) == CMYK_GRAY
    assert convert.hsv_to_cmyk(HSV_BLACK) == CMYK_BLACK
    assert convert.hsv_to_cmyk(HSV_RED) == CMYK_RED
    assert convert.hsv_to_cmyk(HSV_GREEN) == CMYK_GREEN
    assert convert.hsv_to_cmyk(HSV_BLUE) == CMYK_BLUE
    assert convert.hsv_to_cmyk(HSV_CYAN) == CMYK_CYAN
    assert convert.hsv_to_cmyk(HSV_MAGENTA) == CMYK_MAGENTA
    assert convert.hsv_to_cmyk(HSV_YELLOW) == CMYK_YELLOW

    assert convert.hsv_to_cmyk(*HSV_WHITE) == CMYK_WHITE
    assert convert.hsv_to_cmyk(0, 0, 1) == CMYK_WHITE
    assert convert.hsv_to_cmyk((0, 0, 1)) == CMYK_WHITE
    assert convert.hsv_to_cmyk([0, 0, 1]) == CMYK_WHITE


def test_hsv_to_hex():
    assert convert.hsv_to_hex(HSV_WHITE) == HEX_WHITE
    assert convert.hsv_to_hex(HSV_GRAY) == HEX_GRAY
    assert convert.hsv_to_hex(HSV_BLACK) == HEX_BLACK
    assert convert.hsv_to_hex(HSV_RED) == HEX_RED
    assert convert.hsv_to_hex(HSV_GREEN) == HEX_GREEN
    assert convert.hsv_to_hex(HSV_BLUE) == HEX_BLUE
    assert convert.hsv_to_hex(HSV_CYAN) == HEX_CYAN
    assert convert.hsv_to_hex(HSV_MAGENTA) == HEX_MAGENTA
    assert convert.hsv_to_hex(HSV_YELLOW) == HEX_YELLOW

    assert convert.hsv_to_hex(*HSV_WHITE) == HEX_WHITE
    assert convert.hsv_to_hex(0, 0, 1) == HEX_WHITE
    assert convert.hsv_to_hex((0, 0, 1)) == HEX_WHITE
    assert convert.hsv_to_hex([0, 0, 1]) == HEX_WHITE


def test_hsv_to_hls():
    assert convert.hsv_to_hls(HSV_WHITE) == HLS_WHITE
    assert convert.hsv_to_hls(HSV_GRAY) == HLS_GRAY
    assert convert.hsv_to_hls(HSV_BLACK) == HLS_BLACK
    assert convert.hsv_to_hls(HSV_RED) == HLS_RED
    assert convert.hsv_to_hls(HSV_GREEN) == HLS_GREEN
    assert convert.hsv_to_hls(HSV_BLUE) == HLS_BLUE
    assert convert.hsv_to_hls(HSV_CYAN) == HLS_CYAN
    assert convert.hsv_to_hls(HSV_MAGENTA) == HLS_MAGENTA
    assert convert.hsv_to_hls(HSV_YELLOW) == HLS_YELLOW

    assert convert.hsv_to_hls(*HSV_WHITE) == HLS_WHITE
    assert convert.hsv_to_hls(0, 0, 1) == HLS_WHITE
    assert convert.hsv_to_hls((0, 0, 1)) == HLS_WHITE
    assert convert.hsv_to_hls([0, 0, 1]) == HLS_WHITE


def test_hsv_to_rgb():
    assert convert.hsv_to_rgb(HSV_WHITE) == RGB_WHITE
    assert convert.hsv_to_rgb(HSV_GRAY) == RGB_GRAY
    assert convert.hsv_to_rgb(HSV_BLACK) == RGB_BLACK
    assert convert.hsv_to_rgb(HSV_RED) == RGB_RED
    assert convert.hsv_to_rgb(HSV_GREEN) == RGB_GREEN
    assert convert.hsv_to_rgb(HSV_BLUE) == RGB_BLUE
    assert convert.hsv_to_rgb(HSV_CYAN) == RGB_CYAN
    assert convert.hsv_to_rgb(HSV_MAGENTA) == RGB_MAGENTA
    assert convert.hsv_to_rgb(HSV_YELLOW) == RGB_YELLOW

    assert convert.hsv_to_rgb(*HSV_WHITE) == RGB_WHITE
    assert convert.hsv_to_rgb(0, 0, 1) == RGB_WHITE
    assert convert.hsv_to_rgb((0, 0, 1)) == RGB_WHITE
    assert convert.hsv_to_rgb([0, 0, 1]) == RGB_WHITE


# RGB conversion
def test_rgb_to_cmyk():
    assert convert.rgb_to_cmyk(RGB_WHITE) == CMYK_WHITE
    assert convert.rgb_to_cmyk(RGB_GRAY) == CMYK_GRAY
    assert convert.rgb_to_cmyk(RGB_BLACK) == CMYK_BLACK
    assert convert.rgb_to_cmyk(RGB_RED) == CMYK_RED
    assert convert.rgb_to_cmyk(RGB_GREEN) == CMYK_GREEN
    assert convert.rgb_to_cmyk(RGB_BLUE) == CMYK_BLUE
    assert convert.rgb_to_cmyk(RGB_CYAN) == CMYK_CYAN
    assert convert.rgb_to_cmyk(RGB_MAGENTA) == CMYK_MAGENTA
    assert convert.rgb_to_cmyk(RGB_YELLOW) == CMYK_YELLOW

    assert convert.rgb_to_cmyk(*RGB_WHITE) == CMYK_WHITE
    assert convert.rgb_to_cmyk(255, 255, 255) == CMYK_WHITE
    assert convert.rgb_to_cmyk((255, 255, 255)) == CMYK_WHITE
    assert convert.rgb_to_cmyk([255, 255, 255]) == CMYK_WHITE


def test_rgb_to_hex():
    assert convert.rgb_to_hex(RGB_WHITE) == HEX_WHITE
    assert convert.rgb_to_hex(RGB_GRAY) == HEX_GRAY
    assert convert.rgb_to_hex(RGB_BLACK) == HEX_BLACK
    assert convert.rgb_to_hex(RGB_RED) == HEX_RED
    assert convert.rgb_to_hex(RGB_GREEN) == HEX_GREEN
    assert convert.rgb_to_hex(RGB_BLUE) == HEX_BLUE
    assert convert.rgb_to_hex(RGB_CYAN) == HEX_CYAN
    assert convert.rgb_to_hex(RGB_MAGENTA) == HEX_MAGENTA
    assert convert.rgb_to_hex(RGB_YELLOW) == HEX_YELLOW

    assert convert.rgb_to_hex(*RGB_WHITE) == HEX_WHITE
    assert convert.rgb_to_hex(255, 255, 255) == HEX_WHITE
    assert convert.rgb_to_hex((255, 255, 255)) == HEX_WHITE
    assert convert.rgb_to_hex([255, 255, 255]) == HEX_WHITE


def test_rgb_to_hls():
    assert convert.rgb_to_hls(RGB_WHITE) == HLS_WHITE
    assert convert.rgb_to_hls(RGB_GRAY) == HLS_GRAY
    assert convert.rgb_to_hls(RGB_BLACK) == HLS_BLACK
    assert convert.rgb_to_hls(RGB_RED) == HLS_RED
    assert convert.rgb_to_hls(RGB_GREEN) == HLS_GREEN
    assert convert.rgb_to_hls(RGB_BLUE) == HLS_BLUE
    assert convert.rgb_to_hls(RGB_CYAN) == HLS_CYAN
    assert convert.rgb_to_hls(RGB_MAGENTA) == HLS_MAGENTA
    assert convert.rgb_to_hls(RGB_YELLOW) == HLS_YELLOW

    assert convert.rgb_to_hls(*RGB_WHITE) == HLS_WHITE
    assert convert.rgb_to_hls(255, 255, 255) == HLS_WHITE
    assert convert.rgb_to_hls((255, 255, 255)) == HLS_WHITE
    assert convert.rgb_to_hls([255, 255, 255]) == HLS_WHITE


def test_rgb_to_hsv():
    assert convert.rgb_to_hsv(RGB_WHITE) == HSV_WHITE
    assert convert.rgb_to_hsv(RGB_GRAY) == HSV_GRAY
    assert convert.rgb_to_hsv(RGB_BLACK) == HSV_BLACK
    assert convert.rgb_to_hsv(RGB_RED) == HSV_RED
    assert convert.rgb_to_hsv(RGB_GREEN) == HSV_GREEN
    assert convert.rgb_to_hsv(RGB_BLUE) == HSV_BLUE
    assert convert.rgb_to_hsv(RGB_CYAN) == HSV_CYAN
    assert convert.rgb_to_hsv(RGB_MAGENTA) == HSV_MAGENTA
    assert convert.rgb_to_hsv(RGB_YELLOW) == HSV_YELLOW

    assert convert.rgb_to_hsv(*RGB_WHITE) == HSV_WHITE
    assert convert.rgb_to_hsv(255, 255, 255) == HSV_WHITE
    assert convert.rgb_to_hsv((255, 255, 255)) == HSV_WHITE
    assert convert.rgb_to_hsv([255, 255, 255]) == HSV_WHITE
