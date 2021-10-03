from cmyko import cmyko, operations, spaces

# contants
RGB_WHITE = spaces.RGB(255, 255, 255)
RGB_GRAY = spaces.RGB(127, 127, 127)
RGB_BLACK = spaces.RGB(0, 0, 0)
RGB_RED = spaces.RGB(255, 0, 0)
RGB_GREEN = spaces.RGB(0, 255, 0)
RGB_BLUE = spaces.RGB(0, 0, 255)

HEX_WHITE = "ffffff"
HEX_GRAY = "7f7f7f"
HEX_BLACK = "000000"
HEX_RED = "ff0000"
HEX_GREEN = "00ff00"
HEX_BLUE = "0000ff"

CMYK_WHITE = spaces.CMYK(0, 0, 0, 0)
CMYK_GRAY = spaces.CMYK(0, 0, 0, 50.19607843137255)
CMYK_BLACK = spaces.CMYK(0, 0, 0, 100)
CMYK_RED = spaces.CMYK(0, 100, 100, 0)
CMYK_GREEN = spaces.CMYK(100, 0, 100, 0)
CMYK_BLUE = spaces.CMYK(100, 100, 0, 0)

COLOR_WHITE = cmyko.Color(RGB_WHITE)
COLOR_GRAY = cmyko.Color(RGB_GRAY)
COLOR_BLACK = cmyko.Color(RGB_BLACK)
COLOR_RED = cmyko.Color(RGB_RED)
COLOR_GREEN = cmyko.Color(RGB_GREEN)
COLOR_BLUE = cmyko.Color(RGB_BLUE)


def test_blend():
    assert operations.blend(COLOR_WHITE, COLOR_BLACK, 0) == COLOR_WHITE
    assert operations.blend(COLOR_WHITE, COLOR_BLACK, 0.5) == COLOR_GRAY
    assert operations.blend(COLOR_WHITE, COLOR_BLACK, 1) == COLOR_BLACK
    assert operations.blend(COLOR_RED, COLOR_BLACK, 0.5) == cmyko.Color((127, 0, 0))
    assert operations.blend(COLOR_RED, COLOR_BLUE) == cmyko.Color((127, 0, 127))


def test_shade():
    assert operations.shade(COLOR_WHITE, 0.5) == COLOR_GRAY
    assert operations.shade(COLOR_RED, 0.5) == cmyko.Color((127, 0, 0))
    assert operations.shade(COLOR_RED, 1) == COLOR_BLACK


def test_tint():
    assert operations.tint(COLOR_BLACK, 0.5) == COLOR_GRAY
    assert operations.tint(COLOR_RED, 0.5) == cmyko.Color((255, 127, 127))
    assert operations.tint(COLOR_RED, 1) == COLOR_WHITE


def test_tone():
    assert operations.tone(COLOR_RED, 1) == COLOR_GRAY
    assert operations.tone(COLOR_RED, 0.5) == cmyko.Color((191, 63, 63))
    assert operations.tone(COLOR_WHITE, 1) == COLOR_GRAY
    assert operations.tone(COLOR_WHITE, 0.5) == cmyko.Color((191, 191, 191))
    assert operations.tone(COLOR_BLACK, 0.5) == cmyko.Color((63, 63, 63))
    assert operations.tone(COLOR_BLACK, 1) == COLOR_GRAY
