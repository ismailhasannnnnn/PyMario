import pygame as pg
from vector import Vector
from pygame.sprite import Sprite

class Mario(Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.image = pg.image.load("images/Blue_Brick.png")

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.center_bottom()
        self.v = Vector()


    def center_bottom(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = Vector(self.rect.centerx, self.rect.centery)

    def inc_add(self, other):
        self.v += other

    def update(self):
        self.center += self.v * self.settings.mario_speed_factor
        self.rect.centerx, self.rect.centery = self.center.x, self.center.y

    def draw(self):
        self.screen.blit(self.image, self.rect)
