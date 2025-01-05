from typing import TYPE_CHECKING, Self
from abc import abstractmethod, ABC
from inspect import signature
from copy import deepcopy

from pygame.event import Event

from .tools import asserter, merge_deep

if TYPE_CHECKING:
    from .unions import DictParam
    from .events import ElementEvent

class Interface:

    def __init__(self, child_class: object, except_copy: set[str] | str = {}) -> None:
        self._child_class = child_class
        self._except_copy = {except_copy} if isinstance(except_copy, str) else set(except_copy)

    def __str__(self) -> str:
        return self.__class__.__name__

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memo: dict):
        return self.copy()

    def get_param(self) -> 'DictParam':
        parameters = signature(self.__init__).parameters
        return {name: getattr(self, name) for name in parameters}

    def set_param(self, **kwargs) -> Self:
        params = self.get_param()

        for name, value in kwargs.items():
            asserter(
                name in params,
                TypeError(f"{self.__class__.__name__}.set_param() got an unexpected keyword argument '{name}'")
            )
            setattr(self, name, value)

        return self

    def copy(self) -> Self:
        params = self.get_param()

        for key, value in params.items():
            if key not in self._except_copy:
                params[key] = deepcopy(value)

        return self._child_class(**params)

class ElementInterface(ABC, Interface):

    @abstractmethod
    def __init__(self, child_class: 'ElementInterface', except_copy: set[str] | str = {}) -> None:
        super().__init__(child_class, except_copy)
        self._cache = {}

    @abstractmethod
    def update_cache(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def handle_event(self, event: Event) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self) -> 'ElementEvent':
        raise NotImplementedError

    def set_param(self, **kwargs) -> Self:
        super().set_param(**kwargs)
        self.update_cache()
        return self

    def set_merge_param(self, **kwargs) -> Self:
        return self.set_param(**(self.get_param() | kwargs))

    def set_merge_deep_param(self, **kwargs) -> Self:
        return self.set_param(**merge_deep(self.get_param(),
                                           kwargs,
                                           kwargs.pop('_deep_', -1)))

__all__ = [
    'Interface',
    'ElementInterface'
]