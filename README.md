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

# Install

```shell
pip install chromato
```

# Usage

TODO

# API

## Color spaces

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

```python
blend()
shade()
tone()
tint()
grayscale()
invert()
complement()
add()
subtract()
```

## Conversion

🔀 | RGB | HEX | CMYK | HLS | HSV
---|---|---|---|---|---
RGB  | <!-- null --> | `hex_to_rgb`  | `cmyk_to_rgb` | `hls_to_rgb`  | `hsv_to_rgb`
HEX  | `rgb_to_hex`  | <!-- null --> | `cmyk_to_hex` | `hls_to_hex`  | `hsv_to_hex`
CMYK | `rgb_to_cmyk` | `hex_to_cmyk` | <!-- null --> | `hls_to_cmyk` | `hsv_to_cmyk`
HLS  | `rgb_to_hls`  | `hex_to_hls`  | `cmyk_to_hls` | <!-- null --> | `hsv_to_hls`
HSV  | `rgb_to_hsv`  | `hex_to_hsv`  | `cmyk_to_hsv` | `hls_to_hsv`  | <!-- null -->

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
