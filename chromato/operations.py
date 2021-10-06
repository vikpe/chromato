from . import constants, math
from .spaces import Color, RGB


def blend(color1: Color, color2: Color, factor: float = 0.5) -> Color:
    r = math.lerp(color1.rgb.r, color2.rgb.r, factor)
    g = math.lerp(color1.rgb.g, color2.rgb.g, factor)
    b = math.lerp(color1.rgb.b, color2.rgb.b, factor)

    return Color(RGB(r, g, b))


def shade(color: Color, factor: float) -> Color:
    return blend(color, Color(0, 0, 0), factor=factor)


def tone(color: Color, factor: float) -> Color:
    return blend(color, Color(3 * [255 / 2]), factor=factor)


def tint(color: Color, factor: float) -> Color:
    return blend(color, Color(255, 255, 255), factor=factor)


def grayscale(color: Color) -> Color:
    r, g, b = color.rgb
    weighted_average = 0.299 * r + 0.587 * g + 0.114 * b
    return Color(RGB(weighted_average, weighted_average, weighted_average))


def invert(color: Color) -> Color:
    return Color(RGB(*[constants.RGB_MAX - v for v in color.rgb]))


def complement(color: Color) -> Color:
    k = sum([max(*color.rgb), min(*color.rgb)])
    return Color(RGB(*[k - v for v in color.rgb]))


def add(color1: Color, color2: Color) -> Color:
    r = min(constants.RGB_MAX, color1.rgb.r + color2.rgb.r)
    g = min(constants.RGB_MAX, color1.rgb.g + color2.rgb.g)
    b = min(constants.RGB_MAX, color1.rgb.b + color2.rgb.b)
    return Color(RGB(r, g, b))


def subtract(a: Color, b: Color) -> Color:
    r = max(constants.RGB_MIN, a.rgb.r - b.rgb.r)
    g = max(constants.RGB_MIN, a.rgb.g - b.rgb.g)
    b = max(constants.RGB_MIN, a.rgb.b - b.rgb.b)
    return Color(RGB(r, g, b))
