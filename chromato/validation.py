import string

from . import constants


def is_valid_hex(value) -> bool:
    _hex = str(value).lstrip("#")

    return len(_hex) in (3, 6) and all(c in string.hexdigits for c in _hex)


def is_valid_rgb(r, g, b) -> bool:
    return all(is_valid_rgb_value(v) for v in (r, g, b))


def is_valid_rgb_value(value) -> bool:
    if value is None or value is False:
        return False

    try:
        return (
            constants.RGB_MIN
            <= round(float(value), constants.RGB_PRECISION)
            <= constants.RGB_MAX
        )
    except:
        return False
