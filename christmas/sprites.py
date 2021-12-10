from typing import Optional, Sequence, Tuple
from abc import ABC, abstractmethod
import pygame
import math, random

from pygame.constants import K_a, K_d, K_s, K_w


class Sprite(ABC):
    @abstractmethod
    def draw(self) -> None: ...

    @abstractmethod
    def update(self) -> None: ...


class Snowman(Sprite):
    def __init__(self, pos: Tuple[int, int]):
        self.snowman = pygame.image.load("snowman.png")
        self.snowman = pygame.transform.scale(self.snowman, (100, 100))
        self._pos = pos

    def update(self):
        pass

    def draw(self, surface: pygame.Surface):
        surface.blit(self.snowman, self._pos)

    def update_snowball(self, snowball: 'Snowball'):
        snowball.update(self)
   
    def get_pos(self):
        return self._pos
   
    def get_hitbox(self):
        pass


class Snowball(Sprite):
    def __init__(self) -> None:
        self.gravity = 9.81
        self._angle = 0
        self._velocity = 0

        self.x = 0
        self.y = 0
        self.t = 0

    def update(self, snowman: Snowman) -> None:
        self.t += 0.2

        self.x0, self.y0 = snowman.get_pos()

        vx = -(self._velocity * math.cos(self._angle))
        vy = self._velocity * math.sin(self._angle)

        self.x = self.x0 + vx*self.t
        self.y = self.y0 - (vy*self.t - 0.5*self.gravity*self.t**2)

    def is_dead(self) -> bool:
        if self.y > 720:
            dead = True
        else:
            dead = False
        return dead

    def draw(self, surface: pygame.Surface) -> None:
        
        pygame.draw.circle(surface, (0, 0, 255), (self.x, self.y), 30)

    def set_velocity(self, distance: float):
        self._velocity = distance//5

    def set_angle(self, angle: int):
        self._angle = angle