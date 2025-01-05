from typing import Optional

import pygame

from ._utils.constants import PRESS_LEFT
from ._utils.decorators import ElementInterface
from ._utils.events import ElementEvent
from ._utils.tools import boundary
from ._utils.unions import DictParam, Flag, Number

class Scroller(ElementInterface):

    def __init__(

        self,
        clock: Optional[pygame.time.Clock] = None,
        scroll: DictParam = {},
        speed: DictParam = {},
        axis: DictParam = {},
        reversed: DictParam = {},
        only_press: Flag = PRESS_LEFT

    ) -> None:

        super().__init__(Scroller, ['clock'])

        self.event = ElementEvent(self)

        if clock is None:
            self.clock = pygame.time.Clock()
        else:
            self.clock = clock

        self.scroll = scroll
        self.speed = speed
        self.axis = axis
        self.reversed = reversed
        self.only_press = only_press

        self._scroll_speed_x = 0
        self._scroll_speed_y = 0
        self._stopped_time = 0
        self._last_updated = 0
        self._last_mouse_pos = (0, 0)
        self._rscrolling = False
        self._pressed = False
        self._initial_anchor_drag_state = False

        self.update_cache()

        if initial_offset := scroll.get('offset', None):
            self.offset = initial_offset

    @property
    def offset(self) -> tuple[Number, Number]:
        return (self.event.offset_x, self.event.offset_y)

    @offset.setter
    def offset(self, new: tuple[Number, Number]) -> None:
        (min_x_scroll, max_x_scroll), (min_y_scroll, max_y_scroll) = self._cache['scroll.min-max-xy']
        self.event.offset_x = boundary(new[0], min_x_scroll, max_x_scroll)
        self.event.offset_y = boundary(new[1], min_y_scroll, max_y_scroll)

    def update_cache(self) -> None:
        self._cache.clear()

        self._cache['scroll.min-max-xy'] = min_max_offset = self.scroll.get('min-max-xy', None)
        if min_max_offset is None:
            self._cache['scroll.min-max-xy'] = (self.scroll['min-xy'], self.scroll['max-xy'])
        self._cache['scroll.stop-threshold'] = self.scroll.get('stop-threshold', 500)
        self._cache['scroll.inertia'] = self.scroll.get('inertia', True)
        self._cache['scroll.momentum'] = self.scroll.get('momentum', 0.9)

        self._cache['speed.scroll'] = self.speed.get('scroll', 25)
        self._cache['speed.update'] = self.speed.get('update', 16)
        self._cache['speed.keyboard'] = self.speed.get('keyboard', 15)

        self._cache['axis.scroll'] = self.axis.get('scroll', 'y')
        self._cache['axis.keyboard'] = self.axis.get('keyboard', 'xy')

        self._cache['reversed.scroll'] = self.reversed.get('scroll', False)
        self._cache['reversed.keyboard'] = self.reversed.get('keyboard', False)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == self.only_press:
                self.event.dragging = True

                self._last_mouse_pos = pygame.mouse.get_pos()
                self._scroll_speed_x = 0
                self._scroll_speed_y = 0
                self._stopped_time = 0

            elif (mouse_scroll_speed := self._cache['speed.scroll']) is not None and not (self.event.anchor_scroll or self.event.anchor):
                up, down = (5, 4) if self._cache['reversed.scroll'] else (4, 5)
                axis_scroll = self._cache['axis.scroll']

                if event.button == up:
                    self.event.scrolling = True
                    if 'x' in axis_scroll:
                        self.event.offset_x += mouse_scroll_speed
                    if 'y' in axis_scroll:
                        self.event.offset_y += mouse_scroll_speed

                elif event.button == down:
                    self.event.scrolling = True
                    if 'x' in axis_scroll:
                        self.event.offset_x -= mouse_scroll_speed
                    if 'y' in axis_scroll:
                        self.event.offset_y -= mouse_scroll_speed

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == self.only_press:
                self.event.dragging = False
                if self._stopped_time >= self._cache['scroll.stop-threshold']:
                    self._scroll_speed_x = 0
                    self._scroll_speed_y = 0

    def update(self) -> ElementEvent:
        current_time = pygame.time.get_ticks()

        if current_time - self._last_updated >= self._cache['speed.update']:
            self._last_updated = current_time
            mouse_pressed = pygame.mouse.get_pressed()[self.only_press - 1]

            self.event.inertia = False

            if mouse_pressed and not self._pressed:
                self._initial_anchor_drag_state = self.event.anchor_drag or self.event.anchor
                self._pressed = True
            elif not mouse_pressed and self._pressed:
                self._pressed = False

            if (self.event.anchor_drag or self.event.anchor) and self._initial_anchor_drag_state:
                self.event.dragging = False

            if self.event.dragging:
                mouse_pos = pygame.mouse.get_pos()
                dx, dy = mouse_pos[0] - self._last_mouse_pos[0], mouse_pos[1] - self._last_mouse_pos[1]

                self._scroll_speed_x = dx
                self._scroll_speed_y = dy
                self._last_mouse_pos = mouse_pos

                if dx == 0 and dy == 0:
                    self._stopped_time += self.clock.get_time()
                else:
                    self._stopped_time = 0

            elif self._cache['scroll.inertia']:
                momentum = self._cache['scroll.momentum']

                self._scroll_speed_x *= momentum
                self._scroll_speed_y *= momentum

                if abs(self._scroll_speed_x) < 0.1 and abs(self._scroll_speed_y) < 0.1:
                    self._scroll_speed_x = 0
                    self._scroll_speed_y = 0
                else:
                    self.event.inertia = True

            else:
                self._scroll_speed_x = 0
                self._scroll_speed_y = 0

            if (keyboard_speed := self._cache['speed.keyboard']) is not None and not (self.event.anchor_keyboard or self.event.anchor):
                keyboard_press = pygame.key.get_pressed()
                axis_keyboard = self._cache['axis.keyboard']

                self.event.keyboard_scrolling = False

                if self._cache['reversed.keyboard']:

                    if 'x' in axis_keyboard:
                        if keyboard_press[pygame.K_LEFT]:
                            self.event.offset_x += keyboard_speed
                            self.event.keyboard_scrolling = True
                        elif keyboard_press[pygame.K_RIGHT]:
                            self.event.offset_x -= keyboard_speed
                            self.event.keyboard_scrolling = True

                    if 'y' in axis_keyboard:
                        if keyboard_press[pygame.K_UP]:
                            self.event.offset_y += keyboard_speed
                            self.event.keyboard_scrolling = True
                        elif keyboard_press[pygame.K_DOWN]:
                            self.event.offset_y -= keyboard_speed
                            self.event.keyboard_scrolling = True

                else:

                    if 'x' in axis_keyboard:
                        if keyboard_press[pygame.K_LEFT]:
                            self.event.offset_x -= keyboard_speed
                            self.event.keyboard_scrolling = True
                        elif keyboard_press[pygame.K_RIGHT]:
                            self.event.offset_x += keyboard_speed
                            self.event.keyboard_scrolling = True

                    if 'y' in axis_keyboard:
                        if keyboard_press[pygame.K_UP]:
                            self.event.offset_y -= keyboard_speed
                            self.event.keyboard_scrolling = True
                        elif keyboard_press[pygame.K_DOWN]:
                            self.event.offset_y += keyboard_speed
                            self.event.keyboard_scrolling = True

            self.event.offset_x += self._scroll_speed_x
            self.event.offset_y += self._scroll_speed_y

            if self._rscrolling:
                self._rscrolling = False
                self.event.scrolling = False
            elif self.event.scrolling:
                self._rscrolling = True

            self.offset = (self.event.offset_x, self.event.offset_y)

            self.event._send_event()

        return self.event

    def apply(self, screen_surface: pygame.Surface, surface: pygame.Surface) -> None:
        screen_surface.blit(surface, self.offset)

class ScrollerX(Scroller):

    def __init__(

        self,
        clock: Optional[pygame.time.Clock] = None,
        scroll: DictParam = {},
        speed: DictParam = {},
        reversed: DictParam = {},
        only_press: Flag = PRESS_LEFT

    ) -> None:

        super().__init__(
            clock=clock,
            scroll=scroll,
            speed=speed,
            axis={
                'scroll': 'x',
                'keyboard': 'x'
            },
            reversed=reversed,
            only_press=only_press,
        )

        self._child_class = ScrollerX

    @property
    def scroll(self) -> DictParam:
        return self._scroll

    @scroll.setter
    def scroll(self, new: DictParam) -> None:
        min_max_x = new.get('min-max-x', None)
        if min_max_x is None:
            min_max_x = (new['min-x'], new['max-x'])
        self._scroll = {
            'min-max-xy': (
                min_max_x,
                (new['y'], new['y'])
            ),
            **new
        }

class ScrollerY(Scroller):

    def __init__(

        self,
        clock: Optional[pygame.time.Clock] = None,
        scroll: DictParam = {},
        speed: DictParam = {},
        reversed: DictParam = {},
        only_press: Flag = PRESS_LEFT

    ) -> None:

        super().__init__(
            clock=clock,
            scroll=scroll,
            speed=speed,
            axis={
                'scroll': 'y',
                'keyboard': 'y'
            },
            reversed=reversed,
            only_press=only_press
        )

        self._child_class = ScrollerY

    @property
    def scroll(self) -> DictParam:
        return self._scroll

    @scroll.setter
    def scroll(self, new: DictParam) -> None:
        min_max_y = new.get('min-max-y', None)
        if min_max_y is None:
            min_max_y = (new['min-y'], new['max-y'])
        self._scroll = {
            'min-max-xy': (
                (new['x'], new['x']),
                min_max_y
            ),
            **new
        }

__all__ = [
    'Scroller',
    'ScrollerX',
    'ScrollerY'
]