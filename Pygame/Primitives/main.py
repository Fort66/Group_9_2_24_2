import pygame as pg

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, RESIZABLE, FULLSCREEN, MOUSEBUTTONDOWN

from pygame.display import set_mode, set_caption

from random import choice

pg.init()


# width = 1024
# height = 768

colors = ['SteelBlue', 'DarkGreen', 'DarkOliveGreen', 'DarkRed', 'Indigo']

size = [1024, 768]

screen = set_mode(size, flags=pg.RESIZABLE)
set_caption('MyGame')

fps = 60
clock = pg.time.Clock()

class Player:
    def __init__(self):
        self.image = pg.Surface([50, 50])
        self.image.fill('SteelBlue')
        self.rect = self.image.get_rect()


player = Player()


loop = True

while loop:
    # screen.fill('SteelBlue')

    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

        # if event.type == KEYDOWN:
        #     print(event.key)

        # if event.type == MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         print(event.pos)


    # pg.draw.circle(screen, 'blue', (200, 200), 50, 10)
    # pg.draw.rect(screen, 'red', (100, 100, 100, 100), 1)
    # pg.draw.line(screen, 'green', (0, 0), (300, 300), 3)
    # pg.draw.aaline(screen, 'green', (50, 0), (350, 350), 3)
    # pg.draw.lines(screen, 'yellow', True, [(200, 80), (200, 100), (220, 100)], 3)
    # pg.draw.polygon(screen, 'white', [[100, 100], [100, 200], [200, 100]], 3)

    pg.display.update()
    clock.tick(fps)
pg.quit()