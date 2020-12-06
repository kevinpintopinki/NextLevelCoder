import pygame
from utils.constants import (
    BLACK,
    SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_WIDTH, IMG_DIR

)
from components.bullet import Bullet
from os import path


class player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.condic = False
        self.game = game
        self.image = pygame.image.load(path.join(IMG_DIR, "alien.png")).convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 1.1
        self.rect.centery = SCREEN_HEIGHT / 1.1
        self.bullets = pygame.sprite.Group()
        self.contador = 0

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rect.centerx += 5
            key = pygame.key.get_pressed()
        elif key[pygame.K_LEFT]:
            self.rect.centerx -= 5
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0

    def shoot(self):
        sound_rifle = pygame.mixer.Sound(path.join(IMG_DIR, 'rifle.ogg'))
        pygame.mixer.Sound.play(sound_rifle)
        self.contador += 1
        if self.contador == 5 :
            self.condic = False
        if self.condic == False:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.game.all_sprites.add(bullet)
            self.bullets.add(bullet)
        elif self.condic == True:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullet2 = Bullet(self.rect.centerx - 10, self.rect.top)
            bullet3 = Bullet(self.rect.centerx - 20, self.rect.top)
            self.game.all_sprites.add(bullet)
            self.game.all_sprites.add(bullet2)
            self.game.all_sprites.add(bullet3)
            self.bullets.add(bullet)
            self.bullets.add(bullet2)
            self.bullets.add(bullet3)

