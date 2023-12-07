import pygame
import map
from constants import *

clock = pygame.time.Clock()

if __name__ == '__main__':
    pygame.init()
    SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
    pygame.display.set_caption("Conway's game of life")

    map = map.Map(SCREEN)

    clock.tick(FPS)
    run = True
    while run:
        SCREEN.fill(GREY)
        map.draw()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

