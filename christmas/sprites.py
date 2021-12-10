from typing import Optional, Sequence, Tuple
from abc import ABC, abstractmethod
import pygame
import math, random

from pygame.constants import K_a, K_d, K_s, K_w


class Sprite:
    def __init__(self, pos: pygame.Vector2, speed: Optional[pygame.Vector2]=None):
        self._pos = pos
        self._speed = speed

    @abstractmethod
    def draw(self) -> None: ...

    @abstractmethod
    def update(self) -> None: ...


class Snowman(Sprite):
    def update(self, keys_pressed: Sequence[bool]):
        if keys_pressed:
            # if keys_pressed[K_w]:
            #     self._pos[1] -= 5
            if keys_pressed[K_a]:
                self._pos[0] -= 5
            # if keys_pressed[K_s]:
            #     self._pos[1] += 5
            if keys_pressed[K_d]:
                self._pos[0] += 5 

    def draw(self, surface: pygame.Surface):
        # body
        pygame.draw.circle(surface, (255,255,255), (self._pos[0],self._pos[1]), 12)
        pygame.draw.circle(surface, (255,255,255), (self._pos[0],self._pos[1]+25), 20)
        pygame.draw.circle(surface, (255,255,255), (self._pos[0],self._pos[1]+55), 28)
        
        # arms
        pygame.draw.line(surface, (150,75,0), (self._pos[0]-10,self._pos[1]+15), (self._pos[0]-40,self._pos[1]+40), 5)
        pygame.draw.line(surface, (150,75,0), (self._pos[0]+10,self._pos[1]+15), (self._pos[0]+40,self._pos[1]+40), 5)
        
        # eyes
        pygame.draw.circle(surface, (0,0,0), (self._pos[0]-5,self._pos[1]-2), 3)
        pygame.draw.circle(surface, (0,0,0), (self._pos[0]+5,self._pos[1]-2), 3)

        # mouth
        pygame.draw.arc(surface, (0,0,0), (self._pos[0]-6,self._pos[1]+1, 12, 4), math.pi, math.pi*2, 3)

        # buttons
        pygame.draw.circle(surface, (0,0,0), (self._pos[0],self._pos[1]+25), 3)
        pygame.draw.circle(surface, (0,0,0), (self._pos[0],self._pos[1]+40), 3)
        pygame.draw.circle(surface, (0,0,0), (self._pos[0],self._pos[1]+55), 3)

        # hat
        pygame.draw.line(surface, (0,0,0), (self._pos[0]-15,self._pos[1]-11), (self._pos[0]+15,self._pos[1]-11), 2)
        pygame.draw.rect(surface, (0,0,0), (self._pos[0]-10,self._pos[1]-20, 20, 10))

    def throw_snowball(self, end_pos: pygame.Vector2):
        # start_pos = pygame.Vector2((self.x + 40, self.y + 40))
        # end_pos = pygame.Vector2(end_pos)
        start_pos = pygame.Vector2(self._pos)
        speed = end_pos - start_pos
        speed.normalize_ip()
        speed *= 5
        snowball_pos = pygame.Vector2(start_pos)
        snowball = Snowball(snowball_pos, speed)
        # snowball.update(end_pos)
        return snowball

    def set_pos(self, pos: Tuple[int, int]):
        self._pos = pos


class Snowball(Sprite):
    def __init__(self) -> None:
        self.x0 = 0
        self.y0 = 400
        self.gravity = 9.81
        self.angle = 70
        self.velocity = 80
        self.x = 0
        self.y = 0

        vx = self.velocity * math.cos(math.radians(self.angle))
        vy = self.velocity * math.sin(math.radians(self.angle))
        self.t = 0

    def update(self) -> None:
        self.t += 0.2
        self.x = self.x0 + self.vx*self.t
        self.y = self.y0 - (self.vy*self.t - 0.5*self.gravity*self.t**2)
            
    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((255, 255, 255))
        pygame.draw.circle(surface, (0, 0, 255), (self.x, self.y), 30)
