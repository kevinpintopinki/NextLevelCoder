import pygame
import random

from utils.constants import (
    SCREEN_WIDTH, IMG_DIR, BLACK
)
from os import path

allowed_speed = list(range(3, 7))


class Powerup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR, "power.jpg")).convert()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.bottom = 0

    def update(self):
        self.rect.y = self.rect.y + 4
