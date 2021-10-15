import colorsys

from chromato import constants, parse, spaces


def cmyk_to_hex(*args) -> spaces.HEX:
    rgb = cmyk_to_rgb(*args)
    return rgb_to_hex(rgb)


def cmyk_to_hsl(*args) -> spaces.HSL:
    rgb = cmyk_to_rgb(*args)
    return rgb_to_hsl(rgb)


def cmyk_to_hsv(*args) -> spaces.HSV:
    rgb = cmyk_to_rgb(*args)
    return rgb_to_hsv(rgb)


def cmyk_to_rgb(*args) -> spaces.RGB:
    c, m, y, k = parse.parse_cmyk(*args)
    r = constants.RGB_MAX * (1.0 - (c + k) / constants.CMYK_MAX)
    g = constants.RGB_MAX * (1.0 - (m + k) / constants.CMYK_MAX)
    b = constants.RGB_MAX * (1.0 - (y + k) / constants.CMYK_MAX)
    return spaces.RGB(r, g, b)


def float_to_hex(_float: float) -> str:
    template = "{:02x}" if _float < 16 else "{:x}"
    return template.format(int(_float))


def hex_to_int(_hex: str) -> int:
    return int(_hex, 16)


def hex_to_cmyk(_hex) -> spaces.CMYK:
    rgb = hex_to_rgb(_hex)
    return rgb_to_cmyk(rgb)


def hex_to_hsl(_hex) -> spaces.HSL:
    rgb = hex_to_rgb(_hex)
    return rgb_to_hsl(rgb)


def hex_to_hsv(_hex) -> spaces.HSV:
    rgb = hex_to_rgb(_hex)
    return rgb_to_hsv(rgb)


def hex_to_rgb(_hex) -> spaces.RGB:
    result = parse.parse_hex(_hex)
    hlen = len(result)
    pairs = hlen // 3
    r, g, b = [hex_to_int(result[i : i + pairs]) for i in range(0, hlen, pairs)]
    return spaces.RGB(r, g, b)


def hsl_to_cmyk(*args) -> spaces.CMYK:
    rgb = hsl_to_rgb(*args)
    return rgb_to_cmyk(rgb)


def hsl_to_hex(*args) -> spaces.HEX:
    rgb = hsl_to_rgb(*args)
    return rgb_to_hex(rgb)


def hsl_to_hsv(*args) -> spaces.HSV:
    rgb = hsl_to_rgb(*args)
    return rgb_to_hsv(rgb)


def hsl_to_rgb(*args) -> spaces.RGB:
    h, s, l = parse.parse_hsl(*args)
    r, g, b = [constants.RGB_MAX * v for v in colorsys.hls_to_rgb(h, l, s)]
    return spaces.RGB(r, g, b)


def hsv_to_cmyk(*args) -> spaces.CMYK:
    rgb = hsv_to_rgb(*args)
    return rgb_to_cmyk(rgb)


def hsv_to_hex(*args) -> spaces.HEX:
    rgb = hsv_to_rgb(*args)
    return rgb_to_hex(rgb)


def hsv_to_hsl(*args) -> spaces.HSL:
    rgb = hsv_to_rgb(*args)
    return rgb_to_hsl(rgb)


def hsv_to_rgb(*args) -> spaces.RGB:
    hsv = parse.parse_hsv(*args)
    r, g, b = [constants.RGB_MAX * v for v in colorsys.hsv_to_rgb(*hsv)]
    return spaces.RGB(r, g, b)


def rgb_to_cmyk(*args) -> spaces.CMYK:
    r, g, b = parse.parse_rgb(*args)

    if (r, g, b) == (constants.RGB_MIN, constants.RGB_MIN, constants.RGB_MIN):
        return spaces.CMYK(
            constants.CMYK_MIN,
            constants.CMYK_MIN,
            constants.CMYK_MIN,
            constants.CMYK_MAX,
        )  # black

    # rgb [0,255] -> cmy [0,1]
    c = 1 - (r / constants.RGB_MAX)
    m = 1 - (g / constants.RGB_MAX)
    y = 1 - (b / constants.RGB_MAX)

    # extract out k [0,1]
    k = min(c, m, y)
    c = c - k
    m = m - k
    y = y - k

    # rescale to the range [0,100]
    c, m, y, k = [v * constants.CMYK_MAX for v in (c, m, y, k)]
    return spaces.CMYK(c, m, y, k)


def rgb_to_hex(*args) -> spaces.HEX:
    parsed_rgb = parse.parse_rgb(*args)
    _hex = "".join(map(float_to_hex, parsed_rgb))
    return spaces.HEX(_hex)


def rgb_to_hsl(*args) -> spaces.HSL:
    rgb = parse.parse_rgb(*args)
    h, l, s = colorsys.rgb_to_hls(*[v / constants.RGB_MAX for v in rgb])
    return spaces.HSL(h, s, l)


def rgb_to_hsv(*args) -> spaces.HSV:
    rgb = parse.parse_rgb(*args)
    h, s, v = colorsys.rgb_to_hsv(*[v / constants.RGB_MAX for v in rgb])
    return spaces.HSV(h, s, v)
