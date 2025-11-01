from pygame.image import load
from pygame.transform import scale_by

from random import uniform

class Rockets:
    def __init__(self, screen):
        self.screen = screen
        self.image = scale_by(load('images/shutter.png').convert_alpha(), .15)
        self.generator()
        self.speed = uniform(5, 10)

    def generator(self):
        self.rect = self.image.get_rect(center=(
            uniform(self.screen.get_width(), self.screen.get_width() + 1000),
            uniform(0, self.screen.get_height()
            )))

    def move(self):
        self.rect.move_ip(-self.speed, 0)

    def check_position(self):
        if self.rect.left <= -30:
            self.generator()

    def update(self):
        self.move()
        self.check_position()
        self.screen.blit(self.image, self.rect)