import pygame as pg
from pygame.sprite import Sprite
from vector import Vector
from timer import Timer

class Enemy(Sprite):

    def __init__(self, game, ul, image_list, delay=200, isLoop=True):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.spritesheet = game.spritesheet
        self.settings = game.settings
        self.ul = ul
        self.image_list = image_list
        self.image = image_list[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = ul
        self.timer = Timer(self.image_list, 0, delay, isLoop)
        self.screen_rect = self.screen.get_rect()


    def collision_check(self):
        collisions = pg.sprite.spritecollide(self.mario, self.enemies.enemies, True)


    def update(self):
        self.mario = self.game.mario
        self.enemies = self.game.enemies
        self.center = Vector(self.rect.centerx, self.rect.centery)
        self.lastBg_x = 0
        self.center += self.v

        self.rect.centerx += self.enemies.bg_x - self.lastBg_x

        self.collision_check()

        self.rect.centerx, self.rect.centery = self.center.x, self.center.y

    def draw(self):
        self.image = self.timer.image()
        self.screen.blit(self.image, (self.rect.x + self.enemies.bg_x, self.rect.y))