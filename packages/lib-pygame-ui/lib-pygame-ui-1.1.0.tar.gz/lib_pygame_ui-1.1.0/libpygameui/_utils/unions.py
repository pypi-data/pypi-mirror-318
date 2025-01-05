from typing import TYPE_CHECKING, Any, Union, Literal

import pygame

if TYPE_CHECKING:
    from .decorators import ElementInterface

Exceptions = Exception | BaseException
Number = int | float

Flag = int
Element = Union['ElementInterface']
DictParam = dict[str, Any]
WrapMethod = Literal['word', 'mono']
TextAlignment = Literal['left', 'center', 'right', 'fill']

ColorValue = tuple[int] | list[int] | str | pygame.Color
CursorValue = pygame.Cursor | int

__all__ = [
    'Exceptions',
    'Number',
    'Flag',
    'Element',
    'DictParam',
    'WrapMethod',
    'TextAlignment',
    'ColorValue',
    'CursorValue',
]