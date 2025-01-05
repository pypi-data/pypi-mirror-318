from pygame.event import custom_type

DEFAULT = 0

ELEMENT_INACTIVE = 1
ELEMENT_HOVER = 2
ELEMENT_ACTIVE = 3

PRESS_LEFT = 1
PRESS_MIDDLE = 2
PRESS_RIGHT = 3
PRESS_SCROLL = 4

BUTTON = custom_type()
RANGE = custom_type()
SCROLLER = custom_type()

__all__ = [
    'DEFAULT',
    'ELEMENT_INACTIVE',
    'ELEMENT_HOVER',
    'ELEMENT_ACTIVE',
    'PRESS_LEFT',
    'PRESS_MIDDLE',
    'PRESS_RIGHT',
    'PRESS_SCROLL',
    'BUTTON',
    'RANGE',
    'SCROLLER',
]