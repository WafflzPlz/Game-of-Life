import pygame
from map import Map
from eventmanager import EventManager

from constants import *

clock = pygame.time.Clock()

pygame.init()
SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Conway's game of life")

map = Map(SCREEN)
eventmanager = EventManager(SCREEN)

def main():
    run = True
    while run:
        clock.tick(FPS)
        SCREEN.fill(GREY)
        map.draw()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()



if __name__ == '__main__':
    main()
