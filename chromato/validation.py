import string
import numbers

from . import constants


def is_valid_number(value) -> bool:
    return not isinstance(value, bool) and isinstance(value, numbers.Number)


def is_valid_hex(value) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 6
        and all(c in string.hexdigits for c in value)
    )


def is_valid_rgb(r, g, b) -> bool:
    return all(is_valid_rgb_value(v) for v in (r, g, b))


def is_in_range(value, range_from, range_to):
    if not is_valid_number(value):
        return False
    else:
        return range_from <= value <= range_to


def is_valid_rgb_value(value) -> bool:
    return is_in_range(
        value,
        constants.RGB_MIN,
        constants.RGB_MAX,
    )


def is_valid_cmyk_value(value) -> bool:
    return is_in_range(
        value,
        constants.CMYK_MIN,
        constants.CMYK_MAX,
    )


def is_valid_cmyk(c, m, y, k) -> bool:
    return all(is_valid_cmyk_value(v) for v in (c, m, y, k))


def is_valid_hls_value(value) -> bool:
    return is_in_range(
        value,
        constants.HLS_MIN,
        constants.HLS_MAX,
    )


def is_valid_hls(h, l, s) -> bool:
    return all(is_valid_hls_value(v) for v in (h, l, s))


def is_valid_hsv_value(value) -> bool:
    return is_in_range(
        value,
        constants.HSV_MIN,
        constants.HSV_MAX,
    )


def is_valid_hsv(h, s, v) -> bool:
    return all(is_valid_hsv_value(v) for v in (h, s, v))
