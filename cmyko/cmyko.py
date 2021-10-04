import attr

from . import convert, parse


# classes
@attr.s
class Color(object):
    rgb = attr.ib(converter=parse.parse)

    @property
    def hex(self):
        return convert.rgb_to_hex(self.rgb)

    @property
    def cmyk(self):
        return convert.rgb_to_cmyk(self.rgb)

    @property
    def hls(self):
        return convert.rgb_to_hls(self.rgb)

    @property
    def hsv(self):
        return convert.rgb_to_hsv(self.rgb)
