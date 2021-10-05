import string


def is_valid_hex(value) -> bool:
    _hex = str(value).lstrip("#")
    return len(_hex) > 0 and all(c in string.hexdigits for c in _hex)
