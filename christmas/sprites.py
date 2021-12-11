from typing import Dict, List, Tuple
from abc import ABC, abstractmethod
import pygame
import math


class Sprite(ABC):
    @abstractmethod
    def draw(self) -> None: ...

    @abstractmethod
    def update(self) -> None: ...


class Snowman(Sprite):
    def __init__(self, pos: Tuple[int, int], team: str):
        self._snowman = pygame.image.load("images/snowman.png")
        self._snowman = pygame.transform.scale(self._snowman, (100, 100))
        self._pos = pos
        self._team = team

    def update(self):
        pass

    def draw(self, surface: pygame.Surface):
        surface.blit(self._snowman, self._pos)
   
    def get_pos(self) -> Tuple[int, int]:
        return self._pos

    def get_rect(self) -> pygame.Rect:
        return self._snowman.get_rect(left=self._pos[0], top=self._pos[1])

    def get_team(self) -> str:
        return self._team


class Fireball(Sprite):
    def __init__(self, player: Snowman) -> None:
        self._fireball = pygame.image.load("images/fireball.png")
        self._fireball = pygame.transform.scale(self._fireball, (50,60))
        self.gravity = 9.81
        self._player = player
        self._angle = 0
        self._velocity = 0

        self.x = 0
        self.y = 0
        self.t = 0

    def update(self) -> None:
        self.t += 0.2

        self.x0, self.y0 = self._player.get_pos()

        vx = -(self._velocity * math.cos(math.radians(self._angle)))
        vy = self._velocity * math.sin(math.radians(self._angle))

        self.x = self.x0 + vx*self.t
        self.y = self.y0 - (vy*self.t - 0.5*self.gravity*self.t**2)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self._fireball, (self.x, self.y))

    def is_dead(self) -> bool:
        """Checks if fireball should be killed.
        
        Returns:
            True if fireball is off bottom of screen, false otherwise.
        """
        if self.y > 720:
            dead = True
        else:
            dead = False
        return dead

    def collide(self, teams: List[Dict[str, List[Snowman]]]) -> Snowman:
        """Checks if the fireball has hit an enemy player.
        
        Args:
            teams: list of teams that have team name and list of players (Snowman class).
        
        Returns:
            The enemy player if the fireball has hit them, nothing otherwise.
        """

        for team in teams:
            if team['team'] != self._player.get_team():
                continue
            
            for player in team['players']:
                if self.get_rect().colliderect(player.get_rect()):
                    return player
        
        return None

    def get_rect(self) -> pygame.Rect:
        return self._fireball.get_rect(left=self.x, top=self.y)

    def get_player(self) -> Snowman:
        return self._player

    def set_velocity(self, distance: float) -> None:
        self._velocity = distance//5

    def set_angle(self, angle: float) -> None:
        self._angle = angle
