from .constants import DEFAULT, BUTTON, RANGE, SCROLLER
from .unions import Element

from copy import deepcopy
from pygame.event import post, Event

class ElementEvent:

    def __init__(self, element: Element) -> None:

        self.element = element
        self.element_name = str(element)

        match self.element_name:

            case 'Button':
                self.interaction = DEFAULT
                self.press = DEFAULT
                self.hover = False
                self.cursor_active = False

            case 'Range':
                self.interaction = DEFAULT
                self.press = DEFAULT
                self.hover = False
                self.cursor_active = False
                self.dragging = False
                self.value = 0

            case 'Scroller' | 'ScrollerX' | 'ScrollerY':
                self.press = DEFAULT
                self.keyboard_scrolling = False
                self.scrolling = False
                self.dragging = False
                self.inertia = False
                self.anchor = False
                self.anchor_drag = False
                self.anchor_scroll = False
                self.anchor_keyboard = False
                self.offset_x = 0
                self.offset_y = 0

    def __copy__(self):
        return self.copy()

    def copy(self) -> 'ElementEvent':
        return deepcopy(self)

    def _reset(self) -> None:
        self.__init__(self.element)

    def _send_event(self) -> None:
        match self.element_name:

            case 'Button':
                event = Event(
                    BUTTON,
                    element=self.element,
                    interaction=self.interaction,
                    press=self.press,
                    hover=self.hover,
                    cursor_active=self.cursor_active
                )

            case 'Range':
                event = Event(
                    RANGE,
                    element=self.element,
                    interaction=self.interaction,
                    press=self.press,
                    hover=self.hover,
                    cursor_active=self.cursor_active,
                    dragging=self.dragging,
                    value=self.value
                )

            case 'Scroller' | 'ScrollerX' | 'ScrollerY':
                event = Event(
                    SCROLLER,
                    element=self.element,
                    press=self.press,
                    keyboard_scrolling=self.keyboard_scrolling,
                    scrolling=self.scrolling,
                    dragging=self.dragging,
                    inertia=self.inertia,
                    anchor=self.anchor,
                    anchor_drag=self.anchor_drag,
                    anchor_scroll=self.anchor_scroll,
                    anchor_keyboard=self.anchor_keyboard,
                    offset_x=self.offset_x,
                    offset_y=self.offset_y,
                    offset=(self.offset_x, self.offset_y)
                )

        post(event)

__all__ = [
    'ElementEvent'
]