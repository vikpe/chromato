import string
import numbers

from . import constants


def is_number(value) -> bool:
    return not isinstance(value, bool) and isinstance(value, numbers.Number)


def is_hex(value) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 6
        and all(c in string.hexdigits for c in value)
    )


def is_rgb(r, g, b) -> bool:
    return all(is_rgb_value(v) for v in (r, g, b))


def is_number_in_range(value, range_from, range_to):
    if not is_number(value):
        return False
    else:
        return range_from <= value <= range_to


def is_rgb_value(value) -> bool:
    return is_number_in_range(
        value,
        constants.RGB_MIN,
        constants.RGB_MAX,
    )


def is_cmyk_value(value) -> bool:
    return is_number_in_range(
        value,
        constants.CMYK_MIN,
        constants.CMYK_MAX,
    )


def is_cmyk(c, m, y, k) -> bool:
    return all(is_cmyk_value(v) for v in (c, m, y, k))


def is_hls_value(value) -> bool:
    return is_number_in_range(
        value,
        constants.HLS_MIN,
        constants.HLS_MAX,
    )


def is_hls(h, l, s) -> bool:
    return all(is_hls_value(v) for v in (h, l, s))


def is_hsv_value(value) -> bool:
    return is_number_in_range(
        value,
        constants.HSV_MIN,
        constants.HSV_MAX,
    )


def is_hsv(h, s, v) -> bool:
    return all(is_hsv_value(v) for v in (h, s, v))
