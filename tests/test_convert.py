from chromato import convert, spaces

# Constants
CMYK_WHITE = (0, 0, 0, 0)
CMYK_GRAY = (0, 0, 0, 49.80392156862745)
CMYK_BLACK = (0, 0, 0, 100)
CMYK_RED = (0, 100, 100, 0)
CMYK_GREEN = (100, 0, 100, 0)
CMYK_BLUE = (100, 100, 0, 0)
CMYK_CYAN = (100, 0, 0, 0)
CMYK_MAGENTA = (0, 100, 0, 0)
CMYK_YELLOW = (0, 0, 100, 0)

HEX_WHITE = "ffffff"
HEX_GRAY = "808080"
HEX_BLACK = "000000"
HEX_RED = "ff0000"
HEX_GREEN = "00ff00"
HEX_BLUE = "0000ff"
HEX_CYAN = "00ffff"
HEX_MAGENTA = "ff00ff"
HEX_YELLOW = "ffff00"

HSL_WHITE = (0, 0, 1)
HSL_GRAY = (0, 0, 0.5019607843137255)
HSL_BLACK = (0, 0, 0)
HSL_RED = (0, 1, 0.5)
HSL_GREEN = (1 / 3, 1, 0.5)
HSL_BLUE = (2 / 3, 1, 0.5)
HSL_CYAN = (1 / 2, 1, 0.5)
HSL_MAGENTA = (5 / 6, 1, 0.5)
HSL_YELLOW = (1 / 6, 1, 0.5)

HSV_WHITE = (0, 0, 1)
HSV_GRAY = (0, 0, 0.5019607843137255)
HSV_BLACK = (0, 0, 0)
HSV_RED = (0, 1, 1)
HSV_GREEN = (1 / 3, 1, 1)
HSV_BLUE = (2 / 3, 1, 1)
HSV_CYAN = (1 / 2, 1, 1)
HSV_MAGENTA = (5 / 6, 1, 1)
HSV_YELLOW = (1 / 6, 1, 1)


RGB_WHITE = (255, 255, 255)
RGB_GRAY = (128, 128, 128)
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


def test_cmyk_to_hsl():
    assert convert.cmyk_to_hsl(CMYK_WHITE) == spaces.HSL(HSL_WHITE)
    assert convert.cmyk_to_hsl(CMYK_GRAY) == spaces.HSL(HSL_GRAY)
    assert convert.cmyk_to_hsl(CMYK_BLACK) == spaces.HSL(HSL_BLACK)
    assert convert.cmyk_to_hsl(CMYK_RED) == spaces.HSL(HSL_RED)
    assert convert.cmyk_to_hsl(CMYK_GREEN) == spaces.HSL(HSL_GREEN)
    assert convert.cmyk_to_hsl(CMYK_BLUE) == spaces.HSL(HSL_BLUE)
    assert convert.cmyk_to_hsl(CMYK_CYAN) == spaces.HSL(HSL_CYAN)
    assert convert.cmyk_to_hsl(CMYK_MAGENTA) == spaces.HSL(HSL_MAGENTA)
    assert convert.cmyk_to_hsl(CMYK_YELLOW) == spaces.HSL(HSL_YELLOW)

    assert convert.cmyk_to_hsl(spaces.CMYK(CMYK_WHITE)) == spaces.HSL(HSL_WHITE)
    assert convert.cmyk_to_hsl(*CMYK_WHITE) == spaces.HSL(HSL_WHITE)
    assert convert.cmyk_to_hsl(0, 0, 0, 0) == spaces.HSL(HSL_WHITE)
    assert convert.cmyk_to_hsl((0, 0, 0, 0)) == spaces.HSL(HSL_WHITE)
    assert convert.cmyk_to_hsl([0, 0, 0, 0]) == spaces.HSL(HSL_WHITE)


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


def test_hex_to_hsl():
    assert convert.hex_to_hsl(HEX_WHITE) == spaces.HSL(HSL_WHITE)
    assert convert.hex_to_hsl(HEX_GRAY) == spaces.HSL(HSL_GRAY)
    assert convert.hex_to_hsl(HEX_BLACK) == spaces.HSL(HSL_BLACK)
    assert convert.hex_to_hsl(HEX_RED) == spaces.HSL(HSL_RED)
    assert convert.hex_to_hsl(HEX_GREEN) == spaces.HSL(HSL_GREEN)
    assert convert.hex_to_hsl(HEX_BLUE) == spaces.HSL(HSL_BLUE)
    assert convert.hex_to_hsl(HEX_CYAN) == spaces.HSL(HSL_CYAN)
    assert convert.hex_to_hsl(HEX_MAGENTA) == spaces.HSL(HSL_MAGENTA)
    assert convert.hex_to_hsl(HEX_YELLOW) == spaces.HSL(HSL_YELLOW)

    assert convert.hex_to_hsl((spaces.HEX("fff"))) == spaces.HSL(HSL_WHITE)
    assert convert.hex_to_hsl("fff") == spaces.HSL(HSL_WHITE)
    assert convert.hex_to_hsl("#fff") == spaces.HSL(HSL_WHITE)
    assert convert.hex_to_hsl("ffffff") == spaces.HSL(HSL_WHITE)
    assert convert.hex_to_hsl("#ffffff") == spaces.HSL(HSL_WHITE)


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


# HSL conversion
def test_hsl_to_rgb():
    assert convert.hsl_to_rgb(HSL_WHITE) == spaces.RGB(RGB_WHITE)
    assert convert.hsl_to_rgb(HSL_GRAY) == spaces.RGB(RGB_GRAY)
    assert convert.hsl_to_rgb(HSL_BLACK) == spaces.RGB(RGB_BLACK)
    assert convert.hsl_to_rgb(HSL_RED) == spaces.RGB(RGB_RED)
    assert convert.hsl_to_rgb(HSL_GREEN) == spaces.RGB(RGB_GREEN)
    assert convert.hsl_to_rgb(HSL_BLUE) == spaces.RGB(RGB_BLUE)
    assert convert.hsl_to_rgb(HSL_CYAN) == spaces.RGB(RGB_CYAN)
    assert convert.hsl_to_rgb(HSL_MAGENTA) == spaces.RGB(RGB_MAGENTA)
    assert convert.hsl_to_rgb(HSL_YELLOW) == spaces.RGB(RGB_YELLOW)

    assert convert.hsl_to_rgb(spaces.HSL(HSL_WHITE)) == spaces.RGB(RGB_WHITE)
    assert convert.hsl_to_rgb(*HSL_WHITE) == spaces.RGB(RGB_WHITE)
    assert convert.hsl_to_rgb(0, 0, 1) == spaces.RGB(RGB_WHITE)
    assert convert.hsl_to_rgb((0, 0, 1)) == spaces.RGB(RGB_WHITE)
    assert convert.hsl_to_rgb([0, 0, 1]) == spaces.RGB(RGB_WHITE)


def test_hsl_to_cmyk():
    assert convert.hsl_to_cmyk(HSL_WHITE) == spaces.CMYK(CMYK_WHITE)
    assert convert.hsl_to_cmyk(HSL_GRAY) == spaces.CMYK(CMYK_GRAY)
    assert convert.hsl_to_cmyk(HSL_BLACK) == spaces.CMYK(CMYK_BLACK)
    assert convert.hsl_to_cmyk(HSL_RED) == spaces.CMYK(CMYK_RED)
    assert convert.hsl_to_cmyk(HSL_GREEN) == spaces.CMYK(CMYK_GREEN)
    assert convert.hsl_to_cmyk(HSL_BLUE) == spaces.CMYK(CMYK_BLUE)
    assert convert.hsl_to_cmyk(HSL_CYAN) == spaces.CMYK(CMYK_CYAN)
    assert convert.hsl_to_cmyk(HSL_MAGENTA) == spaces.CMYK(CMYK_MAGENTA)
    assert convert.hsl_to_cmyk(HSL_YELLOW) == spaces.CMYK(CMYK_YELLOW)

    assert convert.hsl_to_cmyk(spaces.HSL(HSL_WHITE)) == spaces.CMYK(CMYK_WHITE)
    assert convert.hsl_to_cmyk(*HSL_WHITE) == spaces.CMYK(CMYK_WHITE)
    assert convert.hsl_to_cmyk(0, 0, 1) == spaces.CMYK(CMYK_WHITE)
    assert convert.hsl_to_cmyk((0, 0, 1)) == spaces.CMYK(CMYK_WHITE)
    assert convert.hsl_to_cmyk([0, 0, 1]) == spaces.CMYK(CMYK_WHITE)


def test_hsl_to_hex():
    assert convert.hsl_to_hex(HSL_WHITE) == spaces.HEX(HEX_WHITE)
    assert convert.hsl_to_hex(HSL_GRAY) == spaces.HEX(HEX_GRAY)
    assert convert.hsl_to_hex(HSL_BLACK) == spaces.HEX(HEX_BLACK)
    assert convert.hsl_to_hex(HSL_RED) == spaces.HEX(HEX_RED)
    assert convert.hsl_to_hex(HSL_GREEN) == spaces.HEX(HEX_GREEN)
    assert convert.hsl_to_hex(HSL_BLUE) == spaces.HEX(HEX_BLUE)
    assert convert.hsl_to_hex(HSL_CYAN) == spaces.HEX(HEX_CYAN)
    assert convert.hsl_to_hex(HSL_MAGENTA) == spaces.HEX(HEX_MAGENTA)
    assert convert.hsl_to_hex(HSL_YELLOW) == spaces.HEX(HEX_YELLOW)

    assert convert.hsl_to_hex(spaces.HSL(HSL_WHITE)) == spaces.HEX(HEX_WHITE)
    assert convert.hsl_to_hex(*HSL_WHITE) == spaces.HEX(HEX_WHITE)
    assert convert.hsl_to_hex(0, 0, 1) == spaces.HEX(HEX_WHITE)
    assert convert.hsl_to_hex((0, 0, 1)) == spaces.HEX(HEX_WHITE)
    assert convert.hsl_to_hex([0, 0, 1]) == spaces.HEX(HEX_WHITE)


def test_hsl_to_hsv():
    assert convert.hsl_to_hsv(HSL_WHITE) == spaces.HSV(HSV_WHITE)
    assert convert.hsl_to_hsv(HSL_GRAY) == spaces.HSV(HSV_GRAY)
    assert convert.hsl_to_hsv(HSL_BLACK) == spaces.HSV(HSV_BLACK)
    assert convert.hsl_to_hsv(HSL_RED) == spaces.HSV(HSV_RED)
    assert convert.hsl_to_hsv(HSL_GREEN) == spaces.HSV(HSV_GREEN)
    assert convert.hsl_to_hsv(HSL_BLUE) == spaces.HSV(HSV_BLUE)
    assert convert.hsl_to_hsv(HSL_CYAN) == spaces.HSV(HSV_CYAN)
    assert convert.hsl_to_hsv(HSL_MAGENTA) == spaces.HSV(HSV_MAGENTA)
    assert convert.hsl_to_hsv(HSL_YELLOW) == spaces.HSV(HSV_YELLOW)

    assert convert.hsl_to_hsv(spaces.HSL(HSL_WHITE)) == spaces.HSV(HSV_WHITE)
    assert convert.hsl_to_hsv(*HSL_WHITE) == spaces.HSV(HSV_WHITE)
    assert convert.hsl_to_hsv(0, 0, 1) == spaces.HSV(HSV_WHITE)
    assert convert.hsl_to_hsv((0, 0, 1)) == spaces.HSV(HSV_WHITE)
    assert convert.hsl_to_hsv([0, 0, 1]) == spaces.HSV(HSV_WHITE)


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


def test_hsv_to_hsl():
    assert convert.hsv_to_hsl(HSV_WHITE) == spaces.HSL(HSL_WHITE)
    assert convert.hsv_to_hsl(HSV_GRAY) == spaces.HSL(HSL_GRAY)
    assert convert.hsv_to_hsl(HSV_BLACK) == spaces.HSL(HSL_BLACK)
    assert convert.hsv_to_hsl(HSV_RED) == spaces.HSL(HSL_RED)
    assert convert.hsv_to_hsl(HSV_GREEN) == spaces.HSL(HSL_GREEN)
    assert convert.hsv_to_hsl(HSV_BLUE) == spaces.HSL(HSL_BLUE)
    assert convert.hsv_to_hsl(HSV_CYAN) == spaces.HSL(HSL_CYAN)
    assert convert.hsv_to_hsl(HSV_MAGENTA) == spaces.HSL(HSL_MAGENTA)
    assert convert.hsv_to_hsl(HSV_YELLOW) == spaces.HSL(HSL_YELLOW)

    assert convert.hsv_to_hsl(spaces.HSV(HSV_WHITE)) == spaces.HSL(HSL_WHITE)
    assert convert.hsv_to_hsl(*HSV_WHITE) == spaces.HSL(HSL_WHITE)
    assert convert.hsv_to_hsl(0, 0, 1) == spaces.HSL(HSL_WHITE)
    assert convert.hsv_to_hsl((0, 0, 1)) == spaces.HSL(HSL_WHITE)
    assert convert.hsv_to_hsl([0, 0, 1]) == spaces.HSL(HSL_WHITE)


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


def test_rgb_to_hsl():
    assert convert.rgb_to_hsl(RGB_WHITE) == spaces.HSL(HSL_WHITE)
    assert convert.rgb_to_hsl(RGB_GRAY) == spaces.HSL(HSL_GRAY)
    assert convert.rgb_to_hsl(RGB_BLACK) == spaces.HSL(HSL_BLACK)
    assert convert.rgb_to_hsl(RGB_RED) == spaces.HSL(HSL_RED)
    assert convert.rgb_to_hsl(RGB_GREEN) == spaces.HSL(HSL_GREEN)
    assert convert.rgb_to_hsl(RGB_BLUE) == spaces.HSL(HSL_BLUE)
    assert convert.rgb_to_hsl(RGB_CYAN) == spaces.HSL(HSL_CYAN)
    assert convert.rgb_to_hsl(RGB_MAGENTA) == spaces.HSL(HSL_MAGENTA)
    assert convert.rgb_to_hsl(RGB_YELLOW) == spaces.HSL(HSL_YELLOW)

    assert convert.rgb_to_hsl(spaces.RGB(RGB_WHITE)) == spaces.HSL(HSL_WHITE)
    assert convert.rgb_to_hsl(*RGB_WHITE) == spaces.HSL(HSL_WHITE)
    assert convert.rgb_to_hsl(255, 255, 255) == spaces.HSL(HSL_WHITE)
    assert convert.rgb_to_hsl((255, 255, 255)) == spaces.HSL(HSL_WHITE)
    assert convert.rgb_to_hsl([255, 255, 255]) == spaces.HSL(HSL_WHITE)


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
