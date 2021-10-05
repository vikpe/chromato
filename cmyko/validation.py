import string


def is_valid_hex(value) -> bool:
    _hex = str(value).lstrip("#")

    return len(_hex) in (3, 6) and all(c in string.hexdigits for c in _hex)
