import colorsys

from .constants import RGB_MIN, RGB_MAX, CMYK_MIN, CMYK_MAX
from .parse import parse_hex, parse, parse_cmyk, parse_hls, parse_hsv
from .spaces import RGB, HLS, HSV, CMYK, HEX


def rgb_to_hls(*args) -> HLS:
    rgb = parse(*args)
    return HLS(*colorsys.rgb_to_hls(*[v / RGB_MAX for v in rgb]))


def hls_to_rgb(*args) -> RGB:
    hls = parse_hls(*args)
    return RGB(*[RGB_MAX * v for v in colorsys.hls_to_rgb(*hls)])


def rgb_to_hsv(*args) -> HSV:
    rgb = parse(*args)
    return HSV(*colorsys.rgb_to_hsv(*[v / RGB_MAX for v in rgb]))


def hsv_to_rgb(*args) -> RGB:
    hsv = parse_hsv(*args)
    return RGB(*[RGB_MAX * v for v in colorsys.hsv_to_rgb(*hsv)])


def rgb_to_cmyk(*args) -> CMYK:
    r, g, b = parse(*args)

    if (r, g, b) == (RGB_MIN, RGB_MIN, RGB_MIN):
        return CMYK(CMYK_MIN, CMYK_MIN, CMYK_MIN, CMYK_MAX)  # black

    # rgb [0,255] -> cmy [0,1]
    c = 1 - r / RGB_MAX
    m = 1 - g / RGB_MAX
    y = 1 - b / RGB_MAX

    # extract out k [0,1]
    k = min(c, m, y)
    c = c - k
    m = m - k
    y = y - k

    # rescale to the range [0,100]
    return CMYK(*[v * CMYK_MAX for v in (c, m, y, k)])


def cmyk_to_rgb(*args) -> RGB:
    c, m, y, k = parse_cmyk(*args)
    r = RGB_MAX * (1.0 - (c + k) / CMYK_MAX)
    g = RGB_MAX * (1.0 - (m + k) / CMYK_MAX)
    b = RGB_MAX * (1.0 - (y + k) / CMYK_MAX)
    return RGB(r, g, b)


def float_to_hex(_float: float) -> str:
    template = "{:02x}" if _float < 16 else "{:x}"
    return template.format(int(_float))


def hex_to_int(_hex: str) -> int:
    return int(_hex, 16)


def rgb_to_hex(*args) -> HEX:
    parsed_rgb = parse(*args)
    return HEX("".join(map(float_to_hex, parsed_rgb)))


def hex_to_rgb(_hex) -> RGB:
    result = parse_hex(_hex)
    hlen = len(result)
    pairs = hlen // 3
    r, g, b = [hex_to_int(result[i : i + pairs]) for i in range(0, hlen, pairs)]
    return RGB(r, g, b)
