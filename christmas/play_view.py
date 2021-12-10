from typing import List

import pygame, math
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, K_p

from christmas.base_view import BaseView
from christmas.pause_view import PauseView
from christmas.game import Game
from christmas.sprites import Snowman, Snowball
from christmas.end_view import EndView

class PlayView(BaseView):
    def __init__(self) -> None:
        self.font = pygame.font.SysFont("Arial", 30)

        self.player_1_loc = (1000, 500)
        self.player_1 = Snowman(self.player_1_loc)
        self.existing_snowball = False
        # self.snowballs: List[Snowball]=[]
        # self.targets: List[Target]=[]

        # for _ in range(10):
        #     pos = pygame.Vector2((random.randint(100,1180), 220))
        #     speed = pygame.Vector2((3,0))
        #     num = random.randint(0, 1)
        #     if num:
        #         direction = "right"
        #     else:
        #         direction = "left"
        #     t = Target(pos, speed, direction)

        #     self.targets.append(t)


    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                # mouse_loc = event.pos
                # mouse_loc = pygame.Vector2(mouse_loc)
                # self.snowballs.append(self.player_1.throw_snowball(mouse_loc))
                if not self.existing_snowball:
                    self.existing_snowball = True
                    self.snowball = Snowball()
                    distance_x = event.pos[0] - self.player_1_loc[0]
                    distance_y = event.pos[1] - self.player_1_loc[1]
                    angle = math.atan(distance_y/distance_x)
                    distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
                    self.snowball.set_velocity(distance)
                    self.snowball.set_angle(angle)
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    Game.set_current_view(PauseView(self))


    def update(self) -> None:
        if self.existing_snowball:
            if self.snowball.is_dead():
                self.existing_snowball = False
            else:
                self.player_1.update_snowball(self.snowball)
        # keys_pressed = pygame.key.get_pressed()
        # self.snowman.update(keys_pressed)
        # for snowball in self.snowballs:
        #     snowball.update()

        # for target in self.targets:
        #     target.update()


    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((200,200,200))

        self.player_1.draw(surface)

        if self.existing_snowball:
            self.snowball.draw(surface)

        # for snowball in self.snowballs:
        #     snowball.draw(surface)

        # for target in self.targets:
        #     target.draw(surface)

