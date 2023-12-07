import pygame
from constants import *
class Map:
    def __init__(self, SCREEN):
        self.grid = [[1 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.SCREEN = SCREEN

    def change_value(self, x, y):
        self.grid[y][x] = 0 if self.grid[y][x] == 1 else 0
    def update(self):
        for row in self.grid:
            for col in row:
                print("hello")
                # TODO:implement logic

    def draw(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 1:
                    pygame.draw.rect(self.SCREEN, WHITE, pygame.Rect(row * CELL_SIZE, col * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                else:
                    pygame.draw.rect(self.SCREEN, BLACK, pygame.Rect(row * CELL_SIZE, col * CELL_SIZE, CELL_SIZE, CELL_SIZE))