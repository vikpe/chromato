from chromato import classes, operations

COLOR_WHITE = classes.Color(255, 255, 255)
COLOR_GRAY = classes.Color(127.5, 127.5, 127.5)
COLOR_BLACK = classes.Color(0, 0, 0)
COLOR_RED = classes.Color(255, 0, 0)
COLOR_BLUE = classes.Color(0, 0, 255)


def test_blend():
    assert operations.blend(COLOR_WHITE, COLOR_BLACK, 0) == COLOR_WHITE
    assert operations.blend(COLOR_WHITE, COLOR_BLACK, 0.5) == COLOR_GRAY
    assert operations.blend(COLOR_WHITE, COLOR_BLACK, 1) == COLOR_BLACK
    assert operations.blend(COLOR_RED, COLOR_BLACK, 0.5) == classes.Color(127.5, 0, 0)
    assert operations.blend(COLOR_RED, COLOR_BLUE) == classes.Color(127.5, 0, 127.5)


def test_shade():
    assert operations.shade(COLOR_WHITE, 0.5) == COLOR_GRAY
    assert operations.shade(COLOR_RED, 0.5) == classes.Color(127.5, 0, 0)
    assert operations.shade(COLOR_RED, 1) == COLOR_BLACK


def test_tint():
    assert operations.tint(COLOR_BLACK, 0.5) == COLOR_GRAY
    assert operations.tint(COLOR_RED, 0.5) == classes.Color(255, 127.5, 127.5)
    assert operations.tint(COLOR_RED, 1) == COLOR_WHITE


def test_tone():
    assert operations.tone(COLOR_RED, 1) == COLOR_GRAY
    assert operations.tone(COLOR_RED, 0.5) == classes.Color(191.25, 63.75, 63.75)
    assert operations.tone(COLOR_WHITE, 1) == COLOR_GRAY
    assert operations.tone(COLOR_WHITE, 0.5) == classes.Color(191.25, 191.25, 191.25)
    assert operations.tone(COLOR_BLACK, 0.5) == classes.Color(63.75, 63.75, 63.75)
    assert operations.tone(COLOR_BLACK, 1) == COLOR_GRAY


def test_grayscale():
    assert operations.grayscale(COLOR_WHITE) == COLOR_WHITE
    assert operations.grayscale(COLOR_GRAY) == COLOR_GRAY
    assert operations.grayscale(COLOR_BLACK) == COLOR_BLACK
    assert operations.grayscale(COLOR_RED) == classes.Color(76.245, 76.245, 76.245)
    assert operations.grayscale(COLOR_BLUE) == classes.Color(29.07, 29.07, 29.07)


def test_invert():
    assert operations.invert(COLOR_WHITE) == COLOR_BLACK
    assert operations.invert(COLOR_GRAY) == COLOR_GRAY
    assert operations.invert(COLOR_BLACK) == COLOR_WHITE
    assert operations.invert(COLOR_RED) == classes.Color(0, 255, 255)
    assert operations.invert(COLOR_BLUE) == classes.Color(255, 255, 0)
    assert operations.invert(classes.Color("ff6699")) == classes.Color(0, 153, 102)


def test_complement():
    assert operations.complement(COLOR_WHITE) == COLOR_WHITE
    assert operations.complement(COLOR_GRAY) == COLOR_GRAY
    assert operations.complement(COLOR_BLACK) == COLOR_BLACK
    assert operations.complement(COLOR_RED) == classes.Color(0, 255, 255)
    assert operations.complement(COLOR_BLUE) == classes.Color(255, 255, 0)
    assert operations.complement(classes.Color("ff6699")) == classes.Color(
        (102, 255, 204)
    )


def test_add():
    assert operations.add(
        classes.Color(255, 0, 0), classes.Color(0, 0, 255)
    ) == classes.Color(255, 0, 255)
    assert operations.add(
        classes.Color(255, 0, 255), classes.Color(0, 0, 255)
    ) == classes.Color(255, 0, 255)
