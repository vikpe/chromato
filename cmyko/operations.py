from . import cmyko, constants, math, spaces


def blend(color1: cmyko.Color, color2: cmyko.Color, factor: float = 0.5) -> cmyko.Color:
    r = math.lerp(color1.rgb.r, color2.rgb.r, factor)
    g = math.lerp(color1.rgb.g, color2.rgb.g, factor)
    b = math.lerp(color1.rgb.b, color2.rgb.b, factor)

    return cmyko.Color(spaces.RGB(r, g, b))


def shade(color: cmyko.Color, factor: float) -> cmyko.Color:
    black = cmyko.Color(
        spaces.RGB(constants.RGB_MIN, constants.RGB_MIN, constants.RGB_MIN)
    )
    return blend(color, black, factor=factor)


def tone(color: cmyko.Color, factor: float) -> cmyko.Color:
    gray = cmyko.Color(
        spaces.RGB(constants.RGB_MAX / 2, constants.RGB_MAX / 2, constants.RGB_MAX / 2)
    )
    return blend(color, gray, factor=factor)


def tint(color: cmyko.Color, factor: float) -> cmyko.Color:
    white = cmyko.Color(
        spaces.RGB(constants.RGB_MAX, constants.RGB_MAX, constants.RGB_MAX)
    )
    return blend(color, white, factor=factor)


def grayscale(color: cmyko.Color) -> cmyko.Color:
    r, g, b = color.rgb
    weighted_average = 0.299 * r + 0.587 * g + 0.114 * b
    return cmyko.Color(spaces.RGB(weighted_average, weighted_average, weighted_average))


def invert(color: cmyko.Color) -> cmyko.Color:
    return cmyko.Color([constants.RGB_MAX - v for v in color.rgb])


def complement(color: cmyko.Color) -> cmyko.Color:
    k = sum([max(*color.rgb), min(*color.rgb)])
    return cmyko.Color([k - v for v in color.rgb])
