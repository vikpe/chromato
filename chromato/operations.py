from . import classes, constants, math, spaces


def blend(
    color1: classes.Color, color2: classes.Color, factor: float = 0.5
) -> classes.Color:
    r = math.lerp(color1.rgb.r, color2.rgb.r, factor)
    g = math.lerp(color1.rgb.g, color2.rgb.g, factor)
    b = math.lerp(color1.rgb.b, color2.rgb.b, factor)

    return classes.Color(spaces.RGB(r, g, b))


def shade(color: classes.Color, factor: float) -> classes.Color:
    black = classes.Color(
        spaces.RGB(constants.RGB_MIN, constants.RGB_MIN, constants.RGB_MIN)
    )
    return blend(color, black, factor=factor)


def tone(color: classes.Color, factor: float) -> classes.Color:
    gray = classes.Color(
        spaces.RGB(constants.RGB_MAX / 2, constants.RGB_MAX / 2, constants.RGB_MAX / 2)
    )
    return blend(color, gray, factor=factor)


def tint(color: classes.Color, factor: float) -> classes.Color:
    white = classes.Color(
        spaces.RGB(constants.RGB_MAX, constants.RGB_MAX, constants.RGB_MAX)
    )
    return blend(color, white, factor=factor)


def grayscale(color: classes.Color) -> classes.Color:
    r, g, b = color.rgb
    weighted_average = 0.299 * r + 0.587 * g + 0.114 * b
    return classes.Color(
        spaces.RGB(weighted_average, weighted_average, weighted_average)
    )


def invert(color: classes.Color) -> classes.Color:
    return classes.Color(spaces.RGB(*[constants.RGB_MAX - v for v in color.rgb]))


def complement(color: classes.Color) -> classes.Color:
    k = sum([max(*color.rgb), min(*color.rgb)])
    return classes.Color(spaces.RGB(*[k - v for v in color.rgb]))


def add(a: classes.Color, b: classes.Color) -> classes.Color:
    r_sum = min(constants.RGB_MAX, a.rgb.r + b.rgb.r)
    g_sum = min(constants.RGB_MAX, a.rgb.g + b.rgb.g)
    b_sum = min(constants.RGB_MAX, a.rgb.b + b.rgb.b)
    return classes.Color(spaces.RGB(r_sum, g_sum, b_sum))


def subtract(a: classes.Color, b: classes.Color) -> classes.Color:
    r_sum = max(constants.RGB_MIN, a.rgb.r - b.rgb.r)
    g_sum = max(constants.RGB_MIN, a.rgb.g - b.rgb.g)
    b_sum = max(constants.RGB_MIN, a.rgb.b - b.rgb.b)
    return classes.Color(spaces.RGB(r_sum, g_sum, b_sum))
