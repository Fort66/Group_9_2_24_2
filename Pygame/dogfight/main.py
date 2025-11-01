import pygame as pg
pg.init()

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, RESIZABLE, FULLSCREEN
from pygame.display import set_mode, set_caption

from icecream import ic

from random import choice, uniform

from classes.class_Player import Player
from classes.class_Rockets import Rockets
from classes.class_Clouds import Clouds


size = [1920, 1080]

screen = set_mode(size, flags=pg.RESIZABLE)
set_caption('MyGame')

fps = 60
clock = pg.time.Clock()



player = Player(screen)

rockets = [Rockets(screen) for _ in range(15)]
clouds = [Clouds(screen) for _ in range(15)]


loop = True

while loop:
    screen.fill('SkyBlue')

    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

    player.update()

    for rocket in rockets:
        rocket.update()

    for cloud in clouds:
        cloud.update()

    pg.display.update()
    clock.tick(fps)
pg.quit()