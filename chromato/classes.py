from . import convert, parse

from .spaces import CMYK, HEX, HLS, HSV, RGB


class Color:
    __rgb: RGB

    def __init__(self, *args):
        self.__rgb = parse.parse(*args)

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
