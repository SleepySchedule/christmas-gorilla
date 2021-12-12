from typing import List, Optional

import pygame
from pygame.constants import MOUSEBUTTONDOWN

from christmas.base_view import BaseView
from christmas.my_game import MyGame
from christmas.play_view import PlayView


class TitleView(BaseView):
    def __init__(self) -> None:
        title_font = pygame.font.SysFont("Arial", 40)
        self.title_text = title_font.render("Gorillas: Christmas Edition", True, (255, 255, 255))

        self.info_font = pygame.font.SysFont("Arial", 25)
        self.info_text = self.info_font.render("Click to play", True, (175, 175, 175))

        self.previous_winner: Optional[str] = None

    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                MyGame.set_current_view(PlayView())

    def update(self) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((0, 0, 128))
        surf_center = surface.get_rect().center
        text_rect = self.title_text.get_rect()
        text_rect.center = surf_center
        text_rect.y = surface.get_height() * 0.33
        surface.blit(self.title_text, text_rect.topleft)

        text_rect = self.info_text.get_rect()
        text_rect.center = surf_center
        text_rect.y = surface.get_height() * 0.67
        surface.blit(self.info_text, text_rect.topleft)

        # score, if available
        if self.previous_winner is not None:
            previous_score_text = self.info_font.render(f"Previous winner: {self.previous_winner.capitalize()} side", True, (255, 255, 255))
            text_rect = previous_score_text.get_rect()
            text_rect.center = surf_center
            text_rect.y = surface.get_height() * 0.80
            surface.blit(previous_score_text, (text_rect.topleft))

    def set_previous_winner(self, score: int) -> None:
        self.previous_winner = score