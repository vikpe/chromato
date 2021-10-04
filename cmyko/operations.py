from .cmyko import Color
from .constants import RGB_MAX, RGB_MIN
from .math import lerp
from .spaces import RGB


def blend(color1: Color, color2: Color, factor: float = 0.5) -> Color:
    r = lerp(color1.rgb.r, color2.rgb.r, factor)
    g = lerp(color1.rgb.g, color2.rgb.g, factor)
    b = lerp(color1.rgb.b, color2.rgb.b, factor)

    return Color(RGB(r, g, b))


def shade(color: Color, factor: float) -> Color:
    return blend(color, Color(RGB(RGB_MIN, RGB_MIN, RGB_MIN)), factor=factor)


def tone(color: Color, factor: float) -> Color:
    return blend(
        color, Color(RGB(RGB_MAX / 2, RGB_MAX / 2, RGB_MAX / 2)), factor=factor
    )


def tint(color: Color, factor: float) -> Color:
    return blend(color, Color(RGB(RGB_MAX, RGB_MAX, RGB_MAX)), factor=factor)
