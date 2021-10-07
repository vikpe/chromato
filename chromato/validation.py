import string

from . import constants


def is_valid_hex(value) -> bool:
    _hex = str(value).lstrip("#")

    return len(_hex) in (3, 6) and all(c in string.hexdigits for c in _hex)


def is_valid_rgb(r, g, b) -> bool:
    return all(is_valid_rgb_value(v) for v in (r, g, b))


def _is_in_range(value, precision, range_from, range_to):
    if value is None or value is False:
        return False

    try:
        return range_from <= round(float(value), precision) <= range_to
    except:
        return False


def is_valid_rgb_value(value) -> bool:
    return _is_in_range(
        value,
        constants.RGB_PRECISION,
        constants.RGB_MIN,
        constants.RGB_MAX
    )


def is_valid_cmyk_value(value) -> bool:
    return _is_in_range(
        value,
        constants.CMYK_PRECISION,
        constants.CMYK_MIN,
        constants.CMYK_MAX
    )


def is_valid_cmyk(c, m, y, k) -> bool:
    return all(is_valid_cmyk_value(v) for v in (c, m, y, k))
