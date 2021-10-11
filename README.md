<div align="center">
    <h1>🍅 chromato</h1>
    <p>
        <b>Fresh color utilities for Python</b>
    </p>

<!--![test](https://github.com/vikpe/chromato/workflows/test/badge.svg?branch=master) [![codecov](https://codecov.io/gh/vikpe/chromato/branch/master/graph/badge.svg)](https://codecov.io/gh/vikpe/chromato)-->
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</div>

# Features

* Color spaces
* Operations
* Convert
* Parse
* Validation
* Zero dependecies

# Install

```shell
pip install chromato
```

# Usage

TODO

# API

## Color spaces

### Overview

Name | Scale
---|---
CMYK | (c,m,y,k) 0 - 100
HEX | 000000 - ffffff
HLS | (h,l,s) 0 - 1
HSV | (h,s,v) 0 - 1
RGB | (r,g,b) 0 - 255

### CMYK

> c [0-100] m [0-100] y [0-100] k [0-100]

```python
from chromato import spaces

spaces.CMYK()
spaces.HEX()
spaces.HLS()
spaces.HSV()
spaces.RGB()
```

## Color

```python
from chromato import spaces

red = spaces.Color(255, 0, 0)

red.cmyk  # CMYK(0, 100, 100, 0)
red.hex  # HEX(ff0000)
red.hls  # HLS((0, 0.5, 1)
red.hsv  # HSV(0, 1, 1)
red.rgb  # RGB(255, 0, 0)
```

## Operations

### Blend

> Blend/mix colors

**Synopsis**

```python
blend(color1: Color, color2: Color, factor: float = 0.5) -> Color
```

**Example**

```python
blend((255, 255, 255), (0, 0, 0)).rgb  # (128, 128, 128)
```

---

### Tint

> Increase lightness (blend with white)

**Synopsis**

```python
tint(color: Color, factor: float) -> Color
```

**Example**

```python
tint(RGB(255, 0, 0), 0.5).rgb
```

---

### Shade

> Increase darkness (blend with black)

**Synopsis**

```python
shade(color: Color, factor: float) -> Color
```

**Example**

```python
shade(RGB(255, 0, 0), 0.5).rgb
```

---

### Tone

> Reduce colorfullness (blend with gray)

**Synopsis**

```python
tone(color: Color, factor: float) -> Color
```

**Example**

```python
tone(RGB(255, 0, 0), 0.5).rgb
```

---

### Invert

> Invert color

**Synopsis**

```python
invert(color: Color) -> Color
```

**Example**

```python
invert(RGB(255, 0, 0)).rgb  # (0, 255, 255) 
```

---

### Complement

> Complementary color

**Synopsis**

```python
complementary(c: Color) -> Color
```

**Example**

```python

```

---

### Add

> Add colors

**Synopsis**

```python
add(c1: Color, c2: Color) -> Color
```

**Example**

```python
add(RGB(255, 0, 0), RGB(0, 0, 255)).rgb  # (255, 0, 255) 
```

---

### Subtract

> Subtract colors

**Synopsis**

```python
subtract(c1: Color, c2: Color) -> Color
```

**Example**

```python
subtract(RGB(255, 0, 255), RGB(0, 0, 255)).rgb  # (255, 0, 0)
```

---

### Multiply

> Multiply colors

**Synopsis**

```python
multiply(c1: Color, c2: Color) -> Color
```

**Example**

```python
multiply(RGB(255, 0, 255), RGB(0, 0, 255)).rgb  # (0, 0, 255)
```

## Conversion

🔀 | RGB | HEX | CMYK | HLS | HSV
--- | --- | --- | --- | --- | ---
RGB | <!-- null --> | `hex_to_rgb` | `cmyk_to_rgb` | `hls_to_rgb` | `hsv_to_rgb`
HEX | `rgb_to_hex` | <!-- null --> | `cmyk_to_hex` | `hls_to_hex` | `hsv_to_hex`
CMYK | `rgb_to_cmyk` | `hex_to_cmyk` | <!-- null --> | `hls_to_cmyk` | `hsv_to_cmyk`
HLS | `rgb_to_hls` | `hex_to_hls` | `cmyk_to_hls` | <!-- null --> | `hsv_to_hls`
HSV | `rgb_to_hsv` | `hex_to_hsv` | `cmyk_to_hsv` | `hls_to_hsv` | <!-- null -->

## Parse

```python
from chromato import parse

parse.parse_cmyk()
parse.parse_hex()
parse.parse_hls()
parse.parse_hsv()
parse.parse_rgb()
```

## Validation

```python
from chromato import validation

validation.is_cmyk()
validation.is_hex()
validation.is_hls()
validation.is_hsv()
validation.is_rgb()
```
