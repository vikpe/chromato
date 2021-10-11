def lerp(v1: float, v2: float, factor: float) -> float:
    return v1 + ((v2 - v1) * factor)


def dict_has_keys(_dict: dict, keys: iter) -> bool:
    return all(k in _dict for k in keys)
