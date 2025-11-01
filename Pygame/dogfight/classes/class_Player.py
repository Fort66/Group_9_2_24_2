from pygame.locals import K_w, K_s, K_a, K_d, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_c
from pygame.image import load
from pygame.transform import scale_by, flip
from pygame.key import get_pressed

# from .class_Rockets import Rockets

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = scale_by(load('images/su-33.png').convert_alpha(), .2)
        self.rect = self.image.get_rect()
        self.rect.center = [self.screen.get_width() // 2, self.screen.get_height() // 2]
        self.speed = 5
        self.is_shoot = True

    def move(self):
        keys = get_pressed()

        if keys[K_w] or keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
        if keys[K_s] or keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if keys[K_a] or keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if keys[K_d] or keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[K_c]:
            self.shoot() if self.is_shoot else None
            self.is_shoot = False

    def shoot(self):
        self.shot_image = flip(scale_by(load('images/shutter.png').convert_alpha(), .15), True, False)
        self.shoot_rect = self.shot_image.get_rect(center=(self.rect.centerx - 46, self.rect.centery + 10))

    def check_position(self):
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= self.screen.get_width():
            self.rect.right = self.screen.get_width()

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= self.screen.get_height():
            self.rect.bottom = self.screen.get_height()


    def update(self):
        self.move()
        self.check_position()
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.shot_image, self.shoot_rect) if not self.is_shoot else None