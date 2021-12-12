from typing import Dict, List, Tuple
from abc import ABC, abstractmethod

import pygame, math


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
        """Gets the position of the snowman (from the top left corner)."""
        return self._pos

    def get_rect(self) -> pygame.Rect:
        """Gets the rectangular hitbox of the snowman (cutting off the arms)."""
        return self._snowman.get_rect(left=self._pos[0]+35, top=self._pos[1], width=35)

    def get_team(self) -> str:
        """Gets the team name of the snowman."""
        return self._team


class Fireball(Sprite):
    def __init__(self, player: Snowman) -> None:
        self._fireball = pygame.image.load("images/fireball.png")
        self._fireball = pygame.transform.scale(self._fireball, (25,30))
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
            True if fireball is off bottom of the screen, false otherwise.
        """

        if self.y > 720:
            dead = True
        else:
            dead = False

        return dead

    from christmas.team import Team
    def collide(self, teams: List[Team]) -> Snowman:
        """Checks if the fireball has hit an enemy player.
        
        Args:
            teams: The team class that holds the name and list of players.
        
        Returns:
            The enemy player if the fireball has hit them, nothing otherwise.
        """

        for team in teams:
            if team.get_name() == self.get_player().get_team():
                continue
            
            for player in team.get_players():
                if self.get_rect().colliderect(player.get_rect()):
                    return player
        
        return None

    def get_rect(self) -> pygame.Rect:
        """Gets the rectangular hitbox of the fireball."""
        return self._fireball.get_rect(left=self.x, top=self.y)

    def get_player(self) -> Snowman:
        """Gets the player that threw the fireball."""
        return self._player

    def set_velocity(self, distance: float) -> None:
        """Sets the velocity the fireball will move at.
        
        Args:
            distance: the player position subtracted from the mouse position.
        """
        self._velocity = distance//5

    def set_angle(self, angle: float) -> None:
        """Sets the angle the fireball will move at.
        
        Args:
            angle: angle of the player position to mouse position (starting left side going clockwise)."""
        self._angle = angle
