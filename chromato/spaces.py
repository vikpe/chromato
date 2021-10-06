import attr

from . import constants


class ColorSpace(object):
    def __iter__(self):
        for val in self.__dict__.values():
            yield val


class HEX(str):
    pass


def parse_rgb_value(value) -> float:
    if not value:
        return constants.RGB_MIN
    else:
        return round(float(value), constants.RGB_PRECISION)


@attr.s
class RGB(ColorSpace):
    r = attr.ib(default=constants.RGB_MIN, converter=parse_rgb_value)
    g = attr.ib(default=constants.RGB_MIN, converter=parse_rgb_value)
    b = attr.ib(default=constants.RGB_MIN, converter=parse_rgb_value)


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
class CMYK(ColorSpace):
    c = attr.ib(default=constants.CMYK_MIN, converter=float)
    m = attr.ib(default=constants.CMYK_MIN, converter=float)
    y = attr.ib(default=constants.CMYK_MIN, converter=float)
    k = attr.ib(default=constants.CMYK_MAX, converter=float)
