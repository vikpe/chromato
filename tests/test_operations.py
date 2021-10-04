from cmyko import cmyko, operations

COLOR_WHITE = cmyko.Color((255, 255, 255))
COLOR_GRAY = cmyko.Color((127, 127, 127))
COLOR_BLACK = cmyko.Color((0, 0, 0))
COLOR_RED = cmyko.Color((255, 0, 0))
COLOR_BLUE = cmyko.Color((0, 0, 255))


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
