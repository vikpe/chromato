from . import classes, constants

white = classes.Color(constants.RGB_MAX, constants.RGB_MAX, constants.RGB_MAX)
gray = classes.Color(
    constants.RGB_MAX / 2, constants.RGB_MAX / 2, constants.RGB_MAX / 2
)
black = classes.Color(constants.RGB_MIN, constants.RGB_MIN, constants.RGB_MIN)
red = classes.Color(constants.RGB_MAX, constants.RGB_MIN, constants.RGB_MIN)
green = classes.Color(constants.RGB_MIN, constants.RGB_MAX, constants.RGB_MIN)
blue = classes.Color(constants.RGB_MIN, constants.RGB_MIN, constants.RGB_MAX)
cyan = classes.Color(constants.RGB_MIN, constants.RGB_MAX, constants.RGB_MAX)
magenta = classes.Color(constants.RGB_MAX, constants.RGB_MIN, constants.RGB_MAX)
yellow = classes.Color(constants.RGB_MAX, constants.RGB_MAX, constants.RGB_MIN)
