import pygame

HEIGHT = WIDTH = 500
CELL_SIZE = 25
GRID_HEIGHT = GRID_WIDTH = HEIGHT // CELL_SIZE


WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (128,128,128)

clock = pygame.time.Clock()
FPS = 5


if __name__ == '__main__':
    pygame.init()
    SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
    pygame.display.set_caption("Conway's game of life")

    clock.tick(FPS)
    run = True
    while run:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

