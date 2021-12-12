from typing import List

from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, K_p
from christmas.base_view import BaseView
from christmas.my_game import MyGame

import pygame

class PauseView(BaseView):
    def __init__(self, parent: BaseView) -> None:
        self._parent = parent
        self._font = pygame.font.SysFont("Calibri", 80)
        self._text = self._font.render("PAUSED", True, (0,0,0))


    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                MyGame.set_current_view(self._parent)
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    MyGame.set_current_view(self._parent)


    def update(self) -> None:
        pass


    def draw(self, surface: pygame.Surface) -> None:
        self.get_parent().draw(surface)
        overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0,0,0,150))
        surface.blit(overlay, (0,0))
        surface_rect = surface.get_rect()
        surface_center = surface_rect.center
        text_rect = self.get_text().get_rect(center=surface_center)
        text_rect.y = 100
        surface.blit(self.get_text(), text_rect.topleft)

    
    def get_text(self) -> pygame.Surface:
        return self._text

    
    def get_parent(self) -> BaseView:
        return self._parent