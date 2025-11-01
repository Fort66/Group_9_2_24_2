from pygame.image import load
from pygame.transform import scale_by

from random import uniform, choice

clouds_images = [
    'images/cloud1.png',
    'images/cloud2.png',
    'images/cloud3.png',
    'images/cloud4.png'
]

class Clouds:
    def __init__(self, screen):
        self.screen = screen
        self.image = scale_by(load(choice(clouds_images)).convert_alpha(), .7)
        self.generator()
        self.speed = uniform(1, 2)

    def generator(self):
        self.rect = self.image.get_rect(center=(
            uniform(self.screen.get_width(), self.screen.get_width() + 2000),
            uniform(0, self.screen.get_height()
            )))

    def move(self):
        self.rect.move_ip(-self.speed, 0)

    def check_position(self):
        if self.rect.left <= -1000:
            self.generator()

    def update(self):
        self.move()
        self.check_position()
        self.screen.blit(self.image, self.rect)