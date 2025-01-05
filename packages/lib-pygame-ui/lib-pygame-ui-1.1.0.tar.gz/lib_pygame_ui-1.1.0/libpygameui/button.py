from typing import Self

import pygame

from ._utils import constants
from ._utils.constants import (
    DEFAULT, ELEMENT_ACTIVE, ELEMENT_HOVER, ELEMENT_INACTIVE, PRESS_LEFT, PRESS_LEFT,
    PRESS_MIDDLE, PRESS_RIGHT, PRESS_SCROLL
)
from ._utils.decorators import ElementInterface
from ._utils.events import ElementEvent
from ._utils.tools import asserter, boundary, mouse_pressed, rect_center, strip2underscore
from ._utils.unions import DictParam, Flag, Number
from .wrap import render_wrap

class Button(ElementInterface):

    def __init__(

        self,
        surface: pygame.Surface,
        rect: pygame.Rect,
        text: DictParam = {},
        outline: DictParam = {},
        image: DictParam = {},
        color: DictParam = {},
        cursor: DictParam = {},
        border: DictParam = {},
        with_event: bool = True,
        hide: bool = False,
        alpha: int = 255,
        only_press: list[Flag] = [PRESS_LEFT],
        press_speed: int = 50

    ) -> None:

        super().__init__(Button, 'surface')

        self.event = ElementEvent(self)

        self.surface = surface
        self.rect = rect
        self.text = text
        self.outline = outline
        self.image = image
        self.color = color
        self.cursor = cursor
        self.border = border
        self.with_event = with_event
        self.hide = hide
        self.alpha = alpha
        self.only_press = only_press
        self.press_speed = press_speed

        self._send_event = True
        self._pressed = False
        self._last_pressed_time = 0
        self._initial_pressed_state = DEFAULT

        self.update_cache()

    def _render_and_draw(self, interaction: Flag) -> None:
        if self.isinside():
            rect = self.rect
            button_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
            surf_rect = button_surface.get_rect()

            text = self._cache['text.text']
            font = self._cache['text.font']
            outline_size = self._cache['outline.size']
            image = self._cache['image.surface']
            rect_border_kw = self._cache['border@rect-border']

            size_with_outline = (rect.width - outline_size * 2, rect.height - outline_size * 2)
            with_outline = outline_size > 0

            match interaction:

                case constants.ELEMENT_INACTIVE:
                    text_color = self._cache['text.inactive-color']
                    text_background_color = self._cache['text.bg-inactive-color']
                    outline_color = self._cache['outline.inactive-color']
                    color = self._cache['color.inactive']

                case constants.ELEMENT_HOVER:
                    text_color = self._cache['text.hover-color']
                    text_background_color = self._cache['text.bg-hover-color']
                    outline_color = self._cache['outline.hover-color']
                    color = self._cache['color.hover']

                case constants.ELEMENT_ACTIVE:
                    text_color = self._cache['text.active-color']
                    text_background_color = self._cache['text.bg-active-color']
                    outline_color = self._cache['outline.active-color']
                    color = self._cache['color.active']

            if not self.hide:
                if with_outline:
                    # outline
                    rect_outline_border_kw = {key: value + outline_size for key, value in rect_border_kw.items()}
                    pygame.draw.rect(button_surface, outline_color, surf_rect, **rect_outline_border_kw)

                    # main area
                    pygame.draw.rect(button_surface, color, (((rect.width - size_with_outline[0]) / 2,
                                                              (rect.height - size_with_outline[1]) / 2),
                                                             size_with_outline), **rect_border_kw)
                else:
                    # main area
                    pygame.draw.rect(button_surface, color, surf_rect, **rect_border_kw)

            if image is not None:
                image_position = self._cache['image.position']
                if isinstance(image_position, dict):
                    button_surface.blit(image, image.get_rect(**image_position))
                else:
                    button_surface.blit(image, image.get_rect(**image_position(surf_rect)))

            if text:
                text_antialias = self._cache['text.antialias']
                text_position = self._cache['text.position']

                if isinstance(self._cache['text.wrap'], dict):
                    kw_width = self._cache['text.wrap.width']
                    if kw_width is None:
                        kw_width = rect.width
                    is_area = kw_width == 'area'
                    wrap_width = rect.width if is_area else kw_width
                    if is_area and with_outline:
                        wrap_width = size_with_outline[0]

                    text_surface = render_wrap(
                        font,
                        text,
                        wrap_width,
                        text_antialias,
                        text_color,
                        text_background_color,
                        self._cache['text.wrap.line-gap'],
                        self._cache['text.wrap.tab-size'],
                        self._cache['text.wrap.alignment'],
                        self._cache['text.wrap.method']
                    )
                else:
                    text_surface = font.render(text, text_antialias, text_color, text_background_color)

                if isinstance(text_position, dict):
                    button_surface.blit(text_surface, text_surface.get_rect(**text_position))
                else:
                    button_surface.blit(text_surface, text_surface.get_rect(**text_position(surf_rect)))

            button_surface.set_alpha(self.alpha)

            self.surface.blit(button_surface, self.rect)

    def isinside(self) -> bool:
        return self.surface.get_rect().colliderect(self.rect)

    def update_cache(self) -> None:
        self._cache.clear()

        self._cache['text.text'] = str(self.text.get('text', ''))
        self._cache['text.font'] = font = self.text.get('font', pygame.font.SysFont('arial', 20))
        if isinstance(font, dict):
            if font.get('from', 'sys') == 'path':
                self._cache['text.font'] = pygame.font.Font(font['path'], font['size'])
            else:
                self._cache['text.font'] = pygame.font.SysFont(font['name'], font['size'], font.get('bold', False), font.get('italic', False))
        self._cache['text.inactive-color'] = self.text.get('inactive-color', self.color.get('text-inactive-color', self.text.get('color', '#000000')))
        self._cache['text.hover-color'] = self.text.get('hover-color', self.color.get('text-hover-color', self.text.get('color', '#000000')))
        self._cache['text.active-color'] = self.text.get('active-color', self.color.get('text-active-color', self.text.get('color', '#ffffff')))
        self._cache['text.bg-inactive-color'] = self.text.get('bg-inactive-color', self.color.get('text-bg-inactive-color', None))
        self._cache['text.bg-hover-color'] = self.text.get('bg-hover-color', self.color.get('text-bg-hover-color', None))
        self._cache['text.bg-active-color'] = self.text.get('bg-active-color', self.color.get('text-bg-active-color', None))
        self._cache['text.antialias'] = self.text.get('antialias', True)
        self._cache['text.position'] = self.text.get('position', rect_center)
        self._cache['text.wrap'] = text_wrapped = self.text.get('wrap', False)
        if text_wrapped is True:
            self._cache['text.wrap'] = text_wrapped = {}
        elif not isinstance(text_wrapped, dict):
            text_wrapped = {}
        self._cache['text.wrap.width'] = text_wrapped.get('width', None)
        self._cache['text.wrap.line-gap'] = text_wrapped.get('line-gap', 0)
        self._cache['text.wrap.tab-size'] = text_wrapped.get('tab-size', 4)
        self._cache['text.wrap.alignment'] = text_wrapped.get('alignment', 'center')
        self._cache['text.wrap.method'] = text_wrapped.get('method', 'word')

        self._cache['outline.size'] = self.outline.get('size', 0)
        self._cache['outline.inactive-color'] = self.outline.get('inactive-color', self.color.get('outline-inactive-color', self.outline.get('color', '#3d3d3d')))
        self._cache['outline.hover-color'] = self.outline.get('hover-color', self.color.get('outline-hover-color', self.outline.get('color', '#3d3d3d')))
        self._cache['outline.active-color'] = self.outline.get('active-color', self.color.get('outline-active-color', self.outline.get('color', '#3d3d3d')))

        self._cache['image.surface'] = image = self.image.get('surface', None)
        if (resize := self.image.get('resize', None)) is not None and image is not None:
            self._cache['image.surface'] = pygame.transform.scale(image, resize)
        self._cache['image.position'] = self.image.get('position', rect_center)

        self._cache['color.inactive'] = self.color.get('inactive', self.color.get('color', '#ffffff'))
        self._cache['color.hover'] = self.color.get('hover', self.color.get('color', '#ebebeb'))
        self._cache['color.active'] = self.color.get('active', self.color.get('color', '#d6d6d6'))

        self._cache['cursor.inactive'] = self.cursor.get('inactive', None)
        self._cache['cursor.active'] = self.cursor.get('active', None)

        self._cache['border@rect-border'] = {'border_' + strip2underscore(kw): value for kw, value in self.border.items()}

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and self.with_event:

            self._initial_pressed_state = DEFAULT
            self._pressed = False

            if event.button == 1 and self.event.hover and PRESS_LEFT in self.only_press:
                self._initial_pressed_state = PRESS_LEFT
                self._pressed = True
            elif event.button == 2 and self.event.hover and PRESS_MIDDLE in self.only_press:
                self._initial_pressed_state = PRESS_MIDDLE
                self._pressed = True
            elif event.button == 3 and self.event.hover and PRESS_RIGHT in self.only_press:
                self._initial_pressed_state = PRESS_RIGHT
                self._pressed = True

    def update(self) -> ElementEvent:
        mouse_pos = pygame.mouse.get_pos()
        is_hover = self.rect.collidepoint(mouse_pos)

        self.event.press = DEFAULT
        self.event.interaction = ELEMENT_INACTIVE
        self.event.hover = is_hover
        self.event.cursor_active = False

        if self.isinside():
            current_time = pygame.time.get_ticks()
            get_pressed = mouse_pressed(self.only_press)
            any_pressed = get_pressed[0] or get_pressed[1] or get_pressed[2]

            if (cursor := self._cache['cursor.active']) is not None and is_hover:
                self.event.cursor_active = True
                pygame.mouse.set_cursor(cursor)
            elif (cursor := self._cache['cursor.inactive']) is not None:
                pygame.mouse.set_cursor(cursor)

            if any_pressed and is_hover:
                self.event.interaction = ELEMENT_ACTIVE
            elif is_hover:
                self.event.interaction = ELEMENT_HOVER

            if not self.with_event and is_hover:
                if current_time - self._last_pressed_time > self.press_speed and any_pressed:
                    if get_pressed[0]:
                        press = PRESS_LEFT
                    elif get_pressed[1]:
                        press = PRESS_MIDDLE
                    elif get_pressed[2]:
                        press = PRESS_RIGHT
                    self._pressed = False
                    self._last_pressed_time = current_time
                    self.event.press = press

            elif self.with_event and is_hover:
                if self._pressed and any_pressed:
                    pass
                elif current_time - self._last_pressed_time > self.press_speed and self._pressed:
                    self._pressed = False
                    self._last_pressed_time = current_time
                    self.event.press = self._initial_pressed_state

            if not (is_hover or any_pressed):
                self._pressed = False

        if self._send_event:
            self.event._send_event()

        return self.event

    def draw_and_update(self) -> ElementEvent:
        self.update()
        self._render_and_draw(self.event.interaction)
        return self.event

    def draw_inactive(self) -> None:
        self._pressed = False
        self._render_and_draw(ELEMENT_INACTIVE)
        self.event._reset()

    def draw_hover(self) -> None:
        self._pressed = False
        self._render_and_draw(ELEMENT_HOVER)
        self.event._reset()

    def draw_active(self) -> None:
        self._pressed = False
        self._render_and_draw(ELEMENT_ACTIVE)
        self.event._reset()

class Range(ElementInterface):

    def __init__(

        self,
        surface: pygame.Surface,
        rect: pygame.Rect,
        outline: DictParam = {},
        color: DictParam = {},
        cursor: DictParam = {},
        border: DictParam = {},
        track: DictParam = {},
        track_fill: DictParam = {},
        thumb: DictParam = {},
        value: DictParam = {},
        hide: DictParam = {},
        alpha: DictParam = {},
        reversed: DictParam = {},
        horizontal: bool = True,
        drag_wheel_mouse: bool = True,
        with_event: bool = False,
        only_press: list[Flag] = [PRESS_LEFT],
        press_speed: int = 0

    ) -> None:

        super().__init__(Range, 'surface')

        self._button_track = Button(surface=surface, rect=rect)
        self._button_track_fill = self._button_track.copy()
        self._button_thumb = self._button_track.copy()

        self._button_track._send_event = False
        self._button_track_fill._send_event = False
        self._button_thumb._send_event = False

        self.event = ElementEvent(self)

        self.surface = surface
        self.outline = outline
        self.color = color
        self.cursor = cursor
        self.border = border
        self.track = track
        self.track_fill = track_fill
        self.thumb = thumb
        self.value = value
        self.hide = hide
        self.horizontal = horizontal
        self.reversed = reversed
        self.drag_wheel_mouse = drag_wheel_mouse
        self.with_event = with_event
        self.alpha = alpha
        self.only_press = only_press
        self.press_speed = press_speed

        self._pressed = False
        self._detected_scrolling_mouse = False
        self._last_pressed_time = 0

        self.update_cache()

        self.rect = rect

    @property
    def surface(self) -> pygame.Surface:
        return self._surface

    @property
    def rect(self) -> pygame.Rect:
        return self._rect

    @surface.setter
    def surface(self, new: pygame.Surface) -> None:
        self._surface = new
        self._button_track.surface = new
        self._button_track_fill.surface = new
        self._button_thumb.surface = new

    @rect.setter
    def rect(self, new: pygame.Rect) -> None:
        self._rect = new
        self._update_rect()

    def _snap_step(self) -> Number:
        min_value = self._cache['value.min']
        value = self._cache['value.value']
        step = self._cache['value.step']
        output = self._cache['value.output']

        rest = (value - min_value) % step

        if rest < step / 2:
            return output(value - rest)
        else:
            return output(value + (step - rest))

    def _update_rect(self, mouse_pos: tuple[int, int] | None = None) -> None:
        min_value = self._cache['value.min']
        max_value = self._cache['value.max']
        value = self._cache['value.value']
        step = self._cache['value.step']
        output = self._cache['value.output']
        thumb_size = self._cache['thumb.size']
        reversed = self._cache['reversed.element']

        use_thumb = self._cache['thumb.size'] is not None

        rect = self._button_track.rect = self._rect
        track_fill_rect = self._button_track_fill.rect
        thumb_rect = self._button_thumb.rect

        if step is not None:
            self.event.value = value = self._cache['value.value'] = self._snap_step()

        if mouse_pos is not None:
            xm, ym = mouse_pos
            if self.horizontal:
                relative_position = boundary((xm - rect.left) / rect.width, 0, 1)
            else:
                relative_position = boundary((ym - rect.top) / rect.height, 0, 1)

            self.event.value = value = self._cache['value.value'] = output(
                max_value - relative_position * (max_value - min_value)
                if reversed else
                min_value + relative_position * (max_value - min_value)
            )

            if step is not None:
                self.event.value = value = self._cache['value.value'] = self._snap_step()

        if self.horizontal:
            track_fill_rect.size = (((value - min_value) / (max_value - min_value)) * rect.width, rect.height)
            track_fill_rect.top = rect.top

            if reversed:
                track_fill_rect.left = rect.right - track_fill_rect.width
            else:
                track_fill_rect.left = rect.left

            if use_thumb:
                thumb_rect.size = thumb_size
                thumb_rect.top = rect.top + (rect.height - thumb_rect.height) / 2
                thumb_rect.left = (
                    track_fill_rect.left - thumb_rect.width / 2
                    if reversed else
                    track_fill_rect.right - thumb_rect.width / 2
                )
        else:
            track_fill_rect.size = (rect.width, ((value - min_value) / (max_value - min_value)) * rect.height)
            track_fill_rect.left = rect.left

            if reversed:
                track_fill_rect.top = rect.bottom - track_fill_rect.height
            else:
                track_fill_rect.top = rect.top

            if use_thumb:
                thumb_rect.size = thumb_size
                thumb_rect.left = rect.left + (rect.width - thumb_rect.width) / 2
                thumb_rect.top = (
                    track_fill_rect.top - thumb_rect.height / 2
                    if reversed else
                    track_fill_rect.bottom - thumb_rect.height / 2
                )

    def _render_and_draw(self, interaction: Flag, updated: bool = False) -> None:
        if self.isinside():

            use_thumb = self._cache['thumb.size'] is not None

            match interaction:

                case constants.ELEMENT_INACTIVE:
                    if updated:
                        self._button_track._render_and_draw(interaction)
                    else:
                        self._button_track.draw_inactive()
                    self._button_track_fill.draw_inactive()
                    if use_thumb:
                        self._button_thumb.draw_inactive()

                case constants.ELEMENT_HOVER:
                    if updated:
                        self._button_track._render_and_draw(interaction)
                    else:
                        self._button_track.draw_hover()
                    self._button_track_fill.draw_hover()
                    if use_thumb:
                        self._button_thumb.draw_hover()

                case constants.ELEMENT_ACTIVE:
                    if updated:
                        self._button_track._render_and_draw(interaction)
                    else:
                        self._button_track.draw_active()
                    self._button_track_fill.draw_active()
                    if use_thumb:
                        self._button_thumb.draw_active()

    def set_param(self, **kwargs) -> Self:
        super().set_param(**kwargs)
        self._update_rect()
        return self

    def update_cache(self) -> None:
        self._cache.clear()

        self._button_track.outline = self.outline.get('track', self.track.get('outline', {}))
        self._button_track_fill.outline = self.outline.get('track-fill', self.track_fill.get('outline', {}))
        self._button_thumb.outline = self.outline.get('thumb', self.thumb.get('outline', {}))

        self._button_track.color = self.color.get('track', self.track.get('color', {
            'inactive': '#4a4a4a',
            'hover': '#575757',
            'active': '#383838'
        }))
        self._button_track_fill.color = self.color.get('track-fill', self.track_fill.get('color', {
            'inactive': '#4f8fe3',
            'hover': '#76a5e3',
            'active': '#2e72c9'
        }))
        self._button_thumb.color = self.color.get('thumb', self.thumb.get('color', {}))

        self._cache['cursor.inactive'] = self.cursor.get('inactive', None)
        self._cache['cursor.active'] = self.cursor.get('active', None)
        self._cache['cursor.active-outside'] = self.cursor.get('active-outside', True)

        self._button_track.border = self.border.get('track', self.track.get('border', {
            'radius': 50
        }))
        self._button_track_fill.border = self.border.get('track-fill', self.track_fill.get('border', {
            'radius': 50
        }))
        self._button_thumb.border = self.border.get('thumb', self.thumb.get('border', {
            'radius': 100
        }))

        self._cache['thumb.size'] = self.thumb.get('size', None)

        self._cache['value.min'] = min_value = self.value.get('min', 0)
        self._cache['value.max'] = max_value = self.value.get('max', 100)
        self._cache['value.value'] = value = self.value.get('value', min_value)
        self._cache['value.step'] = step = self.value.get('step', None)
        self._cache['value.output'] = output = self.value.get('output', float)

        self._button_track.hide = self.hide.get('track', self.track.get('hide', False))
        self._button_track_fill.hide = self.hide.get('track-fill', self.track_fill.get('hide', False))
        self._button_thumb.hide = self.hide.get('thumb', self.thumb.get('hide', False))

        self._button_track.alpha = self.alpha.get('track', self.track.get('alpha', 255))
        self._button_track_fill.alpha = self.alpha.get('track-fill', self.track_fill.get('alpha', 255))
        self._button_thumb.alpha = self.alpha.get('thumb', self.thumb.get('alpha', 255))

        self._cache['reversed.element'] = self.reversed.get('element', False)
        self._cache['reversed.scroll'] = self.reversed.get('scroll', False)

        self._button_track.with_event = self.with_event
        self._button_track.only_press = self.only_press
        self._button_track.press_speed = self.press_speed

        self._button_track.update_cache()
        self._button_track_fill.update_cache()
        self._button_thumb.update_cache()

        asserter(
            isinstance(min_value, Number) and
            isinstance(max_value, Number) and
            isinstance(value, Number) and
            isinstance(step, Number | None) and
            output in (int, float),
            TypeError(
                "unexpected any values; min_value, max_value, value, step, output must be numbers, "
                "step can be None, and output must be integer or float callable"
            )
        )
        if step is None:
            condition_step = True
        else:
            condition_step = 0 < step <= (max_value - min_value)
        asserter(
            min_value < max_value and condition_step,
            ValueError(
                "unexpected any values"
            )
        )

        self._cache['value.value'] = boundary(
            output(value),
            min_value,
            max_value,
        )

    def set_value(self, value: Number) -> None:
        self.event.value = self._cache['value.value'] = boundary(
            self._cache['value.output'](value),
            self._cache['value.min'],
            self._cache['value.max']
        )
        self._update_rect()

    def isinside(self) -> bool:
        return (
            self._button_track.isinside() or
            self.surface.get_rect().colliderect(self._button_thumb.rect)
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        self._button_track.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN and self.drag_wheel_mouse:
            detected = False
            value = self._cache['value.value']
            step = self._cache['value.step']
            up, down = (5, 4) if self._cache['reversed.scroll'] else (4, 5)

            asserter(
                step is not None,
                TypeError('step must be set to use mouse wheel scrolling')
            )

            if event.button == up and self.event.hover:
                value += step
                detected = True
            elif event.button == down and self.event.hover:
                value -= step
                detected = True

            if detected:
                self._detected_scrolling_mouse = True

                self.event.press = PRESS_SCROLL
                self.event.dragging = True

                self.set_value(value)
                self.event._send_event()

    def update(self) -> ElementEvent:
        mouse_pos = pygame.mouse.get_pos()
        is_hover = self._rect.collidepoint(mouse_pos)

        if self._cache['thumb.size'] is not None:
            is_hover = is_hover or self._button_thumb.rect.collidepoint(mouse_pos)

        self.event.press = DEFAULT
        self.event.interaction = ELEMENT_INACTIVE
        self.event.hover = is_hover
        self.event.cursor_active = False

        if self.isinside():
            current_time = pygame.time.get_ticks()
            get_pressed = mouse_pressed(self.only_press)
            any_pressed = get_pressed[0] or get_pressed[1] or get_pressed[2]

            if not self._detected_scrolling_mouse:
                self.event.dragging = False

            if (cursor := self._cache['cursor.active']) is not None and ((is_hover or self._pressed)
                                                                          if self._cache['cursor.active-outside'] else
                                                                          is_hover):
                self.event.cursor_active = True
                pygame.mouse.set_cursor(cursor)
            elif (cursor := self._cache['cursor.inactive']) is not None:
                pygame.mouse.set_cursor(cursor)

            self._button_track.update()

            if is_hover:
                self.event.interaction = ELEMENT_HOVER
                if any_pressed:
                    self.event.interaction = ELEMENT_ACTIVE

            if self.with_event and (track_press := self._button_track.event.press):
                self.event.press = track_press
                self.event.dragging = True
                self._update_rect(mouse_pos)

            elif not self.with_event and any_pressed:
                if is_hover:
                    self._pressed = True

                if current_time - self._last_pressed_time > self.press_speed and self._pressed:
                    self._last_pressed_time = current_time
                    self.event.dragging = True

                    if get_pressed[0]:
                        self.event.press = PRESS_LEFT
                    elif get_pressed[1]:
                        self.event.press = PRESS_MIDDLE
                    elif get_pressed[2]:
                        self.event.press = PRESS_RIGHT

                    self._update_rect(mouse_pos)

            elif not self.with_event:
                self._pressed = False

            if self._detected_scrolling_mouse:
                self._detected_scrolling_mouse = False

        self.event._send_event()

        return self.event

    def draw_and_update(self) -> ElementEvent:
        self.update()
        self._render_and_draw(self.event.interaction, True)
        return self.event

    def draw_inactive(self) -> None:
        self._pressed = False
        self._render_and_draw(ELEMENT_INACTIVE)
        self.event._reset()

    def draw_hover(self) -> None:
        self._pressed = False
        self._render_and_draw(ELEMENT_HOVER)
        self.event._reset()

    def draw_active(self) -> None:
        self._pressed = False
        self._render_and_draw(ELEMENT_ACTIVE)
        self.event._reset()

__all__ = [
    'Button',
    'Range'
]