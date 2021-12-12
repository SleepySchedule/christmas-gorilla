import pygame

from typing import List

from pygame.constants import MOUSEBUTTONDOWN

from christmas.base_view import BaseView
from christmas.my_game import MyGame


class EndView(BaseView):
    def __init__(self, winning_team: str) -> None:
        self.winning_team = winning_team

        self.font = pygame.font.SysFont("Calibri", 40)
        self.text = self.font.render(f"{self.winning_team.capitalize()} team wins!", True, (0, 0, 0))
        self.text_rect = self.text.get_rect()


    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                from christmas.title_view import TitleView
                view = TitleView()
                view.set_previous_winner(self.winning_team)
                MyGame.set_current_view(view)


    def update(self) -> None:
        pass


    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((255,255,255))
        self.text_rect.center = surface.get_rect().center
        surface.blit(self.text, self.text_rect.topleft)