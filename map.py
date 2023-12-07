import pygame
from constants import *
class Map:
    def __init__(self, SCREEN):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.SCREEN = SCREEN
        self.grid_lines = True

    def swap_value(self, x, y):
        self.grid[x][y] = 0 if self.grid[x][y] == 1 else 1

    def toggle_grid_lines(self):
        self.grid_lines = not self.grid_lines

    def update(self):
        for row in self.grid:
            for col in row:
                print("hello")
                # TODO:implement logic

    def draw_grid_lines(self):
        for row in range(HEIGHT):
            pygame.draw.line(self.SCREEN, GREY, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE))

        #draw last row line
        pygame.draw.line(self.SCREEN, GREY, (0, HEIGHT - 1), (WIDTH, HEIGHT - 1))

        for col in range(WIDTH):
            pygame.draw.line(self.SCREEN, GREY, (col * CELL_SIZE, 0), (col * CELL_SIZE, HEIGHT))

        #draw last col line
        pygame.draw.line(self.SCREEN, GREY, (WIDTH - 1, 0), (WIDTH - 1, HEIGHT))

    def draw(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 1:
                    pygame.draw.rect(self.SCREEN, WHITE, pygame.Rect(row * CELL_SIZE, col * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                else:
                    pygame.draw.rect(self.SCREEN, BLACK, pygame.Rect(row * CELL_SIZE, col * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        if self.grid_lines: self.draw_grid_lines()