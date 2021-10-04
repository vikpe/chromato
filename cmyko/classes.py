from . import convert, parse, spaces


class Color:
    __rgb: spaces.RGB

    def __init__(self, *args):
        self.__rgb = parse.parse(*args)

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.rgb == other.rgb
        elif isinstance(other, spaces.RGB):
            return self.rgb == other
        else:
            return False

    @property
    def rgb(self) -> spaces.RGB:
        return self.__rgb

    @property
    def hex(self) -> spaces.HEX:
        return convert.rgb_to_hex(self.rgb)

    @property
    def cmyk(self) -> spaces.CMYK:
        return convert.rgb_to_cmyk(self.rgb)

    @property
    def hls(self) -> spaces.HLS:
        return convert.rgb_to_hls(self.rgb)

    @property
    def hsv(self) -> spaces.HSV:
        return convert.rgb_to_hsv(self.rgb)
