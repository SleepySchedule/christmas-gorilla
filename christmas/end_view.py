import pygame

from typing import List

from christmas.base_view import BaseView


class EndView(BaseView):
    def event_loop(self, events: List[pygame.event.Event]) -> None:
        pass


    def update(self) -> None:
        pass


    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((255,255,255))
        pygame.draw.circle(surface, (0,0,0), (640, 360), 100)