from . import convert, validation

from .spaces import CMYK, HEX, HLS, HSV, RGB


def parse_hex(_hex) -> HEX:
    if isinstance(_hex, HEX):
        return _hex

    try:
        parsed_hex = _hex.lstrip("#")

        if 1 == len(parsed_hex):
            parsed_hex = 6 * parsed_hex
        elif 3 == len(parsed_hex):
            parsed_hex = "".join(char * 2 for char in parsed_hex)

        if not validation.is_hex(parsed_hex):
            raise

    except BaseException:
        raise ValueError("Unable to parse value as HEX", _hex)

    return HEX(parsed_hex)


def parse_hsv(*args) -> HSV:
    h, s, v = HSV()

    try:
        num_args = len(args)

        if 1 == num_args:
            arg = args[0]

            if isinstance(arg, HSV):
                return arg

            elif isinstance(arg, tuple) or isinstance(arg, list):
                return parse_hsv(*arg)

            else:
                h = arg

        elif 2 == num_args:
            h, s = args

        elif 3 == num_args:
            h, s, v = args

        hsv = HSV(h, s, v)

    except BaseException:
        raise ValueError("Unable to parse value as HSV", args)

    return hsv


def parse_hls(*args) -> HLS:
    h, l, s = HLS()

    try:
        num_args = len(args)

        if 1 == num_args:
            arg = args[0]

            if isinstance(arg, HLS):
                return arg

            elif isinstance(arg, tuple) or isinstance(arg, list):
                return parse_hls(*arg)

            else:
                h = arg

        elif 2 == num_args:
            h, l = args

        elif 3 == num_args:
            h, l, s = args

        hls = HLS(h, l, s)

    except BaseException:
        raise ValueError("Unable to parse value as HLS", args)

    return hls


def parse_cmyk(*args) -> CMYK:
    c, m, y, k = CMYK()

    try:
        num_args = len(args)

        if 1 == num_args:
            arg = args[0]

            if isinstance(arg, CMYK):
                return arg

            elif isinstance(arg, tuple) or isinstance(arg, list):
                return parse_cmyk(*arg)

            else:
                c = arg

        elif 2 == num_args:
            c, m = args

        elif 3 == num_args:
            c, m, y = args

        elif 4 == num_args:
            c, m, y, k = args

        cmyk = CMYK(c, m, y, k)

    except BaseException:
        raise ValueError("Unable to parse value as CMYK", args)

    return cmyk


def parse_value(*args) -> RGB:
    r, g, b = (0, 0, 0)

    try:
        num_args = len(args)

        if 1 == num_args:
            arg = args[0]

            if isinstance(arg, int) or isinstance(arg, float):
                r = arg

            elif isinstance(arg, RGB):
                return arg

            elif isinstance(arg, CMYK):
                return convert.cmyk_to_rgb(arg)

            elif isinstance(arg, HSV):
                return convert.hsv_to_rgb(arg)

            elif isinstance(arg, HLS):
                return convert.hls_to_rgb(arg)

            elif isinstance(arg, HEX):
                return convert.hex_to_rgb(arg)

            elif isinstance(arg, tuple) and 3 == len(arg):
                r, g, b = arg

            elif isinstance(arg, list) and 3 == len(arg):
                r, g, b = arg

            elif isinstance(arg, str) and len(arg) > 0:
                r, g, b = convert.hex_to_rgb(parse_hex(arg))

        elif 2 == num_args:
            r = args[0]
            g = args[1]

        elif 3 == num_args:
            return parse_value(args)

        rgb = RGB(r, g, b)

    except BaseException:
        raise ValueError("Unable to parse value", args)

    return rgb
