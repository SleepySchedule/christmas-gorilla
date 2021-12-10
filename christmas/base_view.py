from abc import ABC, abstractmethod
from typing import List

import pygame


class BaseView(ABC):
    @abstractmethod
    def event_loop(self, events: List[pygame.event.Event]) -> None: ...

    @abstractmethod
    def update(self) -> None: ...

    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None: ...