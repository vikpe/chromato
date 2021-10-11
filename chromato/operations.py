from chromato import constants, utils
from chromato.spaces import Color, RGB


def blend(color1: Color, color2: Color, factor: float = 0.5) -> Color:
    r = utils.lerp(color1.rgb.r, color2.rgb.r, factor)
    g = utils.lerp(color1.rgb.g, color2.rgb.g, factor)
    b = utils.lerp(color1.rgb.b, color2.rgb.b, factor)

    return Color(RGB(r, g, b))


def shade(color: Color, factor: float) -> Color:
    black = Color(RGB(0, 0, 0))
    return blend(color, black, factor=factor)


def tone(color: Color, factor: float) -> Color:
    gray = Color(RGB(128, 128, 128))
    return blend(color, gray, factor=factor)


def tint(color: Color, factor: float) -> Color:
    white = Color(RGB(255, 255, 255))
    return blend(color, white, factor=factor)


def grayscale(color: Color) -> Color:
    r, g, b = color.rgb
    weighted_average = 0.299 * r + 0.587 * g + 0.114 * b
    return Color(RGB(weighted_average, weighted_average, weighted_average))


def invert(color: Color) -> Color:
    invert_r, invert_g, invert_b = [constants.RGB_MAX - v for v in color.rgb]
    return Color(RGB(invert_r, invert_g, invert_b))


def complement(color: Color) -> Color:
    k = sum([max(*color.rgb), min(*color.rgb)])
    comp_r, comp_g, comp_b = [k - v for v in color.rgb]
    return Color(RGB(comp_r, comp_g, comp_b))


def add(color1: Color, color2: Color) -> Color:
    r_sum = min(constants.RGB_MAX, color1.rgb.r + color2.rgb.r)
    g_sum = min(constants.RGB_MAX, color1.rgb.g + color2.rgb.g)
    b_sum = min(constants.RGB_MAX, color1.rgb.b + color2.rgb.b)
    return Color(RGB(r_sum, g_sum, b_sum))


def subtract(a: Color, b: Color) -> Color:
    r_diff = max(constants.RGB_MIN, a.rgb.r - b.rgb.r)
    g_diff = max(constants.RGB_MIN, a.rgb.g - b.rgb.g)
    b_diff = max(constants.RGB_MIN, a.rgb.b - b.rgb.b)
    return Color(RGB(r_diff, g_diff, b_diff))
