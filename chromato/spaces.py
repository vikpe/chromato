import attr

from . import constants, convert, parse


class ColorSpace(object):
    def __iter__(self):
        for val in self.__dict__.values():
            yield val


def parse_float_value(value) -> float:
    if not value:
        return 0
    else:
        return float(value)


@attr.s
class CMYK(ColorSpace):
    c = attr.ib(default=constants.CMYK_MIN, converter=parse_float_value)
    m = attr.ib(default=constants.CMYK_MIN, converter=parse_float_value)
    y = attr.ib(default=constants.CMYK_MIN, converter=parse_float_value)
    k = attr.ib(default=constants.CMYK_MAX, converter=parse_float_value)


class HEX(str):
    pass


@attr.s
class HLS(ColorSpace):
    h = attr.ib(default=constants.HLS_MIN, converter=parse_float_value)
    l = attr.ib(default=constants.HLS_MIN, converter=parse_float_value)
    s = attr.ib(default=constants.HLS_MIN, converter=parse_float_value)


@attr.s
class HSV(ColorSpace):
    h = attr.ib(default=constants.HSV_MIN, converter=parse_float_value)
    s = attr.ib(default=constants.HSV_MIN, converter=parse_float_value)
    v = attr.ib(default=constants.HSV_MIN, converter=parse_float_value)


@attr.s
class RGB(ColorSpace):
    r = attr.ib(default=constants.RGB_MIN, converter=parse_float_value)
    g = attr.ib(default=constants.RGB_MIN, converter=parse_float_value)
    b = attr.ib(default=constants.RGB_MIN, converter=parse_float_value)


class Color:
    __rgb: tuple

    def __init__(self, *args):
        self.__rgb = parse.parse_value(*args)

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.rgb == other.rgb
        else:
            return False

    def __repr__(self):
        return f"Color(r={self.rgb.r}, g={self.rgb.g}, b={self.rgb.b})"

    @classmethod
    def from_cmyk(cls, *args):
        return Color(convert.cmyk_to_rgb(*args))

    @classmethod
    def from_hex(cls, *args):
        return Color(convert.hex_to_rgb(*args))

    @classmethod
    def from_hls(cls, *args):
        return Color(convert.hls_to_rgb(*args))

    @classmethod
    def from_hsv(cls, *args):
        return Color(convert.hsv_to_rgb(*args))

    @classmethod
    def from_rgb(cls, *args):
        return Color(*args)

    @property
    def rgb(self) -> RGB:
        return RGB(*self.__rgb)

    @property
    def hex(self) -> HEX:
        return HEX(convert.rgb_to_hex(self.rgb))

    @property
    def cmyk(self) -> CMYK:
        return CMYK(*convert.rgb_to_cmyk(self.rgb))

    @property
    def hls(self) -> HLS:
        return HLS(*convert.rgb_to_hls(self.rgb))

    @property
    def hsv(self) -> HSV:
        return HSV(*convert.rgb_to_hsv(self.rgb))
