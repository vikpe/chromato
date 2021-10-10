import math
from . import convert, validation
from .spaces import CMYK, HEX, HLS, HSV, RGB


def dict_has_keys(_dict: dict, keys: iter) -> bool:
    return all(k in _dict for k in keys)


def parse_rgb_values(*args) -> tuple:
    return tuple(map(math.ceil, parse_float_values(*args)))


def parse_float_values(*args) -> tuple:
    return tuple([0 if not v else float(v) for v in args])


def parse_hex(_hex) -> str:
    if not _hex:
        return "000000"

    elif isinstance(_hex, HEX):
        return str(_hex)

    elif isinstance(_hex, CMYK):
        return str(convert.cmyk_to_hex(_hex))

    elif isinstance(_hex, HLS):
        return str(convert.hls_to_hex(_hex))

    elif isinstance(_hex, HSV):
        return str(convert.hsv_to_hex(_hex))

    elif isinstance(_hex, RGB):
        return str(convert.rgb_to_hex(_hex))

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

            elif isinstance(arg, HLS):
                return tuple(convert.hls_to_hsv(arg))

            elif isinstance(arg, RGB):
                return tuple(convert.rgb_to_hsv(arg))

            elif type(arg) in [tuple, list]:
                return parse_hsv(*arg)

            elif isinstance(arg, dict) and dict_has_keys(arg, "hsv"):
                h, s, v = arg["h"], arg["s"], arg["v"]

            else:
                h = arg

        elif 2 == num_args:
            h, s = args

        elif 3 == num_args:
            h, s, v = args

        h, s, v = parse_float_values(h, s, v)

        if not validation.is_hsv(h, s, v):
            raise

    except BaseException:
        raise ValueError("Unable to parse value as HSV", args)

    return h, s, v


def parse_hls(*args) -> tuple:
    h, l, s = (0, 0, 0)

    try:
        num_args = len(args)

        if 1 == num_args:
            arg = args[0]

            if isinstance(arg, HLS):
                return tuple(arg)

            elif isinstance(arg, HEX):
                return tuple(convert.hex_to_hls(arg))

            elif isinstance(arg, CMYK):
                return tuple(convert.cmyk_to_hls(arg))

            elif isinstance(arg, HSV):
                return tuple(convert.hsv_to_hls(arg))

            elif isinstance(arg, RGB):
                return tuple(convert.rgb_to_hls(arg))

            elif type(arg) in [tuple, list]:
                return parse_hls(*arg)

            elif isinstance(arg, dict) and dict_has_keys(arg, "hls"):
                h, l, s = arg["h"], arg["l"], arg["s"]

            else:
                h = arg

        elif 2 == num_args:
            h, l = args

        elif 3 == num_args:
            h, l, s = args

        h, l, s = parse_float_values(h, l, s)

        if not validation.is_hls(h, l, s):
            raise

    except BaseException:
        raise ValueError("Unable to parse value as HLS", args)

    return h, l, s


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

            elif isinstance(arg, HLS):
                return tuple(convert.hls_to_cmyk(arg))

            elif isinstance(arg, HSV):
                return tuple(convert.hsv_to_cmyk(arg))

            elif isinstance(arg, RGB):
                return tuple(convert.rgb_to_cmyk(arg))

            elif type(arg) in [tuple, list]:
                return parse_cmyk(*arg)

            elif isinstance(arg, dict) and dict_has_keys(arg, "cmyk"):
                c, m, y, k = arg["c"], arg["m"], arg["y"], arg["k"]

            else:
                c = arg

        elif 2 == num_args:
            c, m = args

        elif 3 == num_args:
            c, m, y = args

        elif 4 == num_args:
            c, m, y, k = args

        c, m, y, k = parse_float_values(c, m, y, k)

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

            elif isinstance(arg, HLS):
                return tuple(convert.hls_to_rgb(arg))

            elif isinstance(arg, HEX):
                return tuple(convert.hex_to_rgb(arg))

            elif type(arg) in [tuple, list]:
                return parse_rgb(*arg)

            elif isinstance(arg, dict) and dict_has_keys(arg, "rgb"):
                r, g, b = arg["r"], arg["g"], arg["b"]

            else:
                r = arg

        elif 2 == num_args:
            r, g = args

        elif 3 == num_args:
            r, g, b = args

        r, g, b = parse_rgb_values(r, g, b)

        if not validation.is_rgb(r, g, b):
            raise

    except BaseException:
        raise ValueError("Unable to parse value as RGB", args)

    return r, g, b


def parse_value(*args) -> tuple:
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

            elif isinstance(arg, HLS):
                return tuple(convert.hls_to_rgb(arg))

            elif isinstance(arg, HEX):
                return tuple(convert.hex_to_rgb(arg))

            elif (isinstance(arg, tuple) or isinstance(arg, list)) and 3 == len(arg):
                r, g, b = arg

            elif isinstance(arg, dict) and dict_has_keys(arg, ["r", "g", "b"]):
                r, g, b = arg["r"], arg["g"], arg["b"]

            elif isinstance(arg, str) and len(arg) > 0:
                r, g, b = convert.hex_to_rgb(parse_hex(arg))

            else:
                r = arg

        elif 2 == num_args:
            r = args[0]
            g = args[1]

        elif 3 == num_args:
            return parse_value(args)

        r, g, b = parse_rgb_values(r, g, b)

        if not validation.is_rgb(r, g, b):
            raise

    except BaseException:
        raise ValueError("Unable to parse value", args)

    return r, g, b
