import attr

from . import constants, convert, parse


class ColorSpace(object):
    def __iter__(self):
        for val in self.__dict__.values():
            yield val


def parse_rgb_value(value) -> float:
    if not value:
        return constants.RGB_MIN
    else:
        return round(float(value), constants.RGB_PRECISION)


@attr.s
class CMYK(ColorSpace):
    c = attr.ib(default=constants.CMYK_MIN, converter=float)
    m = attr.ib(default=constants.CMYK_MIN, converter=float)
    y = attr.ib(default=constants.CMYK_MIN, converter=float)
    k = attr.ib(default=constants.CMYK_MAX, converter=float)


class HEX(str):
    pass


@attr.s
class HLS(ColorSpace):
    h = attr.ib(default=constants.HLS_MIN, converter=float)
    l = attr.ib(default=constants.HLS_MIN, converter=float)
    s = attr.ib(default=constants.HLS_MIN, converter=float)


@attr.s
class HSV(ColorSpace):
    h = attr.ib(default=constants.HSV_MIN, converter=float)
    s = attr.ib(default=constants.HSV_MIN, converter=float)
    v = attr.ib(default=constants.HSV_MIN, converter=float)


@attr.s
class RGB(ColorSpace):
    r = attr.ib(default=constants.RGB_MIN, converter=parse_rgb_value)
    g = attr.ib(default=constants.RGB_MIN, converter=parse_rgb_value)
    b = attr.ib(default=constants.RGB_MIN, converter=parse_rgb_value)


class Color:
    __rgb: RGB

    def __init__(self, *args):
        self.__rgb = parse.parse_value(*args)

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.rgb == other.rgb
        else:
            return False

    @property
    def rgb(self) -> RGB:
        return self.__rgb

    @property
    def hex(self) -> HEX:
        return convert.rgb_to_hex(self.rgb)

    @property
    def cmyk(self) -> CMYK:
        return convert.rgb_to_cmyk(self.rgb)

    @property
    def hls(self) -> HLS:
        return convert.rgb_to_hls(self.rgb)

    @property
    def hsv(self) -> HSV:
        return convert.rgb_to_hsv(self.rgb)
