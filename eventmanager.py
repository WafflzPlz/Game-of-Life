import pygame
import sys
import constants

class EventManager:
    def __init__(self, SCREEN, grid):
        self.SCREEN = SCREEN
        self.map = grid

    def close(self):
        pygame.quit()
        sys.exit()

    def update(self):
        events = pygame.event.get()
        for event in events:

            if event.type == pygame.KEYDOWN:

                # close game
                if event.key == pygame.K_ESCAPE:
                    self.close()

            #close game
            if event.type == pygame.QUIT:
                self.close()