from chromato import operations as op
from chromato.spaces import Color

WHITE = Color(255, 255, 255)
GRAY = Color(127.5, 127.5, 127.5)
BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
BLUE = Color(0, 0, 255)
GREEN = Color(0, 255, 0)
CYAN = Color(0, 255, 255)
MAGENTA = Color(255, 0, 255)
YELLOW = Color(255, 255, 0)


def test_blend():
    assert op.blend(WHITE, BLACK, 0) == WHITE
    assert op.blend(WHITE, BLACK, 0.5) == GRAY
    assert op.blend(WHITE, BLACK, 1) == BLACK
    assert op.blend(RED, BLACK, 0.5) == Color(127.5, 0, 0)
    assert op.blend(RED, BLUE) == Color(127.5, 0, 127.5)


def test_shade():
    assert op.shade(WHITE, 0.5) == GRAY
    assert op.shade(RED, 0.5) == Color(127.5, 0, 0)
    assert op.shade(RED, 1) == BLACK


def test_tint():
    assert op.tint(BLACK, 0.5) == GRAY
    assert op.tint(RED, 0.5) == Color(255, 127.5, 127.5)
    assert op.tint(RED, 1) == WHITE


def test_tone():
    assert op.tone(RED, 1) == GRAY
    assert op.tone(RED, 0.5) == Color(191.25, 63.75, 63.75)
    assert op.tone(WHITE, 1) == GRAY
    assert op.tone(WHITE, 0.5) == Color(191.25, 191.25, 191.25)
    assert op.tone(BLACK, 0.5) == Color(63.75, 63.75, 63.75)
    assert op.tone(BLACK, 1) == GRAY


def test_grayscale():
    assert op.grayscale(WHITE) == WHITE
    assert op.grayscale(GRAY) == GRAY
    assert op.grayscale(BLACK) == BLACK
    assert op.grayscale(RED) == Color(76.24499999999999, 76.24499999999999, 76.24499999999999)
    assert op.grayscale(GREEN) == Color(149.685, 149.685, 149.685)
    assert op.grayscale(BLUE) == Color(29.07, 29.07, 29.07)
    assert op.grayscale(CYAN) == Color(178.755, 178.755, 178.755)
    assert op.grayscale(MAGENTA) == Color(105.315, 105.315, 105.315)
    assert op.grayscale(YELLOW) == Color(225.93, 225.93, 225.93)


def test_invert():
    assert op.invert(Color("ff6699")) == Color(0, 153, 102)

    assert op.invert(WHITE) == BLACK
    assert op.invert(GRAY) == GRAY
    assert op.invert(BLACK) == WHITE
    assert op.invert(RED) == CYAN
    assert op.invert(BLUE) == YELLOW
    assert op.invert(GREEN) == MAGENTA
    assert op.invert(CYAN) == RED
    assert op.invert(YELLOW) == BLUE
    assert op.invert(MAGENTA) == GREEN


def test_complement():
    assert op.complement(Color("ff6699")) == Color((102, 255, 204))

    assert op.complement(WHITE) == WHITE
    assert op.complement(GRAY) == GRAY
    assert op.complement(BLACK) == BLACK
    assert op.complement(RED) == CYAN
    assert op.complement(BLUE) == YELLOW
    assert op.complement(GREEN) == MAGENTA
    assert op.complement(CYAN) == RED
    assert op.complement(YELLOW) == BLUE
    assert op.complement(MAGENTA) == GREEN


def test_add():
    assert op.add(RED, BLUE) == MAGENTA
    assert op.add(MAGENTA, BLUE) == MAGENTA


def test_subtract():
    assert op.subtract(RED, BLUE) == RED
    assert op.subtract(MAGENTA, BLUE) == RED
