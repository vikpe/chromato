import attr

from .constants import RGB_MIN, CMYK_MIN


class ColorSpace(object):
    def __iter__(self):
        for val in self.__dict__.values():
            yield val


class HEX(str):
    pass


@attr.s
class RGB(ColorSpace):
    r = attr.ib(default=RGB_MIN, converter=float)
    g = attr.ib(default=RGB_MIN, converter=float)
    b = attr.ib(default=RGB_MIN, converter=float)


@attr.s
class HLS(ColorSpace):
    h = attr.ib(default=0, converter=float)
    l = attr.ib(default=0, converter=float)
    s = attr.ib(default=0, converter=float)


@attr.s
class HSV(ColorSpace):
    h = attr.ib(default=0, converter=float)
    s = attr.ib(default=0, converter=float)
    v = attr.ib(default=0, converter=float)


@attr.s
class CMYK(ColorSpace):
    c = attr.ib(default=CMYK_MIN, converter=float)
    m = attr.ib(default=CMYK_MIN, converter=float)
    y = attr.ib(default=CMYK_MIN, converter=float)
    k = attr.ib(default=CMYK_MIN, converter=float)
