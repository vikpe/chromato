from collections import UserString

import attr

from chromato import convert, parse


class ColorSpace(object):
    def __iter__(self):
        for val in self.__dict__.values():
            yield val


@attr.s(init=False)
class CMYK(ColorSpace):
    c = attr.ib()
    m = attr.ib()
    y = attr.ib()
    k = attr.ib()

    def __init__(self, *args):
        c, m, y, k = parse.parse_cmyk(*args)
        self.__attrs_init__(c, m, y, k)


class HEX(ColorSpace, UserString):
    def __init__(self, seq: object) -> None:
        super().__init__(parse.parse_hex(seq))


@attr.s(init=False)
class HLS(ColorSpace):
    h = attr.ib()
    l = attr.ib()
    s = attr.ib()

    def __init__(self, *args):
        h, l, s = parse.parse_hls(*args)
        self.__attrs_init__(h, l, s)


@attr.s(init=False)
class HSV(ColorSpace):
    h = attr.ib()
    s = attr.ib()
    v = attr.ib()

    def __init__(self, *args):
        h, s, v = parse.parse_hsv(*args)
        self.__attrs_init__(h, s, v)


@attr.s(init=False)
class RGB(ColorSpace):
    r = attr.ib()
    g = attr.ib()
    b = attr.ib()

    def __init__(self, *args):
        r, g, b = parse.parse_rgb(*args)
        self.__attrs_init__(r, g, b)


class Color:
    __rgb: RGB

    def __init__(self, *args):
        self.__rgb = RGB(parse.parse_rgb(*args))

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.rgb == other.rgb
        else:
            return False

    def __repr__(self):
        return f"Color(r={self.rgb.r}, g={self.rgb.g}, b={self.rgb.b})"

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
