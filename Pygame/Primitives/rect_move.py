import pygame as pg

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, RESIZABLE, FULLSCREEN, MOUSEBUTTONDOWN, K_w, K_s, K_a, K_d

from pygame.display import set_mode, set_caption

from icecream import ic

from random import choice

pg.init()



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
        self.rect.center = [screen.get_width() // 2, screen.get_height() // 2]

    def move(self):
        keys = pg.key.get_pressed()

        if keys[K_w]:
            self.rect.move_ip(0, -10)
        if keys[K_s]:
            self.rect.move_ip(0, 10)
        if keys[K_a]:
            self.rect.move_ip(-10, 0)
        if keys[K_d]:
            self.rect.move_ip(10, 0)

    def check_position(self):
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= screen.get_width():
            self.rect.right = screen.get_width()

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= screen.get_height():
            self.rect.bottom = screen.get_height()


    def update(self):
        screen.blit(player.image, player.rect)
        self.check_position()
        self.move()


player = Player()


loop = True

while loop:
    screen.fill('black')

    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

    player.update()

    pg.display.update()
    clock.tick(fps)
pg.quit()