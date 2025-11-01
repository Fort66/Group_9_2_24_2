import pygame as pg

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, RESIZABLE, FULLSCREEN, MOUSEBUTTONDOWN, K_w, K_s, K_a, K_d

from pygame.display import set_mode, set_caption

from icecream import ic

from random import choice, uniform

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
        self.speed = 5

    def move(self):
        keys = pg.key.get_pressed()

        if keys[K_w]:
            self.rect.move_ip(0, -self.speed)
        if keys[K_s]:
            self.rect.move_ip(0, self.speed)
        if keys[K_a]:
            self.rect.move_ip(-self.speed, 0)
        if keys[K_d]:
            self.rect.move_ip(self.speed, 0)

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
        self.move()
        self.check_position()
        screen.blit(self.image, self.rect)


class Ball:
    def __init__(self):
        self.image = pg.Surface([25, 25])
        self.image.fill('DarkGreen')
        self.generator()
        self.speed = 10

    def generator(self):
        self.rect = self.image.get_rect(center=(
            uniform(screen.get_width(), screen.get_width() + 1000),
            uniform(0, screen.get_height()
            )))

    def move(self):
        self.rect.move_ip(-self.speed, 0)

    def check_position(self):
        if self.rect.left <= -30:
            self.generator()

    def update(self):
        self.move()
        self.check_position()
        screen.blit(self.image, self.rect)




player = Player()

balls = []

for i in range(10):
    balls.append(Ball())


loop = True

while loop:
    screen.fill('black')

    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

    player.update()
    for ball in balls:
        ball.update()

    pg.display.update()
    clock.tick(fps)
pg.quit()