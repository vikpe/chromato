from chromato import constants, parse, utils
from chromato.spaces import Color, RGB


def blend(color1, color2, factor: float = 0.5) -> Color:
    r1, g1, b1 = parse.parse_rgb(color1)
    r2, g2, b2 = parse.parse_rgb(color2)
    r_blend = utils.lerp(r1, r2, factor)
    g_blend = utils.lerp(g1, g2, factor)
    b_blend = utils.lerp(b1, b2, factor)
    return Color(RGB(r_blend, g_blend, b_blend))


def shade(color, factor: float) -> Color:
    black = RGB(0, 0, 0)
    return blend(color, black, factor)


def tone(color, factor: float) -> Color:
    gray = RGB(128, 128, 128)
    return blend(color, gray, factor)


def tint(color, factor: float) -> Color:
    white = RGB(255, 255, 255)
    return blend(color, white, factor)


def grayscale(color) -> Color:
    r, g, b = parse.parse_rgb(color)
    weighted_average = 0.299 * r + 0.587 * g + 0.114 * b
    return Color(RGB(weighted_average, weighted_average, weighted_average))


def invert(color) -> Color:
    rgb = parse.parse_rgb(color)
    r_inv, g_inv, b_inv = [constants.RGB_MAX - v for v in rgb]
    return Color(RGB(r_inv, g_inv, b_inv))


def complement(color) -> Color:
    rgb = parse.parse_rgb(color)
    k = sum([max(*rgb), min(*rgb)])
    r_comp, g_comp, b_comp = [k - v for v in rgb]
    return Color(RGB(r_comp, g_comp, b_comp))


def add(color1, color2) -> Color:
    r1, g1, b1 = parse.parse_rgb(color1)
    r2, g2, b2 = parse.parse_rgb(color2)
    r_sum = min(constants.RGB_MAX, r1 + r2)
    g_sum = min(constants.RGB_MAX, g1 + g2)
    b_sum = min(constants.RGB_MAX, b1 + b2)
    return Color(RGB(r_sum, g_sum, b_sum))


def subtract(color1, color2) -> Color:
    r1, g1, b1 = parse.parse_rgb(color1)
    r2, g2, b2 = parse.parse_rgb(color2)
    r_diff = max(constants.RGB_MIN, r1 - r2)
    g_diff = max(constants.RGB_MIN, g1 - g2)
    b_diff = max(constants.RGB_MIN, b1 - b2)
    return Color(RGB(r_diff, g_diff, b_diff))


def multiply(color1, color2) -> Color:
    r1, g1, b1 = parse.parse_rgb(color1)
    r2, g2, b2 = parse.parse_rgb(color2)
    r_mult = r1 * r2 / constants.RGB_MAX
    g_mult = g1 * g2 / constants.RGB_MAX
    b_mult = b1 * b2 / constants.RGB_MAX
    return Color(RGB(r_mult, g_mult, b_mult))
