import math
from chromato import convert, validation, utils
from chromato.spaces import Color, CMYK, HEX, HSL, HSV, RGB


def _is_possibly_hex(arg):
    return isinstance(arg, str) and len(arg.strip("# ")) > 0


def _parse_rgb_values(*args) -> tuple:
    return tuple(map(math.ceil, _parse_float_values(*args)))


def _parse_float_values(*args) -> tuple:
    return tuple([0 if not v else float(v) for v in args])


def parse_hex(_hex) -> str:
    if not _hex:
        return "000000"

    elif isinstance(_hex, HEX):
        return str(_hex)

    elif isinstance(_hex, CMYK):
        return str(convert.cmyk_to_hex(_hex))

    elif isinstance(_hex, HSL):
        return str(convert.hsl_to_hex(_hex))

    elif isinstance(_hex, HSV):
        return str(convert.hsv_to_hex(_hex))

    elif isinstance(_hex, RGB):
        return str(convert.rgb_to_hex(_hex))

    elif isinstance(_hex, Color):
        return str(_hex.hex)

    elif isinstance(_hex, dict) and "hex" in _hex:
        return parse_hex(_hex["hex"])

    try:
        parsed_hex = str(_hex).strip("# ")

        if 1 == len(parsed_hex):
            parsed_hex = 6 * parsed_hex

        elif 3 == len(parsed_hex):
            parsed_hex = "".join(char * 2 for char in parsed_hex)

        if not validation.is_hex(parsed_hex):
            raise

    except BaseException:
        raise ValueError("Unable to parse value as HEX", _hex)

    return parsed_hex


def parse_hsv(*args) -> tuple:
    h, s, v = (0, 0, 0)

    try:
        num_args = len(args)

        if 1 == num_args:
            arg = args[0]

            if isinstance(arg, HSV):
                return tuple(arg)

            elif isinstance(arg, HEX):
                return tuple(convert.hex_to_hsv(arg))

            elif isinstance(arg, CMYK):
                return tuple(convert.cmyk_to_hsv(arg))

            elif isinstance(arg, HSL):
                return tuple(convert.hsl_to_hsv(arg))

            elif isinstance(arg, RGB):
                return tuple(convert.rgb_to_hsv(arg))

            elif isinstance(arg, Color):
                return tuple(arg.hsv)

            elif type(arg) in [tuple, list]:
                return parse_hsv(*arg)

            elif isinstance(arg, dict) and utils.dict_has_keys(arg, "hsv"):
                h, s, v = arg["h"], arg["s"], arg["v"]

            elif _is_possibly_hex(arg):
                h, s, v = convert.hex_to_hsv(parse_hex(arg))

            else:
                h = arg

        elif 2 == num_args:
            h, s = args

        elif 3 == num_args:
            h, s, v = args

        h, s, v = _parse_float_values(h, s, v)

        if not validation.is_hsv(h, s, v):
            raise

    except BaseException:
        raise ValueError("Unable to parse value as HSV", args)

    return h, s, v


def parse_hsl(*args) -> tuple:
    h, s, l = (0, 0, 0)

    try:
        num_args = len(args)

        if 1 == num_args:
            arg = args[0]

            if isinstance(arg, HSL):
                return tuple(arg)

            elif isinstance(arg, HEX):
                return tuple(convert.hex_to_hsl(arg))

            elif isinstance(arg, CMYK):
                return tuple(convert.cmyk_to_hsl(arg))

            elif isinstance(arg, HSV):
                return tuple(convert.hsv_to_hsl(arg))

            elif isinstance(arg, RGB):
                return tuple(convert.rgb_to_hsl(arg))

            elif isinstance(arg, Color):
                return tuple(arg.hsl)

            elif type(arg) in [tuple, list]:
                return parse_hsl(*arg)

            elif isinstance(arg, dict) and utils.dict_has_keys(arg, "hsl"):
                h, s, l = arg["h"], arg["s"], arg["l"]

            elif _is_possibly_hex(arg):
                h, s, l = convert.hex_to_hsl(parse_hex(arg))

            else:
                h = arg

        elif 2 == num_args:
            h, s = args

        elif 3 == num_args:
            h, s, l = args

        h, s, l = _parse_float_values(h, s, l)

        if not validation.is_hsl(h, s, l):
            raise

    except BaseException:
        raise ValueError("Unable to parse value as HSL", args)

    return h, s, l


def parse_cmyk(*args) -> tuple:
    c, m, y, k = (0, 0, 0, 100)

    try:
        num_args = len(args)

        if 1 == num_args:
            arg = args[0]

            if isinstance(arg, CMYK):
                return tuple(arg)

            elif isinstance(arg, HEX):
                return tuple(convert.hex_to_cmyk(arg))

            elif isinstance(arg, HSL):
                return tuple(convert.hsl_to_cmyk(arg))

            elif isinstance(arg, HSV):
                return tuple(convert.hsv_to_cmyk(arg))

            elif isinstance(arg, RGB):
                return tuple(convert.rgb_to_cmyk(arg))

            elif isinstance(arg, Color):
                return tuple(arg.cmyk)

            elif type(arg) in [tuple, list]:
                return parse_cmyk(*arg)

            elif isinstance(arg, dict) and utils.dict_has_keys(arg, "cmyk"):
                c, m, y, k = arg["c"], arg["m"], arg["y"], arg["k"]

            elif _is_possibly_hex(arg):
                c, m, y, k = convert.hex_to_cmyk(parse_hex(arg))

            else:
                c = arg

        elif 2 == num_args:
            c, m = args

        elif 3 == num_args:
            c, m, y = args

        elif 4 == num_args:
            c, m, y, k = args

        c, m, y, k = _parse_float_values(c, m, y, k)

        if not validation.is_cmyk(c, m, y, k):
            raise

    except BaseException:
        raise ValueError("Unable to parse value as CMYK", args)

    return c, m, y, k


def parse_rgb(*args) -> tuple:
    r, g, b = (0, 0, 0)

    try:
        num_args = len(args)

        if 1 == num_args:
            arg = args[0]

            if isinstance(arg, RGB):
                return tuple(arg)

            elif isinstance(arg, CMYK):
                return tuple(convert.cmyk_to_rgb(arg))

            elif isinstance(arg, HSV):
                return tuple(convert.hsv_to_rgb(arg))

            elif isinstance(arg, HSL):
                return tuple(convert.hsl_to_rgb(arg))

            elif isinstance(arg, HEX):
                return tuple(convert.hex_to_rgb(arg))

            elif isinstance(arg, Color):
                return tuple(arg.rgb)

            elif type(arg) in [tuple, list]:
                return parse_rgb(*arg)

            elif isinstance(arg, dict) and utils.dict_has_keys(arg, "rgb"):
                r, g, b = arg["r"], arg["g"], arg["b"]

            elif _is_possibly_hex(arg):
                r, g, b = convert.hex_to_rgb(parse_hex(arg))

            else:
                r = arg

        elif 2 == num_args:
            r, g = args

        elif 3 == num_args:
            r, g, b = args

        r, g, b = _parse_rgb_values(r, g, b)

        if not validation.is_rgb(r, g, b):
            raise

    except BaseException:
        raise ValueError("Unable to parse value as RGB", args)

    return r, g, b
