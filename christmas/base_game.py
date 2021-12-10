from abc import ABC, abstractmethod

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

from christmas.base_view import BaseView


class BaseGame(ABC):
    game: 'BaseGame' = None

    def __init__(self):
        BaseGame.game = self

        pygame.init()
        pygame.font.init()

        WIDTH = 1280
        HEIGHT = 720
        SIZE = (WIDTH, HEIGHT)

        self.screen = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()

        self.current_view = None

        self.create()
    
    @staticmethod
    def set_current_view(view: BaseView):
        BaseGame.game.current_view = view


    @abstractmethod
    def create(self) -> None: ...

    def run(self) -> None:
        running = True
        while running:
            # EVENT HANDLING
            events = pygame.event.get()
            for event in events:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False
            
            self.current_view.event_loop(events)
            self.current_view.update()
            self.current_view.draw(self.screen)
            

            # Must be the last two lines
            # of the game loop
            pygame.display.flip()
            self.clock.tick(30)
            #---------------------------


        pygame.quit()