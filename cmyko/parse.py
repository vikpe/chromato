from . import convert, constants, spaces


def parse_hex(_hex) -> str:
    result = _hex.lstrip("#")
    if 3 == len(result):
        return "".join(c * 2 for c in result)
    else:
        return result


def parse_cmyk(*args) -> spaces.CMYK:
    c, m, y, k = (
        constants.CMYK_MIN,
        constants.CMYK_MIN,
        constants.CMYK_MIN,
        constants.CMYK_MAX,
    )

    try:
        num_args = len(args)

        if 1 == num_args:
            arg = args[0]

            if isinstance(arg, spaces.CMYK):
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

        cmyk = spaces.CMYK(c, m, y, k)

    except BaseException:
        raise ValueError("Unable to parse value as CMYK", args)

    return cmyk


def parse(*args) -> spaces.RGB:
    r, g, b = (constants.RGB_MIN, constants.RGB_MIN, constants.RGB_MIN)

    try:
        num_args = len(args)

        if 1 == num_args:
            arg = args[0]

            if isinstance(arg, int):
                r = arg

            elif isinstance(arg, spaces.RGB):
                r, g, b = arg

            elif isinstance(arg, spaces.CMYK):
                r, g, b = convert.cmyk_to_rgb(arg)

            elif isinstance(arg, spaces.HSV):
                r, g, b = convert.hsv_to_rgb(arg)

            elif isinstance(arg, spaces.HLS):
                r, g, b = convert.hls_to_rgb(arg)

            elif isinstance(arg, spaces.HEX):
                r, g, b = convert.hex_to_rgb(arg)

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
            return parse(args)

    except BaseException:
        raise ValueError("Unable to parse value", args)

    return spaces.RGB(r, g, b)
