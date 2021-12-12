from typing import List

import pygame, random
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, K_p

from christmas.base_view import BaseView
from christmas.pause_view import PauseView
from christmas.my_game import MyGame
from christmas.sprites import Snowman, Fireball
from christmas.team import Team
from christmas.end_view import EndView

class PlayView(BaseView):
    def __init__(self) -> None:
        self.font = pygame.font.SysFont("Arial", 30)

        self.player_loc = [(1000, 500), (180, 500)]

        self.player_1 = Snowman(self.player_loc[0], "right")
        self.player_2 = Snowman(self.player_loc[1], "left")

        self.team_right = Team('right', [self.player_1])
        self.team_left = Team('left', [self.player_2])
        
        self.teams = [self.team_left, self.team_right]

        self.existing_fireball = False

        self.turn = random.randint(1, 2)

        self.right_turn_text = self.font.render("Right Side's Turn", True, (0,0,0))

        self.left_turn_text = self.font.render("Left Side's Turn", True, (0,0,0))

        if self.turn == 1:
            self.turn_text = self.right_turn_text
        elif self.turn == 2:
            self.turn_text = self.left_turn_text


    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if not self.existing_fireball:
                    self.existing_fireball = True
                    player_pos = pygame.Vector2(self.player_loc[self.turn-1])
                    if self.turn == 1:
                        self.fireball = Fireball(self.player_1)
                        self.turn = 2
                        self.turn_text = self.left_turn_text
                    elif self.turn == 2:
                        self.fireball = Fireball(self.player_2)
                        self.turn = 1
                        self.turn_text = self.right_turn_text

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
                return
           
            self.fireball.update()

            player = self.fireball.collide(self.teams)
            
            if player != None:
                self.existing_fireball = False
                
                for team in self.teams:
                    if player not in team.get_players():
                        continue
                    
                    team.remove_player(player)
                    
                    if team.get_players() == []:
                        winning_team = self.fireball.get_player().get_team()
                        MyGame.set_current_view(EndView(winning_team))


    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((200,200,200))

        turn_text_rect = self.turn_text.get_rect()
        surface_rect = surface.get_rect()
        turn_text_rect.center = surface_rect.center
        turn_text_rect.y = surface_rect.y

        surface.blit(self.turn_text, turn_text_rect.topleft)

        for team in self.teams:
            for player in team.get_players():
                player.draw(surface)

        if self.existing_fireball:
            self.fireball.draw(surface)
