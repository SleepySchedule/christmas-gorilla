from typing import List

import pygame
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, K_p

from christmas.base_view import BaseView
from christmas.pause_view import PauseView
from christmas.my_game import MyGame
from christmas.sprites import Snowman, Fireball
from christmas.end_view import EndView

class PlayView(BaseView):
    def __init__(self) -> None:
        self.font = pygame.font.SysFont("Arial", 30)

        self.player_loc = [(1000, 500), (180, 500)]

        self.player_1 = Snowman(self.player_loc[0], "right")
        self.player_2 = Snowman(self.player_loc[1], "left")


        self.team_left = {
            'team': 'left',
            'players': [self.player_1]
        }
        self.team_right = {
            'team': 'right',
            'players': [self.player_2]
        }
        
        self.teams = [self.team_left, self.team_right]

        self.existing_fireball = False

        self.turn = 1


    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if not self.existing_fireball:
                    self.existing_fireball = True
                    player_pos = pygame.Vector2(self.player_loc[self.turn-1])
                    if self.turn == 1:
                        self.fireball = Fireball(self.player_1)
                        self.turn = 2
                    elif self.turn == 2:
                        self.fireball = Fireball(self.player_2)
                        self.turn = 1

                    mouse_pos = pygame.Vector2(event.pos)
                    difference = mouse_pos - player_pos

                    distance, angle = pygame.Vector2.as_polar(difference)

                    angle -= 180
                    distance = min(max(distance, 250), 600)

                    self.fireball.set_velocity(distance)
                    self.fireball.set_angle(angle)

            elif event.type == KEYDOWN:
                if event.key == K_p:
                    MyGame.set_current_view(PauseView(self))


    def update(self) -> None:
        if self.existing_fireball:
            if self.fireball.is_dead():
                self.existing_fireball = False
            else:
                self.fireball.update()

                player = self.fireball.collide(self.teams)
                
                if player != None:
                    self.existing_fireball = False
                    
                    for team in self.teams:
                        if team['team'] == player.get_team():
                            continue
                        
                        team['players'].remove(player)
                        
                        if team['players'] == []:
                            winning_team = self.fireball.get_player().get_team()
                            MyGame.set_current_view(EndView(winning_team))


    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((200,200,200))

        for team in self.teams:
            for player in team['players']:
                player.draw(surface)

        if self.existing_fireball:
            self.fireball.draw(surface)
