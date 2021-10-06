import colorsys

from . import constants, parse
from .spaces import CMYK, HEX, HLS, HSV, RGB


def cmyk_to_hex(*args) -> HEX:
    rgb = cmyk_to_rgb(*args)
    return rgb_to_hex(rgb)


def cmyk_to_hls(*args) -> HLS:
    rgb = cmyk_to_rgb(*args)
    return rgb_to_hls(rgb)


def cmyk_to_hsv(*args) -> HSV:
    rgb = cmyk_to_rgb(*args)
    return rgb_to_hsv(rgb)


def cmyk_to_rgb(*args) -> RGB:
    c, m, y, k = parse.parse_cmyk(*args)
    r = constants.RGB_MAX * (1.0 - (c + k) / constants.CMYK_MAX)
    g = constants.RGB_MAX * (1.0 - (m + k) / constants.CMYK_MAX)
    b = constants.RGB_MAX * (1.0 - (y + k) / constants.CMYK_MAX)
    return RGB(r, g, b)


def float_to_hex(_float: float) -> str:
    template = "{:02x}" if _float < 16 else "{:x}"
    return template.format(int(_float))


def hex_to_int(_hex: str) -> int:
    return int(_hex, 16)


def hex_to_cmyk(_hex) -> CMYK:
    rgb = hex_to_rgb(_hex)
    return rgb_to_cmyk(rgb)


def hex_to_hls(_hex) -> HLS:
    rgb = hex_to_rgb(_hex)
    return rgb_to_hls(rgb)


def hex_to_hsv(_hex) -> HSV:
    rgb = hex_to_rgb(_hex)
    return rgb_to_hsv(rgb)


def hex_to_rgb(_hex) -> RGB:
    result = parse.parse_hex(_hex)
    hlen = len(result)
    pairs = hlen // 3
    r, g, b = [hex_to_int(result[i : i + pairs]) for i in range(0, hlen, pairs)]
    return RGB(r, g, b)


def hls_to_cmyk(*args) -> CMYK:
    rgb = hls_to_rgb(*args)
    return rgb_to_cmyk(rgb)


def hls_to_hex(*args) -> HEX:
    rgb = hls_to_rgb(*args)
    return rgb_to_hex(rgb)


def hls_to_hsv(*args) -> HSV:
    rgb = hls_to_rgb(*args)
    return rgb_to_hsv(rgb)


def hls_to_rgb(*args) -> RGB:
    hls = parse.parse_hls(*args)
    return RGB(*[constants.RGB_MAX * v for v in colorsys.hls_to_rgb(*hls)])


def hsv_to_cmyk(*args) -> CMYK:
    rgb = hsv_to_rgb(*args)
    return rgb_to_cmyk(rgb)


def hsv_to_hex(*args) -> HEX:
    rgb = hsv_to_rgb(*args)
    return rgb_to_hex(rgb)


def hsv_to_hls(*args) -> HLS:
    rgb = hsv_to_rgb(*args)
    return rgb_to_hls(rgb)


def hsv_to_rgb(*args) -> RGB:
    hsv = parse.parse_hsv(*args)
    return RGB(*[constants.RGB_MAX * v for v in colorsys.hsv_to_rgb(*hsv)])


def rgb_to_cmyk(*args) -> CMYK:
    r, g, b = parse.parse(*args)

    if (r, g, b) == (constants.RGB_MIN, constants.RGB_MIN, constants.RGB_MIN):
        return CMYK(
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
    return CMYK(*[v * constants.CMYK_MAX for v in (c, m, y, k)])


def rgb_to_hex(*args) -> HEX:
    parsed_rgb = parse.parse(*args)
    return HEX("".join(map(float_to_hex, parsed_rgb)))


def rgb_to_hls(*args) -> HLS:
    rgb = parse.parse(*args)
    return HLS(*colorsys.rgb_to_hls(*[v / constants.RGB_MAX for v in rgb]))


def rgb_to_hsv(*args) -> HSV:
    rgb = parse.parse(*args)
    return HSV(*colorsys.rgb_to_hsv(*[v / constants.RGB_MAX for v in rgb]))
