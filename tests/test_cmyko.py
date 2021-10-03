from cmyko import cmyko, math

# contants
RGB_WHITE = cmyko.RGB(255, 255, 255)
RGB_GRAY = cmyko.RGB(127, 127, 127)
RGB_BLACK = cmyko.RGB(0, 0, 0)
RGB_RED = cmyko.RGB(255, 0, 0)
RGB_GREEN = cmyko.RGB(0, 255, 0)
RGB_BLUE = cmyko.RGB(0, 0, 255)

HEX_WHITE = "ffffff"
HEX_GRAY = "7f7f7f"
HEX_BLACK = "000000"
HEX_RED = "ff0000"
HEX_GREEN = "00ff00"
HEX_BLUE = "0000ff"

CMYK_WHITE = cmyko.CMYK(0, 0, 0, 0)
CMYK_GRAY = cmyko.CMYK(0, 0, 0, 50.19607843137255)
CMYK_BLACK = cmyko.CMYK(0, 0, 0, 100)
CMYK_RED = cmyko.CMYK(0, 100, 100, 0)
CMYK_GREEN = cmyko.CMYK(100, 0, 100, 0)
CMYK_BLUE = cmyko.CMYK(100, 100, 0, 0)

COLOR_WHITE = cmyko.Color(RGB_WHITE)
COLOR_GRAY = cmyko.Color(RGB_GRAY)
COLOR_BLACK = cmyko.Color(RGB_BLACK)
COLOR_RED = cmyko.Color(RGB_RED)
COLOR_GREEN = cmyko.Color(RGB_GREEN)
COLOR_BLUE = cmyko.Color(RGB_BLUE)


# classes
def test_color():
    color = cmyko.Color(RGB_RED)
    assert color == cmyko.Color.from_hex(HEX_RED)
    assert color.rgb == RGB_RED
    assert color.hex == HEX_RED
    assert color.cmyk == CMYK_RED
    assert color.hls == cmyko.HLS(0, 127.5, -1.007905138339921)
    assert color.hsv == cmyko.HSV(0, 1, 255)
    assert color.yiq == cmyko.YIQ(76.5, 152.745, 54.315)


# parse
def test_parse_hex():
    assert cmyko.parse_hex("ff00ff") == "ff00ff"
    assert cmyko.parse_hex("#ff00ff") == "ff00ff"
    assert cmyko.parse_hex("f0f") == "ff00ff"
    assert cmyko.parse_hex("#f0f") == "ff00ff"


# conversion
def test_hex_to_rgb():
    assert cmyko.hex_to_rgb(HEX_WHITE) == RGB_WHITE
    assert cmyko.hex_to_rgb(HEX_GRAY) == RGB_GRAY
    assert cmyko.hex_to_rgb(HEX_BLACK) == RGB_BLACK
    assert cmyko.hex_to_rgb(HEX_RED) == RGB_RED
    assert cmyko.hex_to_rgb(HEX_GREEN) == RGB_GREEN
    assert cmyko.hex_to_rgb(HEX_BLUE) == RGB_BLUE


def test_rgb_to_hex():
    assert cmyko.rgb_to_hex(RGB_WHITE) == HEX_WHITE
    assert cmyko.rgb_to_hex(RGB_GRAY) == HEX_GRAY
    assert cmyko.rgb_to_hex(RGB_BLACK) == HEX_BLACK
    assert cmyko.rgb_to_hex(RGB_RED) == HEX_RED
    assert cmyko.rgb_to_hex(RGB_GREEN) == HEX_GREEN
    assert cmyko.rgb_to_hex(RGB_BLUE) == HEX_BLUE


def test_rgb_to_cmyk():
    assert cmyko.rgb_to_cmyk(RGB_WHITE) == CMYK_WHITE
    assert cmyko.rgb_to_cmyk(RGB_GRAY) == CMYK_GRAY
    assert cmyko.rgb_to_cmyk(RGB_BLACK) == CMYK_BLACK
    assert cmyko.rgb_to_cmyk(RGB_RED) == CMYK_RED
    assert cmyko.rgb_to_cmyk(RGB_GREEN) == CMYK_GREEN
    assert cmyko.rgb_to_cmyk(RGB_BLUE) == CMYK_BLUE


def test_cmyk_to_rgb():
    assert cmyko.cmyk_to_rgb(CMYK_WHITE) == RGB_WHITE
    assert cmyko.cmyk_to_rgb(CMYK_GRAY) == RGB_GRAY
    assert cmyko.cmyk_to_rgb(CMYK_BLACK) == RGB_BLACK
    assert cmyko.cmyk_to_rgb(CMYK_RED) == RGB_RED
    assert cmyko.cmyk_to_rgb(CMYK_GREEN) == RGB_GREEN
    assert cmyko.cmyk_to_rgb(CMYK_BLUE) == RGB_BLUE


# operations
def test_lerp():
    assert math.lerp(10, 0, 0) == 10
    assert math.lerp(0, 10, 0.5) == 5
    assert math.lerp(10, 1, 0.5) == 5.5
    assert math.lerp(1, 2, 0.5) == 1.5
    assert math.lerp(1, 2, 1) == 2


def test_blend():
    assert cmyko.blend(COLOR_WHITE, COLOR_BLACK, 0) == COLOR_WHITE
    assert cmyko.blend(COLOR_WHITE, COLOR_BLACK, 0.5) == COLOR_GRAY
    assert cmyko.blend(COLOR_WHITE, COLOR_BLACK, 1) == COLOR_BLACK
    assert cmyko.blend(COLOR_RED, COLOR_BLACK, 0.5) == cmyko.Color((127, 0, 0))
    assert cmyko.blend(COLOR_RED, COLOR_BLUE) == cmyko.Color((127, 0, 127))


def test_shade():
    assert cmyko.shade(COLOR_WHITE, 0.5) == COLOR_GRAY
    assert cmyko.shade(COLOR_RED, 0.5) == cmyko.Color((127, 0, 0))
    assert cmyko.shade(COLOR_RED, 1) == COLOR_BLACK


def test_tint():
    assert cmyko.tint(COLOR_BLACK, 0.5) == COLOR_GRAY
    assert cmyko.tint(COLOR_RED, 0.5) == cmyko.Color((255, 127, 127))
    assert cmyko.tint(COLOR_RED, 1) == COLOR_WHITE


def test_tone():
    assert cmyko.tone(COLOR_RED, 1) == COLOR_GRAY
    assert cmyko.tone(COLOR_RED, 0.5) == cmyko.Color((191, 63, 63))
    assert cmyko.tone(COLOR_WHITE, 1) == COLOR_GRAY
    assert cmyko.tone(COLOR_WHITE, 0.5) == cmyko.Color((191, 191, 191))
    assert cmyko.tone(COLOR_BLACK, 0.5) == cmyko.Color((63, 63, 63))
    assert cmyko.tone(COLOR_BLACK, 1) == COLOR_GRAY
