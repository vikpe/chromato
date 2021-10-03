import attr

from .convert import (
    rgb_to_hex,
    rgb_to_cmyk,
    rgb_to_hls,
    rgb_to_hsv,
    rgb_to_yiq,
    hex_to_rgb,
)
from .parse import parse_rgb


# classes
@attr.s
class Color(object):
    rgb = attr.ib(converter=parse_rgb)

    @classmethod
    def from_hex(cls, _hex):
        return cls(hex_to_rgb(_hex))

    @property
    def hex(self):
        return rgb_to_hex(self.rgb)

    @property
    def cmyk(self):
        return rgb_to_cmyk(self.rgb)

    @property
    def hls(self):
        return rgb_to_hls(self.rgb)

    @property
    def hsv(self):
        return rgb_to_hsv(self.rgb)

    @property
    def yiq(self):
        return rgb_to_yiq(self.rgb)
