<div align="center">
    <h1>🍅 chromato</h1>
    <p>
        <b>Fresh color utilities for Python</b>
    </p>

[![PyPI version](https://badge.fury.io/py/chromato.svg)](https://pypi.org/project/chromato/) [![test](https://github.com/vikpe/chromato/actions/workflows/test.yml/badge.svg)](https://github.com/vikpe/chromato/actions/workflows/test.yml) [![codecov](https://codecov.io/gh/vikpe/chromato/branch/main/graph/badge.svg)](https://codecov.io/gh/vikpe/chromato)

<br>

</div>

* [**Color spaces**](#color-spaces): CMYK, HEX, RGB, HSL, HSV
* [**Color class**](#color-class): Convenience class for color manipulation
* [**Operations**](#operations): shade, tone, tint, grayscale, invert, complement, add, subtract, multiply
* [**Conversion**](#conversion): Convert any color space to any color space
* [Parsing](#parsing) 
* [Validation](#validation)
* (zero dependecies!)

<br>

# Install

```shell
pip install chromato
```

<br>

# Example usage

**Color class**
```python
from chromato.spaces import Color

red = Color(255, 0, 0)

red.cmyk  # CMYK(c=0, m=100, y=100, k=0)
red.hex   # HEX(ff0000)
red.rgb   # RGB(r=255, g=0, b=0)
red.hsl   # HSL(h=0, s=1, l=0.5)
red.hsv   # HSV(h=0, s=1, v=1)
```

**Operations**
```python
from chromato import operations
from chromato.spaces import RGB

red = RGB(255, 0, 0)
blue = RGB(0, 0, 255)

operations.invert(red).rgb       # RGB(r=0, g=255, b=255)
operations.add(red, blue)        # RGB(r=255, g=0, b=255)
operations.blend(red, blue).rgb  # RGB(r=128, g=0, b=128)
operations.tint(red, 0.1).rgb    # RGB(r=255, g=26, b=26)
```

**Conversion**
```python
from chromato import convert

convert.rgb_to_hex(255, 0, 0)  # HEX(ff0000)
convert.hex_to_rgb("ff0000")   # RGB(r=255, g=0, b=0)
convert.hex_to_cmyk("f0f")     # CMYK(c=0, m=100, y=0, k=0)
```

<br>

# API

## Color spaces

Name | Properties | Range
---|---|---
CMYK | `c`, `m`, `y`, `k` | `0-100`, `0-100`, `0-100`, `0-100`
HEX | (is a string) | `000000-ffffff`
HSL | `h`, `s`, `l` |  `0-1`, `0-1`, `0-1`
HSV | `h`, `s`, `v` |  `0-1`, `0-1`, `0-1`
RGB | `r`, `g`, `b` | `0-255`, `0-255`, `0-255`

```python
from chromato.spaces import CMYK, HEX, HSL, HSV, RGB

red_cmyk = CMYK(0, 100, 100, 0)
red_hex  = HEX("ff0000")
red_hsl  = HSL(0, 1, 0.5)
red_hsv  = HSV(0, 1, 1)
red_rgb  = RGB(255, 0, 0)
```

## Color class

**Properties**
```python
from chromato.spaces import Color

red = Color(255, 0, 0)

red.cmyk  # CMYK(c=0, m=100, y=100, k=0)
red.hex   # HEX(ff0000)
red.hsl   # HSL(h=0, s=1, l=0.5)
red.hsv   # HSV(h=0, s=1, v=1)
red.rgb   # RGB(r=255, g=0, b=0)
```

**Construct**

```python
# examples below are equal
Color(255, 0, 0)
Color((255, 0, 0))
Color([255, 0, 0])
Color({"r": 255, "g": 0, "b": 0})
Color("ff0000")
Color("ff0")
Color(Color(255, 0, 0))
Color(RGB(255, 0, 0))
Color(HEX("ff0"))
Color(HSV(0, 1, 1))
Color(HSL(0, 1, 0.5))
Color(CMYK(0, 100, 100, 0))
```

## Operations
Each operation take one or several color values and returns a `Color` instance.

Operation | Description
--- | ---
**`blend`**`(color1, color2, factor)` | Blend/mix colors
**`tint`**`(color, factor)` | Increase lightness (blend with white)
**`shade`**`(color, factor)` | Increase darkness (blend with black)
**`tone`**`(color, factor)` | Reduce colorfullness (blend with gray)
**`invert`**`(color)` | Invert color
**`complement`**`(color)` | Complementary color
**`add`**`(color1, color2)` | Add colors
**`subtract`**`(color1, color2)` | Subtract colors
**`multiply`**`(color1, color2)` | Multiply colors

* **Arguments**: `color<any>`, `factor <float> [0-1]`
* **Returns**: instance of `Color`

**Example**
```python
from chromato.spaces import RGB
from chromato.operations import blend, invert

white = RGB(255, 255, 255)
black = RGB(0, 0, 0)

blend(white, black).rgb       # RGB(r=128, g=128, b=128)
blend(white, black, 0.2).rgb  # RGB(r=204, g=204, b=204)
blend(white, black, 0.8).rgb  # RGB(r=51, g=51, b=51)

invert(black).rgb             # RGB(r=255, g=255, b=255)
invert((255, 0, 0)).cmyk      # CMYK(c=0, m=100, y=100, k=0)
invert("ff0000").hex          # HEX(00ffff)
```

## Conversion
Convert any color space to any color space.

🔀 | RGB | HEX | CMYK | HSL | HSV
--- | --- | --- | --- | --- | ---
RGB | <!-- null --> | `hex_to_rgb` | `cmyk_to_rgb` | `hsl_to_rgb` | `hsv_to_rgb`
HEX | `rgb_to_hex` | <!-- null --> | `cmyk_to_hex` | `hsl_to_hex` | `hsv_to_hex`
CMYK | `rgb_to_cmyk` | `hex_to_cmyk` | <!-- null --> | `hsl_to_cmyk` | `hsv_to_cmyk`
HSL | `rgb_to_hsl` | `hex_to_hsl` | `cmyk_to_hsl` | <!-- null --> | `hsv_to_hsl`
HSV | `rgb_to_hsv` | `hex_to_hsv` | `cmyk_to_hsv` | `hsl_to_hsv` | <!-- null -->


**Example**

```python
from chromato import convert

convert.rgb_to_cmyk(255, 0, 0)  # CMYK(c=0, m=100, y=100, k=0)
convert.rgb_to_hex(255, 0, 0)   # HEX(ff0000)
convert.rgb_to_hex(255, 0, 0)   # HEX(ff0000)
convert.rgb_to_hsl(255, 0, 0)   # HSL(h=0, s=1, l=0.5)
convert.rgb_to_hsv(255, 0, 0)   # HSV(h=0, s=1, v=1)
```

## Parsing
Each parse function takes any kind of value and tries to parse it.

Function | Returns | Description
--- | --- | ---
**`parse_cmyk`**`(value)` | `tuple(c,m,y,k)` |  Parse value as CMYK 
**`parse_hex`**`(value)` | `str(hex)` |  Parse value as HEX
**`parse_hsl`**`(value)` | `tuple(h,l,s)` |  Parse value as HSL 
**`parse_hsv`**`(value)` | `tuple(h,s,v)` |  Parse value as HSV 
**`parse_rgb`**`(value)` | `tuple(r,g,b)` |  Parse value as RGB 

**Example**

```python
from chromato import parse
from chromato.spaces import Color, HEX, RGB

parse.parse_hex("f")                 # "ffffff"
parse.parse_hex("f60")               # "ff6600"
parse.parse_hex("ff6600")            # "ff6600"
parse.parse_hex(" #ff6600 ")         # "ff6600"
parse.parse_hex(333)                 # "333333"
parse.parse_hex(HEX("ff6600"))       # "ff6600"
parse.parse_hex(RGB(255, 102, 0))    # "ff6600"
parse.parse_hex(Color(255, 102, 0))  # "ff6600"
```

## Validation
Each validation function validates type and range. Returns `True`/`False`.

```python
from chromato import validation

validation.is_cmyk(c, m, y, k)
validation.is_hex(hex)
validation.is_hsl(h, s, l)
validation.is_hsv(h, s, v)
validation.is_rgb(r, g, b)
```

<br>

# Development [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Setup**

1. Install [poetry](https://github.com/python-poetry/poetry)
2. `poetry install`

**Tests**

Run tests on changes in source code or tests.

```shell
poetry run ptw --clear --runner "poetry run pytest --cov -vv" 
```

**Code formatting (black)**

```shell
poetry run black . 
```
