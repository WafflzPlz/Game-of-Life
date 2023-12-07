import pygame
import sys
from constants import *

class EventManager:
    def __init__(self, SCREEN, map):
        self.SCREEN = SCREEN
        self.map = map

    def close(self):
        pygame.quit()
        sys.exit()

    def click(self):
        x, y = pygame.mouse.get_pos()
        col = x // CELL_SIZE
        row = y // CELL_SIZE
        self.map.swap_value(col, row)

    def toggle_grid_lines(self):
        self.map.toggle_grid_lines()

    def update(self):
        events = pygame.event.get()
        for event in events:

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.click()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_t:
                    self.toggle_grid_lines()

                # close game
                if event.key == pygame.K_ESCAPE:
                    self.close()

            #close game
            if event.type == pygame.QUIT:
                self.close()