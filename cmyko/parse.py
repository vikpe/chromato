from .spaces import RGB


def parse_hex(_hex) -> str:
    result = _hex.lstrip("#")
    if 3 == len(result):
        return "".join(c * 2 for c in result)
    else:
        return result


def parse_rgb(args) -> RGB:
    return RGB(*args)
