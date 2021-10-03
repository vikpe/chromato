import colorsys

from .constants import RGB_MIN, RGB_MAX, CMYK_MIN, CMYK_MAX
from .parse import parse_hex
from .spaces import RGB, HLS, HSV, YIQ, CMYK


def rgb_to_yiq(rgb) -> YIQ:
    return YIQ(*colorsys.rgb_to_yiq(*rgb))


def yiq_to_rgb(yiq) -> RGB:
    return RGB(*colorsys.yiq_to_rgb(*yiq))


def rgb_to_hls(rgb) -> HLS:
    return HLS(*colorsys.rgb_to_hls(*rgb))


def hls_to_rgb(hls) -> RGB:
    return RGB(*colorsys.hls_to_rgb(*hls))


def rgb_to_hsv(rgb) -> HSV:
    return HSV(*colorsys.rgb_to_hsv(*rgb))


def hsv_to_rgb(hsv) -> RGB:
    return RGB(*colorsys.hsv_to_rgb(*hsv))


def rgb_to_cmyk(rgb) -> CMYK:
    r, g, b = rgb

    if (r == RGB_MIN) and (g == RGB_MIN) and (b == RGB_MIN):
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
    return CMYK(*[c * CMYK_MAX, m * CMYK_MAX, y * CMYK_MAX, k * CMYK_MAX])


def cmyk_to_rgb(cmyk) -> RGB:
    c, m, y, k = cmyk
    r = RGB_MAX * (1.0 - (c + k) / CMYK_MAX)
    g = RGB_MAX * (1.0 - (m + k) / CMYK_MAX)
    b = RGB_MAX * (1.0 - (y + k) / CMYK_MAX)
    return RGB(r, g, b)


def int_to_hex(_int: int) -> str:
    template = "{:02x}" if _int < 16 else "{:x}"
    return template.format(_int)


def hex_to_int(_hex: str) -> int:
    return int(_hex, 16)


def rgb_to_hex(rgb) -> str:
    return "".join(map(int_to_hex, rgb))


def hex_to_rgb(_hex) -> RGB:
    result = parse_hex(_hex)
    hlen = len(result)
    pairs = hlen // 3
    r, g, b = [hex_to_int(result[i : i + pairs]) for i in range(0, hlen, pairs)]
    return RGB(r, g, b)
