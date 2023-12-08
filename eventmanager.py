import pygame
import sys
from constants import *

class EventManager:
    def __init__(self, SCREEN, map):
        self.SCREEN = SCREEN
        self.map = map
        self.running = False

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

    def toggle_pause(self):
        self.running = not self.running

    def update(self):
        if self.running: self.map.update()

        events = pygame.event.get()
        for event in events:

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.click()

            if event.type == pygame.KEYDOWN:

                # deacitvate drawing of grid lines
                if event.key == pygame.K_t:
                    self.toggle_grid_lines()

                # pause the game
                if event.key == pygame.K_SPACE:
                    self.toggle_pause()

                # reset map
                if event.key == pygame.K_r:
                    self.map.reset()

                # close game
                if event.key == pygame.K_ESCAPE:
                    self.close()

            #close game
            if event.type == pygame.QUIT:
                self.close()
