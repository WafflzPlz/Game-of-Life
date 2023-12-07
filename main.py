import pygame
from map import Map
from eventmanager import EventManager

from constants import *

clock = pygame.time.Clock()

pygame.init()
SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Conway's game of life")

map = Map(SCREEN)
eventmanager = EventManager(SCREEN, map.grid)

run = True
def main():

    while True:
        clock.tick(FPS)
        SCREEN.fill(GREY)

        eventmanager.update()

        map.draw()

        pygame.display.update()

if __name__ == '__main__':
    main()
