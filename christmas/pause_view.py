from typing import List

from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, K_p
from christmas.base_view import BaseView
from christmas.game import Game

import pygame

class PauseView(BaseView):
    def __init__(self, parent: BaseView):
        self._parent = parent
        self._font = pygame.font.SysFont("Calibri", 40)
        self._text = self._font.render("PAUSED", True, (0,0,0))


    def event_loop(self, events: List[pygame.event.Event]):
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                Game.set_current_view(self._parent)
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    Game.set_current_view(self._parent)


    def update(self):
        pass


    def draw(self, surface: pygame.Surface):
        overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0,0,0,200))

        overlay.blit(self.get_text(), (100,100))

    
    def get_text(self):
        return self._text