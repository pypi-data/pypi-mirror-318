from typing import Any
from re import match

import pygame

from .unions import DictParam, Exceptions, Flag, Number
from .constants import PRESS_LEFT, PRESS_MIDDLE, PRESS_RIGHT

def asserter(

    condition: bool,
    exception: Exceptions | str,
    from_exception: Exceptions | None = None

) -> None:

    if not condition:

        if from_exception is not None:
            if isinstance(exception, str):
                raise AssertionError(exception) from from_exception
            raise exception from from_exception

        if isinstance(exception, str):
            raise AssertionError(exception)

        raise exception

def name(obj: Any) -> str:
    return obj.__class__.__name__

def isvalidname(name: str) -> bool:
    return bool(match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name))

def isprivate(self: object, name: str) -> bool:
    return name.startswith('__') or name.startswith(f'_{self.__class__.__name__}__')

def strip2underscore(name: str) -> str:
    return name.replace('-', '_')

def merge_deep(dict1: dict, dict2: dict, deep: int = -1) -> dict:
    if deep == 0:
        return dict1.copy()

    merge = {}
    for key, value in dict2.items():
        if isinstance(dict1.get(key, None), dict) and isinstance(value, dict):
            merge[key] = merge_deep(dict1[key], value, deep - 1)
        else:
            merge[key] = value

    return dict1 | merge

def floor_value(value: Number, step: Number) -> Number:
    rest = value % step
    if rest < step / 2:
        return value - rest
    return value + (step - rest)

def boundary(value: Number, nmin: Number, nmax: Number) -> Number:
    return min(nmax, max(nmin, value))

def rect_center(rect: pygame.Rect) -> DictParam:
    return {'center': rect.center}

def mouse_pressed(only_press: list[Flag] | tuple[Flag]) -> tuple[bool, bool, bool]:
    pressed = pygame.mouse.get_pressed()
    return (
        pressed[0] if PRESS_LEFT in only_press else False,
        pressed[1] if PRESS_MIDDLE in only_press else False,
        pressed[2] if PRESS_RIGHT in only_press else False
    )

__all__ = [
    'asserter',
    'name',
    'floor_value',
    'boundary',
    'rect_center',
    'mouse_pressed'
]