from typing import Optional
from copy import deepcopy

import pygame

from ._utils.constants import SCROLLER
from ._utils.decorators import ElementInterface
from ._utils.unions import CursorValue, DictParam, Element

def set_cursor_global(

        elements: list[Element],
        inactive: Optional[CursorValue] = None,
        active: Optional[CursorValue] = None,
        set_active: bool = True

    ) -> None:

    any_pressed = False

    for element in elements:

        if hasattr(element, 'cursor'):
            if set_active:
                element.cursor['active'] = active
            element.cursor['inactive'] = None

        if str(element) in ('Button', 'Range') and element.event.cursor_active and not any_pressed:
            any_pressed = True

    if inactive is not None and not any_pressed:
        pygame.mouse.set_cursor(inactive)

class Manager(ElementInterface):

    def __init__(

        self,
        elements: list[Element] = [],
        with_logic: bool = False,
        cursor_global_param: DictParam = {}

    ) -> None:

        super().__init__(Manager, ['elements'])

        self.elements = elements
        self.with_logic = with_logic
        self.cursor_global_param = cursor_global_param

    def __deepcopy__(self, memo: dict):
        new = super().copy()
        new.elements = deepcopy(self.elements)
        return new

    def copy(self) -> 'Manager':
        new = super().copy()
        new.elements = self.elements.copy()
        return new

    def add_element(self, element: Element) -> None:
        self.elements.append(element)

    def remove_element(self, element: Element) -> None:
        self.elements.remove(element)

    def clear_element(self) -> None:
        self.elements.clear()

    def has_element(self, element: Element) -> bool:
        return element in self.elements

    def update_cache(self) -> None:
        for element in self.elements:
            element.update_cache()

    def handle_event(self, event: pygame.event.Event) -> None:
        for element in self.elements:

            if self.with_logic:
                element_name = str(element)

                if element_name == 'Button':
                    element.with_event = True

                if element_name == 'Range':
                    element.drag_middle_mouse = False

                if event.type == SCROLLER:
                    if element_name == 'Range':
                        element.with_event = element._button_track.with_event = event.dragging

            element.handle_event(event)

    def update(self) -> None:
        set_cursor_global(self.elements, **self.cursor_global_param)
        for element in self.elements:
            element.update()

    def draw_and_update(self) -> None:
        set_cursor_global(self.elements, **self.cursor_global_param)
        for element in self.elements:
            if hasattr(element, 'draw_and_update'):
                element.draw_and_update()
            else:
                element.update()

    def draw_inactive(self) -> None:
        for element in self.elements:
            if hasattr(element, 'draw_inactive'):
                element.draw_inactive()

    def draw_hover(self) -> None:
        for element in self.elements:
            if hasattr(element, 'draw_hover'):
                element.draw_hover()

    def draw_active(self) -> None:
        for element in self.elements:
            if hasattr(element, 'draw_active'):
                element.draw_active()

__all__ = [
    'set_cursor_global',
    'Manager'
]