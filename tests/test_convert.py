from chromato import convert, spaces

# Constants
CMYK_WHITE = (0, 0, 0, 0)
CMYK_GRAY = (0, 0, 0, 50)
CMYK_BLACK = (0, 0, 0, 100)
CMYK_RED = (0, 100, 100, 0)
CMYK_GREEN = (100, 0, 100, 0)
CMYK_BLUE = (100, 100, 0, 0)
CMYK_CYAN = (100, 0, 0, 0)
CMYK_MAGENTA = (0, 100, 0, 0)
CMYK_YELLOW = (0, 0, 100, 0)

HEX_WHITE = "ffffff"
HEX_GRAY = "7f7f7f"
HEX_BLACK = "000000"
HEX_RED = "ff0000"
HEX_GREEN = "00ff00"
HEX_BLUE = "0000ff"
HEX_CYAN = "00ffff"
HEX_MAGENTA = "ff00ff"
HEX_YELLOW = "ffff00"

HLS_WHITE = (0, 1, 0)
HLS_GRAY = (0, 0.5, 0)
HLS_BLACK = (0, 0, 0)
HLS_RED = (0, 0.5, 1)
HLS_GREEN = (1 / 3, 0.5, 1)
HLS_BLUE = (2 / 3, 0.5, 1)
HLS_CYAN = (1 / 2, 0.5, 1)
HLS_MAGENTA = (5 / 6, 0.5, 1)
HLS_YELLOW = (1 / 6, 0.5, 1)

HSV_WHITE = (0, 0, 1)
HSV_GRAY = (0, 0, 0.5)
HSV_BLACK = (0, 0, 0)
HSV_RED = (0, 1, 1)
HSV_GREEN = (1 / 3, 1, 1)
HSV_BLUE = (2 / 3, 1, 1)
HSV_CYAN = (1 / 2, 1, 1)
HSV_MAGENTA = (5 / 6, 1, 1)
HSV_YELLOW = (1 / 6, 1, 1)

RGB_WHITE = (255, 255, 255)
RGB_GRAY = (255 / 2, 255 / 2, 255 / 2)
RGB_BLACK = (0, 0, 0)
RGB_RED = (255, 0, 0)
RGB_GREEN = (0, 255, 0)
RGB_BLUE = (0, 0, 255)
RGB_CYAN = (0, 255, 255)
RGB_MAGENTA = (255, 0, 255)
RGB_YELLOW = (255, 255, 0)


# CMYK conversion
def test_cmyk_to_rgb():
    assert convert.cmyk_to_rgb(CMYK_WHITE) == spaces.RGB(RGB_WHITE)
    assert convert.cmyk_to_rgb(CMYK_GRAY) == spaces.RGB(RGB_GRAY)
    assert convert.cmyk_to_rgb(CMYK_BLACK) == spaces.RGB(RGB_BLACK)
    assert convert.cmyk_to_rgb(CMYK_RED) == spaces.RGB(RGB_RED)
    assert convert.cmyk_to_rgb(CMYK_GREEN) == spaces.RGB(RGB_GREEN)
    assert convert.cmyk_to_rgb(CMYK_BLUE) == spaces.RGB(RGB_BLUE)
    assert convert.cmyk_to_rgb(CMYK_CYAN) == spaces.RGB(RGB_CYAN)
    assert convert.cmyk_to_rgb(CMYK_MAGENTA) == spaces.RGB(RGB_MAGENTA)
    assert convert.cmyk_to_rgb(CMYK_YELLOW) == spaces.RGB(RGB_YELLOW)

    assert convert.cmyk_to_rgb(spaces.CMYK(CMYK_WHITE)) == spaces.RGB(RGB_WHITE)
    assert convert.cmyk_to_rgb(*CMYK_WHITE) == spaces.RGB(RGB_WHITE)
    assert convert.cmyk_to_rgb(0, 0, 0, 0) == spaces.RGB(RGB_WHITE)
    assert convert.cmyk_to_rgb((0, 0, 0, 0)) == spaces.RGB(RGB_WHITE)
    assert convert.cmyk_to_rgb([0, 0, 0, 0]) == spaces.RGB(RGB_WHITE)


def test_cmyk_to_hex():
    assert convert.cmyk_to_hex(CMYK_WHITE) == spaces.HEX(HEX_WHITE)
    assert convert.cmyk_to_hex(CMYK_GRAY) == spaces.HEX(HEX_GRAY)
    assert convert.cmyk_to_hex(CMYK_BLACK) == spaces.HEX(HEX_BLACK)
    assert convert.cmyk_to_hex(CMYK_RED) == spaces.HEX(HEX_RED)
    assert convert.cmyk_to_hex(CMYK_GREEN) == spaces.HEX(HEX_GREEN)
    assert convert.cmyk_to_hex(CMYK_BLUE) == spaces.HEX(HEX_BLUE)
    assert convert.cmyk_to_hex(CMYK_CYAN) == spaces.HEX(HEX_CYAN)
    assert convert.cmyk_to_hex(CMYK_MAGENTA) == spaces.HEX(HEX_MAGENTA)
    assert convert.cmyk_to_hex(CMYK_YELLOW) == spaces.HEX(HEX_YELLOW)

    assert convert.cmyk_to_hex(spaces.CMYK(CMYK_WHITE)) == spaces.HEX(HEX_WHITE)
    assert convert.cmyk_to_hex(*CMYK_WHITE) == spaces.HEX(HEX_WHITE)
    assert convert.cmyk_to_hex(0, 0, 0, 0) == spaces.HEX(HEX_WHITE)
    assert convert.cmyk_to_hex((0, 0, 0, 0)) == spaces.HEX(HEX_WHITE)
    assert convert.cmyk_to_hex([0, 0, 0, 0]) == spaces.HEX(HEX_WHITE)


def test_cmyk_to_hls():
    assert convert.cmyk_to_hls(CMYK_WHITE) == spaces.HLS(HLS_WHITE)
    assert convert.cmyk_to_hls(CMYK_GRAY) == spaces.HLS(HLS_GRAY)
    assert convert.cmyk_to_hls(CMYK_BLACK) == spaces.HLS(HLS_BLACK)
    assert convert.cmyk_to_hls(CMYK_RED) == spaces.HLS(HLS_RED)
    assert convert.cmyk_to_hls(CMYK_GREEN) == spaces.HLS(HLS_GREEN)
    assert convert.cmyk_to_hls(CMYK_BLUE) == spaces.HLS(HLS_BLUE)
    assert convert.cmyk_to_hls(CMYK_CYAN) == spaces.HLS(HLS_CYAN)
    assert convert.cmyk_to_hls(CMYK_MAGENTA) == spaces.HLS(HLS_MAGENTA)
    assert convert.cmyk_to_hls(CMYK_YELLOW) == spaces.HLS(HLS_YELLOW)

    assert convert.cmyk_to_hls(spaces.CMYK(CMYK_WHITE)) == spaces.HLS(HLS_WHITE)
    assert convert.cmyk_to_hls(*CMYK_WHITE) == spaces.HLS(HLS_WHITE)
    assert convert.cmyk_to_hls(0, 0, 0, 0) == spaces.HLS(HLS_WHITE)
    assert convert.cmyk_to_hls((0, 0, 0, 0)) == spaces.HLS(HLS_WHITE)
    assert convert.cmyk_to_hls([0, 0, 0, 0]) == spaces.HLS(HLS_WHITE)


def test_cmyk_to_hsv():
    assert convert.cmyk_to_hsv(CMYK_WHITE) == spaces.HSV(HSV_WHITE)
    assert convert.cmyk_to_hsv(CMYK_GRAY) == spaces.HSV(HSV_GRAY)
    assert convert.cmyk_to_hsv(CMYK_BLACK) == spaces.HSV(HSV_BLACK)
    assert convert.cmyk_to_hsv(CMYK_RED) == spaces.HSV(HSV_RED)
    assert convert.cmyk_to_hsv(CMYK_GREEN) == spaces.HSV(HSV_GREEN)
    assert convert.cmyk_to_hsv(CMYK_BLUE) == spaces.HSV(HSV_BLUE)
    assert convert.cmyk_to_hsv(CMYK_CYAN) == spaces.HSV(HSV_CYAN)
    assert convert.cmyk_to_hsv(CMYK_MAGENTA) == spaces.HSV(HSV_MAGENTA)
    assert convert.cmyk_to_hsv(CMYK_YELLOW) == spaces.HSV(HSV_YELLOW)

    assert convert.cmyk_to_hsv(spaces.CMYK(CMYK_WHITE)) == spaces.HSV(HSV_WHITE)
    assert convert.cmyk_to_hsv(*CMYK_WHITE) == spaces.HSV(HSV_WHITE)
    assert convert.cmyk_to_hsv(0, 0, 0, 0) == spaces.HSV(HSV_WHITE)
    assert convert.cmyk_to_hsv((0, 0, 0, 0)) == spaces.HSV(HSV_WHITE)
    assert convert.cmyk_to_hsv([0, 0, 0, 0]) == spaces.HSV(HSV_WHITE)


# HEX conversion
def test_hex_to_cmyk():
    assert convert.hex_to_cmyk(HEX_WHITE) == spaces.CMYK(CMYK_WHITE)
    assert convert.hex_to_cmyk(HEX_GRAY) == spaces.CMYK(CMYK_GRAY)
    assert convert.hex_to_cmyk(HEX_BLACK) == spaces.CMYK(CMYK_BLACK)
    assert convert.hex_to_cmyk(HEX_RED) == spaces.CMYK(CMYK_RED)
    assert convert.hex_to_cmyk(HEX_GREEN) == spaces.CMYK(CMYK_GREEN)
    assert convert.hex_to_cmyk(HEX_BLUE) == spaces.CMYK(CMYK_BLUE)
    assert convert.hex_to_cmyk(HEX_CYAN) == spaces.CMYK(CMYK_CYAN)
    assert convert.hex_to_cmyk(HEX_MAGENTA) == spaces.CMYK(CMYK_MAGENTA)
    assert convert.hex_to_cmyk(HEX_YELLOW) == spaces.CMYK(CMYK_YELLOW)

    assert convert.hex_to_cmyk(spaces.HEX("fff")) == spaces.CMYK(CMYK_WHITE)
    assert convert.hex_to_cmyk("fff") == spaces.CMYK(CMYK_WHITE)
    assert convert.hex_to_cmyk("#fff") == spaces.CMYK(CMYK_WHITE)
    assert convert.hex_to_cmyk("ffffff") == spaces.CMYK(CMYK_WHITE)
    assert convert.hex_to_cmyk("#ffffff") == spaces.CMYK(CMYK_WHITE)


def test_hex_to_hls():
    assert convert.hex_to_hls(HEX_WHITE) == spaces.HLS(HLS_WHITE)
    assert convert.hex_to_hls(HEX_GRAY) == spaces.HLS(HLS_GRAY)
    assert convert.hex_to_hls(HEX_BLACK) == spaces.HLS(HLS_BLACK)
    assert convert.hex_to_hls(HEX_RED) == spaces.HLS(HLS_RED)
    assert convert.hex_to_hls(HEX_GREEN) == spaces.HLS(HLS_GREEN)
    assert convert.hex_to_hls(HEX_BLUE) == spaces.HLS(HLS_BLUE)
    assert convert.hex_to_hls(HEX_CYAN) == spaces.HLS(HLS_CYAN)
    assert convert.hex_to_hls(HEX_MAGENTA) == spaces.HLS(HLS_MAGENTA)
    assert convert.hex_to_hls(HEX_YELLOW) == spaces.HLS(HLS_YELLOW)

    assert convert.hex_to_hls((spaces.HEX("fff"))) == spaces.HLS(HLS_WHITE)
    assert convert.hex_to_hls("fff") == spaces.HLS(HLS_WHITE)
    assert convert.hex_to_hls("#fff") == spaces.HLS(HLS_WHITE)
    assert convert.hex_to_hls("ffffff") == spaces.HLS(HLS_WHITE)
    assert convert.hex_to_hls("#ffffff") == spaces.HLS(HLS_WHITE)


def test_hex_to_hsv():
    assert convert.hex_to_hsv(HEX_WHITE) == spaces.HSV(HSV_WHITE)
    assert convert.hex_to_hsv(HEX_GRAY) == spaces.HSV(HSV_GRAY)
    assert convert.hex_to_hsv(HEX_BLACK) == spaces.HSV(HSV_BLACK)
    assert convert.hex_to_hsv(HEX_RED) == spaces.HSV(HSV_RED)
    assert convert.hex_to_hsv(HEX_GREEN) == spaces.HSV(HSV_GREEN)
    assert convert.hex_to_hsv(HEX_BLUE) == spaces.HSV(HSV_BLUE)
    assert convert.hex_to_hsv(HEX_CYAN) == spaces.HSV(HSV_CYAN)
    assert convert.hex_to_hsv(HEX_MAGENTA) == spaces.HSV(HSV_MAGENTA)
    assert convert.hex_to_hsv(HEX_YELLOW) == spaces.HSV(HSV_YELLOW)

    assert convert.hex_to_hsv((spaces.HEX("fff"))) == spaces.HSV(HSV_WHITE)
    assert convert.hex_to_hsv("fff") == spaces.HSV(HSV_WHITE)
    assert convert.hex_to_hsv("#fff") == spaces.HSV(HSV_WHITE)
    assert convert.hex_to_hsv("ffffff") == spaces.HSV(HSV_WHITE)
    assert convert.hex_to_hsv("#ffffff") == spaces.HSV(HSV_WHITE)


def test_hex_to_rgb():
    assert convert.hex_to_rgb(HEX_WHITE) == spaces.RGB(RGB_WHITE)
    assert convert.hex_to_rgb(HEX_GRAY) == spaces.RGB(RGB_GRAY)
    assert convert.hex_to_rgb(HEX_BLACK) == spaces.RGB(RGB_BLACK)
    assert convert.hex_to_rgb(HEX_RED) == spaces.RGB(RGB_RED)
    assert convert.hex_to_rgb(HEX_GREEN) == spaces.RGB(RGB_GREEN)
    assert convert.hex_to_rgb(HEX_BLUE) == spaces.RGB(RGB_BLUE)
    assert convert.hex_to_rgb(HEX_CYAN) == spaces.RGB(RGB_CYAN)
    assert convert.hex_to_rgb(HEX_MAGENTA) == spaces.RGB(RGB_MAGENTA)
    assert convert.hex_to_rgb(HEX_YELLOW) == spaces.RGB(RGB_YELLOW)

    assert convert.hex_to_rgb((spaces.HEX("fff"))) == spaces.RGB(RGB_WHITE)
    assert convert.hex_to_rgb("fff") == spaces.RGB(RGB_WHITE)
    assert convert.hex_to_rgb("#fff") == spaces.RGB(RGB_WHITE)
    assert convert.hex_to_rgb("ffffff") == spaces.RGB(RGB_WHITE)
    assert convert.hex_to_rgb("#ffffff") == spaces.RGB(RGB_WHITE)


# HLS conversion
def test_hls_to_rgb():
    assert convert.hls_to_rgb(HLS_WHITE) == spaces.RGB(RGB_WHITE)
    assert convert.hls_to_rgb(HLS_GRAY) == spaces.RGB(RGB_GRAY)
    assert convert.hls_to_rgb(HLS_BLACK) == spaces.RGB(RGB_BLACK)
    assert convert.hls_to_rgb(HLS_RED) == spaces.RGB(RGB_RED)
    assert convert.hls_to_rgb(HLS_GREEN) == spaces.RGB(RGB_GREEN)
    assert convert.hls_to_rgb(HLS_BLUE) == spaces.RGB(RGB_BLUE)
    assert convert.hls_to_rgb(HLS_CYAN) == spaces.RGB(RGB_CYAN)
    assert convert.hls_to_rgb(HLS_MAGENTA) == spaces.RGB(RGB_MAGENTA)
    assert convert.hls_to_rgb(HLS_YELLOW) == spaces.RGB(RGB_YELLOW)

    assert convert.hls_to_rgb(spaces.HLS(HLS_WHITE)) == spaces.RGB(RGB_WHITE)
    assert convert.hls_to_rgb(*HLS_WHITE) == spaces.RGB(RGB_WHITE)
    assert convert.hls_to_rgb(0, 1, 0) == spaces.RGB(RGB_WHITE)
    assert convert.hls_to_rgb((0, 1, 0)) == spaces.RGB(RGB_WHITE)
    assert convert.hls_to_rgb([0, 1, 0]) == spaces.RGB(RGB_WHITE)


def test_hls_to_cmyk():
    assert convert.hls_to_cmyk(HLS_WHITE) == spaces.CMYK(CMYK_WHITE)
    assert convert.hls_to_cmyk(HLS_GRAY) == spaces.CMYK(CMYK_GRAY)
    assert convert.hls_to_cmyk(HLS_BLACK) == spaces.CMYK(CMYK_BLACK)
    assert convert.hls_to_cmyk(HLS_RED) == spaces.CMYK(CMYK_RED)
    assert convert.hls_to_cmyk(HLS_GREEN) == spaces.CMYK(CMYK_GREEN)
    assert convert.hls_to_cmyk(HLS_BLUE) == spaces.CMYK(CMYK_BLUE)
    assert convert.hls_to_cmyk(HLS_CYAN) == spaces.CMYK(CMYK_CYAN)
    assert convert.hls_to_cmyk(HLS_MAGENTA) == spaces.CMYK(CMYK_MAGENTA)
    assert convert.hls_to_cmyk(HLS_YELLOW) == spaces.CMYK(CMYK_YELLOW)

    assert convert.hls_to_cmyk(spaces.HLS(HLS_WHITE)) == spaces.CMYK(CMYK_WHITE)
    assert convert.hls_to_cmyk(*HLS_WHITE) == spaces.CMYK(CMYK_WHITE)
    assert convert.hls_to_cmyk(0, 1, 0) == spaces.CMYK(CMYK_WHITE)
    assert convert.hls_to_cmyk((0, 1, 0)) == spaces.CMYK(CMYK_WHITE)
    assert convert.hls_to_cmyk([0, 1, 0]) == spaces.CMYK(CMYK_WHITE)


def test_hls_to_hex():
    assert convert.hls_to_hex(HLS_WHITE) == spaces.HEX(HEX_WHITE)
    assert convert.hls_to_hex(HLS_GRAY) == spaces.HEX(HEX_GRAY)
    assert convert.hls_to_hex(HLS_BLACK) == spaces.HEX(HEX_BLACK)
    assert convert.hls_to_hex(HLS_RED) == spaces.HEX(HEX_RED)
    assert convert.hls_to_hex(HLS_GREEN) == spaces.HEX(HEX_GREEN)
    assert convert.hls_to_hex(HLS_BLUE) == spaces.HEX(HEX_BLUE)
    assert convert.hls_to_hex(HLS_CYAN) == spaces.HEX(HEX_CYAN)
    assert convert.hls_to_hex(HLS_MAGENTA) == spaces.HEX(HEX_MAGENTA)
    assert convert.hls_to_hex(HLS_YELLOW) == spaces.HEX(HEX_YELLOW)

    assert convert.hls_to_hex(spaces.HLS(HLS_WHITE)) == spaces.HEX(HEX_WHITE)
    assert convert.hls_to_hex(*HLS_WHITE) == spaces.HEX(HEX_WHITE)
    assert convert.hls_to_hex(0, 1, 0) == spaces.HEX(HEX_WHITE)
    assert convert.hls_to_hex((0, 1, 0)) == spaces.HEX(HEX_WHITE)
    assert convert.hls_to_hex([0, 1, 0]) == spaces.HEX(HEX_WHITE)


def test_hls_to_hsv():
    assert convert.hls_to_hsv(HLS_WHITE) == spaces.HSV(HSV_WHITE)
    assert convert.hls_to_hsv(HLS_GRAY) == spaces.HSV(HSV_GRAY)
    assert convert.hls_to_hsv(HLS_BLACK) == spaces.HSV(HSV_BLACK)
    assert convert.hls_to_hsv(HLS_RED) == spaces.HSV(HSV_RED)
    assert convert.hls_to_hsv(HLS_GREEN) == spaces.HSV(HSV_GREEN)
    assert convert.hls_to_hsv(HLS_BLUE) == spaces.HSV(HSV_BLUE)
    assert convert.hls_to_hsv(HLS_CYAN) == spaces.HSV(HSV_CYAN)
    assert convert.hls_to_hsv(HLS_MAGENTA) == spaces.HSV(HSV_MAGENTA)
    assert convert.hls_to_hsv(HLS_YELLOW) == spaces.HSV(HSV_YELLOW)

    assert convert.hls_to_hsv(spaces.HLS(HLS_WHITE)) == spaces.HSV(HSV_WHITE)
    assert convert.hls_to_hsv(*HLS_WHITE) == spaces.HSV(HSV_WHITE)
    assert convert.hls_to_hsv(0, 1, 0) == spaces.HSV(HSV_WHITE)
    assert convert.hls_to_hsv((0, 1, 0)) == spaces.HSV(HSV_WHITE)
    assert convert.hls_to_hsv([0, 1, 0]) == spaces.HSV(HSV_WHITE)


# HSV conversion
def test_hsv_to_cmyk():
    assert convert.hsv_to_cmyk(HSV_WHITE) == spaces.CMYK(CMYK_WHITE)
    assert convert.hsv_to_cmyk(HSV_GRAY) == spaces.CMYK(CMYK_GRAY)
    assert convert.hsv_to_cmyk(HSV_BLACK) == spaces.CMYK(CMYK_BLACK)
    assert convert.hsv_to_cmyk(HSV_RED) == spaces.CMYK(CMYK_RED)
    assert convert.hsv_to_cmyk(HSV_GREEN) == spaces.CMYK(CMYK_GREEN)
    assert convert.hsv_to_cmyk(HSV_BLUE) == spaces.CMYK(CMYK_BLUE)
    assert convert.hsv_to_cmyk(HSV_CYAN) == spaces.CMYK(CMYK_CYAN)
    assert convert.hsv_to_cmyk(HSV_MAGENTA) == spaces.CMYK(CMYK_MAGENTA)
    assert convert.hsv_to_cmyk(HSV_YELLOW) == spaces.CMYK(CMYK_YELLOW)

    assert convert.hsv_to_cmyk(spaces.HSV(HSV_WHITE)) == spaces.CMYK(CMYK_WHITE)
    assert convert.hsv_to_cmyk(*HSV_WHITE) == spaces.CMYK(CMYK_WHITE)
    assert convert.hsv_to_cmyk(0, 0, 1) == spaces.CMYK(CMYK_WHITE)
    assert convert.hsv_to_cmyk((0, 0, 1)) == spaces.CMYK(CMYK_WHITE)
    assert convert.hsv_to_cmyk([0, 0, 1]) == spaces.CMYK(CMYK_WHITE)


def test_hsv_to_hex():
    assert convert.hsv_to_hex(HSV_WHITE) == spaces.HEX(HEX_WHITE)
    assert convert.hsv_to_hex(HSV_GRAY) == spaces.HEX(HEX_GRAY)
    assert convert.hsv_to_hex(HSV_BLACK) == spaces.HEX(HEX_BLACK)
    assert convert.hsv_to_hex(HSV_RED) == spaces.HEX(HEX_RED)
    assert convert.hsv_to_hex(HSV_GREEN) == spaces.HEX(HEX_GREEN)
    assert convert.hsv_to_hex(HSV_BLUE) == spaces.HEX(HEX_BLUE)
    assert convert.hsv_to_hex(HSV_CYAN) == spaces.HEX(HEX_CYAN)
    assert convert.hsv_to_hex(HSV_MAGENTA) == spaces.HEX(HEX_MAGENTA)
    assert convert.hsv_to_hex(HSV_YELLOW) == spaces.HEX(HEX_YELLOW)

    assert convert.hsv_to_hex(spaces.HSV(HSV_WHITE)) == spaces.HEX(HEX_WHITE)
    assert convert.hsv_to_hex(*HSV_WHITE) == spaces.HEX(HEX_WHITE)
    assert convert.hsv_to_hex(0, 0, 1) == spaces.HEX(HEX_WHITE)
    assert convert.hsv_to_hex((0, 0, 1)) == spaces.HEX(HEX_WHITE)
    assert convert.hsv_to_hex([0, 0, 1]) == spaces.HEX(HEX_WHITE)


def test_hsv_to_hls():
    assert convert.hsv_to_hls(HSV_WHITE) == spaces.HLS(HLS_WHITE)
    assert convert.hsv_to_hls(HSV_GRAY) == spaces.HLS(HLS_GRAY)
    assert convert.hsv_to_hls(HSV_BLACK) == spaces.HLS(HLS_BLACK)
    assert convert.hsv_to_hls(HSV_RED) == spaces.HLS(HLS_RED)
    assert convert.hsv_to_hls(HSV_GREEN) == spaces.HLS(HLS_GREEN)
    assert convert.hsv_to_hls(HSV_BLUE) == spaces.HLS(HLS_BLUE)
    assert convert.hsv_to_hls(HSV_CYAN) == spaces.HLS(HLS_CYAN)
    assert convert.hsv_to_hls(HSV_MAGENTA) == spaces.HLS(HLS_MAGENTA)
    assert convert.hsv_to_hls(HSV_YELLOW) == spaces.HLS(HLS_YELLOW)

    assert convert.hsv_to_hls(spaces.HSV(HSV_WHITE)) == spaces.HLS(HLS_WHITE)
    assert convert.hsv_to_hls(*HSV_WHITE) == spaces.HLS(HLS_WHITE)
    assert convert.hsv_to_hls(0, 0, 1) == spaces.HLS(HLS_WHITE)
    assert convert.hsv_to_hls((0, 0, 1)) == spaces.HLS(HLS_WHITE)
    assert convert.hsv_to_hls([0, 0, 1]) == spaces.HLS(HLS_WHITE)


def test_hsv_to_rgb():
    assert convert.hsv_to_rgb(HSV_WHITE) == spaces.RGB(RGB_WHITE)
    assert convert.hsv_to_rgb(HSV_GRAY) == spaces.RGB(RGB_GRAY)
    assert convert.hsv_to_rgb(HSV_BLACK) == spaces.RGB(RGB_BLACK)
    assert convert.hsv_to_rgb(HSV_RED) == spaces.RGB(RGB_RED)
    assert convert.hsv_to_rgb(HSV_GREEN) == spaces.RGB(RGB_GREEN)
    assert convert.hsv_to_rgb(HSV_BLUE) == spaces.RGB(RGB_BLUE)
    assert convert.hsv_to_rgb(HSV_CYAN) == spaces.RGB(RGB_CYAN)
    assert convert.hsv_to_rgb(HSV_MAGENTA) == spaces.RGB(RGB_MAGENTA)
    assert convert.hsv_to_rgb(HSV_YELLOW) == spaces.RGB(RGB_YELLOW)

    assert convert.hsv_to_rgb(spaces.HSV(HSV_WHITE)) == spaces.RGB(RGB_WHITE)
    assert convert.hsv_to_rgb(*HSV_WHITE) == spaces.RGB(RGB_WHITE)
    assert convert.hsv_to_rgb(0, 0, 1) == spaces.RGB(RGB_WHITE)
    assert convert.hsv_to_rgb((0, 0, 1)) == spaces.RGB(RGB_WHITE)
    assert convert.hsv_to_rgb([0, 0, 1]) == spaces.RGB(RGB_WHITE)


# RGB conversion
def test_rgb_to_cmyk():
    assert convert.rgb_to_cmyk(RGB_WHITE) == spaces.CMYK(CMYK_WHITE)
    assert convert.rgb_to_cmyk(RGB_GRAY) == spaces.CMYK(CMYK_GRAY)
    assert convert.rgb_to_cmyk(RGB_BLACK) == spaces.CMYK(CMYK_BLACK)
    assert convert.rgb_to_cmyk(RGB_RED) == spaces.CMYK(CMYK_RED)
    assert convert.rgb_to_cmyk(RGB_GREEN) == spaces.CMYK(CMYK_GREEN)
    assert convert.rgb_to_cmyk(RGB_BLUE) == spaces.CMYK(CMYK_BLUE)
    assert convert.rgb_to_cmyk(RGB_CYAN) == spaces.CMYK(CMYK_CYAN)
    assert convert.rgb_to_cmyk(RGB_MAGENTA) == spaces.CMYK(CMYK_MAGENTA)
    assert convert.rgb_to_cmyk(RGB_YELLOW) == spaces.CMYK(CMYK_YELLOW)

    assert convert.rgb_to_cmyk(spaces.RGB(RGB_WHITE)) == spaces.CMYK(CMYK_WHITE)
    assert convert.rgb_to_cmyk(*RGB_WHITE) == spaces.CMYK(CMYK_WHITE)
    assert convert.rgb_to_cmyk(255, 255, 255) == spaces.CMYK(CMYK_WHITE)
    assert convert.rgb_to_cmyk((255, 255, 255)) == spaces.CMYK(CMYK_WHITE)
    assert convert.rgb_to_cmyk([255, 255, 255]) == spaces.CMYK(CMYK_WHITE)


def test_rgb_to_hex():
    assert convert.rgb_to_hex(RGB_WHITE) == spaces.HEX(HEX_WHITE)
    assert convert.rgb_to_hex(RGB_GRAY) == spaces.HEX(HEX_GRAY)
    assert convert.rgb_to_hex(RGB_BLACK) == spaces.HEX(HEX_BLACK)
    assert convert.rgb_to_hex(RGB_RED) == spaces.HEX(HEX_RED)
    assert convert.rgb_to_hex(RGB_GREEN) == spaces.HEX(HEX_GREEN)
    assert convert.rgb_to_hex(RGB_BLUE) == spaces.HEX(HEX_BLUE)
    assert convert.rgb_to_hex(RGB_CYAN) == spaces.HEX(HEX_CYAN)
    assert convert.rgb_to_hex(RGB_MAGENTA) == spaces.HEX(HEX_MAGENTA)
    assert convert.rgb_to_hex(RGB_YELLOW) == spaces.HEX(HEX_YELLOW)

    assert convert.rgb_to_hex(spaces.RGB(RGB_WHITE)) == spaces.HEX(HEX_WHITE)
    assert convert.rgb_to_hex(*RGB_WHITE) == spaces.HEX(HEX_WHITE)
    assert convert.rgb_to_hex(255, 255, 255) == spaces.HEX(HEX_WHITE)
    assert convert.rgb_to_hex((255, 255, 255)) == spaces.HEX(HEX_WHITE)
    assert convert.rgb_to_hex([255, 255, 255]) == spaces.HEX(HEX_WHITE)


def test_rgb_to_hls():
    assert convert.rgb_to_hls(RGB_WHITE) == spaces.HLS(HLS_WHITE)
    assert convert.rgb_to_hls(RGB_GRAY) == spaces.HLS(HLS_GRAY)
    assert convert.rgb_to_hls(RGB_BLACK) == spaces.HLS(HLS_BLACK)
    assert convert.rgb_to_hls(RGB_RED) == spaces.HLS(HLS_RED)
    assert convert.rgb_to_hls(RGB_GREEN) == spaces.HLS(HLS_GREEN)
    assert convert.rgb_to_hls(RGB_BLUE) == spaces.HLS(HLS_BLUE)
    assert convert.rgb_to_hls(RGB_CYAN) == spaces.HLS(HLS_CYAN)
    assert convert.rgb_to_hls(RGB_MAGENTA) == spaces.HLS(HLS_MAGENTA)
    assert convert.rgb_to_hls(RGB_YELLOW) == spaces.HLS(HLS_YELLOW)

    assert convert.rgb_to_hls(spaces.RGB(RGB_WHITE)) == spaces.HLS(HLS_WHITE)
    assert convert.rgb_to_hls(*RGB_WHITE) == spaces.HLS(HLS_WHITE)
    assert convert.rgb_to_hls(255, 255, 255) == spaces.HLS(HLS_WHITE)
    assert convert.rgb_to_hls((255, 255, 255)) == spaces.HLS(HLS_WHITE)
    assert convert.rgb_to_hls([255, 255, 255]) == spaces.HLS(HLS_WHITE)


def test_rgb_to_hsv():
    assert convert.rgb_to_hsv(RGB_WHITE) == spaces.HSV(HSV_WHITE)
    assert convert.rgb_to_hsv(RGB_GRAY) == spaces.HSV(HSV_GRAY)
    assert convert.rgb_to_hsv(RGB_BLACK) == spaces.HSV(HSV_BLACK)
    assert convert.rgb_to_hsv(RGB_RED) == spaces.HSV(HSV_RED)
    assert convert.rgb_to_hsv(RGB_GREEN) == spaces.HSV(HSV_GREEN)
    assert convert.rgb_to_hsv(RGB_BLUE) == spaces.HSV(HSV_BLUE)
    assert convert.rgb_to_hsv(RGB_CYAN) == spaces.HSV(HSV_CYAN)
    assert convert.rgb_to_hsv(RGB_MAGENTA) == spaces.HSV(HSV_MAGENTA)
    assert convert.rgb_to_hsv(RGB_YELLOW) == spaces.HSV(HSV_YELLOW)

    assert convert.rgb_to_hsv(spaces.RGB(RGB_WHITE)) == spaces.HSV(HSV_WHITE)
    assert convert.rgb_to_hsv(*RGB_WHITE) == spaces.HSV(HSV_WHITE)
    assert convert.rgb_to_hsv(255, 255, 255) == spaces.HSV(HSV_WHITE)
    assert convert.rgb_to_hsv((255, 255, 255)) == spaces.HSV(HSV_WHITE)
    assert convert.rgb_to_hsv([255, 255, 255]) == spaces.HSV(HSV_WHITE)
