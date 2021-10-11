<div align="center">
    <h1>🍅 chromato</h1>
    <p>
        <b>Fresh color utilities for Python</b>
    </p>

<!--![test](https://github.com/vikpe/chromato/workflows/test/badge.svg?branch=master) [![codecov](https://codecov.io/gh/vikpe/chromato/branch/master/graph/badge.svg)](https://codecov.io/gh/vikpe/chromato)-->
    
<br>

</div>

* [**Color spaces**](#color-spaces): CMYK, HEX, RGB, HLS, HSV
* [**Color class**](#color-class): Convenience class for color manipulation
* [**Operations**](#operations): shade, tone, tint, grayscale, invert, complement, add, subtract, multiply
* [**Conversion**](#conversion): any color space to any color space
* [Parsing](#parsing) 
* [Validation](#validation)
* (zero dependecies!)

# Install

```shell
pip install chromato
```

# Example usage

**Color class**
```python
from chromato.spaces import Color

red = Color(255, 0, 0)

red.cmyk  # CMYK(c=0, m=100, y=100, k=0)
red.hex   # HEX(ff0000)
red.rgb   # RGB(r=255, g=0, b=0)
red.hls   # HLS(h=0, l=0.5, s=1)
red.hsv   # HSV(h=0, s=1, v=1)
```

**Operations**
```python
from chromato import operations
from chromato.spaces import Color

red = Color(255, 0, 0)
blue = Color(0, 0, 255)

operations.invert(red).rgb       # RGB(r=0, g=255, b=255)
operations.blend(red, blue).rgb  # RGB(r=128, g=0, b=128)
operations.tint(red, 0.1).rgb    # Color(r=255, g=26, b=26)
```

**Conversion**
```python
from chromato import convert

convert.rgb_to_hex(255, 0, 0)  # HEX(ff0000)
convert.hex_to_rgb("ff0000")   # RGB(r=255, g=0, b=0)
convert.hex_to_cmyk("f0f")     # CMYK(c=0, m=100.0, y=0, k=0)
```

**Parsing**
```python
from chromato import parse
from chromato.spaces import Color, HEX, RGB

parse.parse_hex("f")                 # HEX(ffffff)
parse.parse_hex("f60")               # HEX(ff6600)
parse.parse_hex("ff6600")            # HEX(ff6600)
parse.parse_hex(" #ff6600 ")         # HEX(ff6600)
parse.parse_hex(333)                 # HEX(333333)
parse.parse_hex(HEX("ff6600"))       # HEX(ff6600)
parse.parse_hex(RGB(255, 102, 0))    # HEX(ff6600)
parse.parse_hex(Color(255, 102, 0))  # HEX(ff6600)
```

# API

## Color spaces

Name | Properties | Range
---|---|---
CMYK | `c`, `m`, `y`, `k` | `0-100`, `0-100`, `0-100`, `0-100`
HEX | (is a string) | `000000-ffffff`
HLS | `h`, `l`, `s` |  `0-1`, `0-1`, `0-1`
HSV | `h`, `s`, `v` |  `0-1`, `0-1`, `0-1`
RGB | `r`, `g`, `b` | `0-255`, `0-255`, `0-255`


```python
from chromato.spaces import CMYK, HEX, HLS, HSV, RGB

red_cmyk = CMYK(0, 100, 100, 0)
red_hex  = HEX("ff0000")
red_hls  = HLS(0, 0.5, 1)
red_hsv  = HSV(0, 1, 1)
red_rgb  = RGB(255, 0, 0)
```

## Color class

**Properties**
```python
from chromato.spaces import Color

red = Color(255, 0, 0)

red.cmyk  # CMYK(0, 100, 100, 0)
red.hex   # HEX(ff0000)
red.hls   # HLS(0, 0.5, 1)
red.hsv   # HSV(0, 1, 1)
red.rgb   # RGB(255, 0, 0)
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
Color(HLS(0, 0.5, 1))
Color(CMYK(0, 100, 100, 0))
```

## Operations

### Blend

Blend/mix colors

```python
blend(color1: Color, color2: Color, factor: float = 0.5) -> Color
```

**Examples**

```python
white = Color(255, 255, 255)
black = Color(0, 0, 0)

blend(white, black).rgb       # Color(r=128, g=128, b=128)
blend(white, black, 0.2).rgb  # Color(r=204, g=204, b=204)
blend(white, black, 0.8).rgb  # Color(r=51, g=51, b=51)
```

---

### Tint

Increase lightness (blend with white)

```python
tint(color: Color, factor: float) -> Color
```

**Example**

```python
tint(Color(255, 0, 0), 0.5).rgb  # Color(r=255, g=128, b=128)
```

---

### Shade

Increase darkness (blend with black)

```python
shade(color: Color, factor: float) -> Color
```

**Example**

```python
shade(Color(255, 0, 0), 0.5).rgb  # Color(r=128, g=0, b=0)
```

---

### Tone

Reduce colorfullness (blend with gray)

```python
tone(color: Color, factor: float) -> Color
```

**Example**

```python
tone(Color(255, 0, 0), 0.5).rgb  # Color(r=192, g=64, b=64)
```

---

### Invert

Invert color

```python
invert(color: Color) -> Color
```

**Example**

```python
invert(Color(255, 0, 0)).rgb  # Color(r=0, g=255, b=255) 
```

---

### Complement

Complementary color

```python
complementary(c: Color) -> Color
```

**Example**

```python
complement(Color(255, 0, 0))  # Color(r=0, g=255, b=255)
```

---

### Add

Add colors

```python
add(c1: Color, c2: Color) -> Color
```

**Example**

```python
add(Color(255, 0, 0), Color(0, 0, 255)).rgb  # Color(r=255, g=0, b=255) 
```

---

### Subtract

Subtract colors

```python
subtract(c1: Color, c2: Color) -> Color
```

**Example**

```python
subtract(Color(255, 0, 255), Color(0, 0, 255)).rgb  # Color(r=255, g=0, b=0)
```

---

### Multiply

Multiply colors

```python
multiply(c1: Color, c2: Color) -> Color
```

**Example**

```python
multiply(RGB(255, 0, 255), RGB(0, 0, 255)).rgb  # Color(r=0, g=0, b=255)
```

## Conversion

🔀 | RGB | HEX | CMYK | HLS | HSV
--- | --- | --- | --- | --- | ---
RGB | <!-- null --> | `hex_to_rgb` | `cmyk_to_rgb` | `hls_to_rgb` | `hsv_to_rgb`
HEX | `rgb_to_hex` | <!-- null --> | `cmyk_to_hex` | `hls_to_hex` | `hsv_to_hex`
CMYK | `rgb_to_cmyk` | `hex_to_cmyk` | <!-- null --> | `hls_to_cmyk` | `hsv_to_cmyk`
HLS | `rgb_to_hls` | `hex_to_hls` | `cmyk_to_hls` | <!-- null --> | `hsv_to_hls`
HSV | `rgb_to_hsv` | `hex_to_hsv` | `cmyk_to_hsv` | `hls_to_hsv` | <!-- null -->

```python
from chromato import convert

convert.rgb_to_hex(255, 255, 0)   # HEX(ff0000)
convert.rgb_to_cmyk(255, 255, 0)  # CMYK(0, 100, 100, 0)
convert.rgb_to_hex(255, 255, 0)   # HEX(ff0000)
convert.rgb_to_hls(255, 255, 0)   # HLS(0, 0.5, 1)
convert.rgb_to_hsv(255, 255, 0)   # HSV(0, 1, 1)
```

## Parsing
Each parse function takes any kind of value and tries to parse it.

```python
from chromato import parse

parse.parse_cmyk(value)  # (c, m, y, k)
parse.parse_hex(value)   # "hex"
parse.parse_hls(value)   # (h, l, s)
parse.parse_hsv(value)   # (h, s, v)
parse.parse_rgb(value)   # (r, g, b)
```

## Validation
Each validation function validates type and range. Returns `True`/`False`.

```python
from chromato import validation

validation.is_cmyk(c, m, y, k)
validation.is_hex(hex)
validation.is_hls(h, l, s)
validation.is_hsv(h, s, v)
validation.is_rgb(r, g, b)
```

# Development

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Setup

1. Install [poetry](https://github.com/python-poetry/poetry)
2. `poetry install`

## Tests

Run tests on changes in source code or tests.

```shell
poetry run ptw --clear --runner "poetry run pytest --cov -vv" 
```

## Code formatting (black)

```shell
poetry run black . 
```
