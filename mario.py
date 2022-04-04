import pygame as pg
from vector import Vector
from pygame.sprite import Sprite

class Mario(Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.image = pg.transform.rotozoom(pg.image.load("images/Blue_Brick.png"), 0, 3)

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.center_bottom()
        self.v = Vector()
        self.movingForward = False


    def center_bottom(self):
        self.rect.centerx = self.screen_rect.centerx - 400
        self.rect.centery = self.screen_rect.centery - 200
        self.rect.bottom = self.screen_rect.bottom
        self.center = Vector(self.rect.centerx, self.rect.centery)

    def inc_add(self, other):
        self.v += other

    def clamp(self):
        rw, rh = self.rect.width, self.rect.height
        srw, srb = self.screen_rect.width, self.screen_rect.bottom
        x, y = self.center.x, self.center.y

        self.center.x = min(max(x, rw / 2), srw - rw / 2)
        self.center.y = min(max(y, rh / 2), srb - rh / 2)

    def update(self):
        self.center += self.v * self.settings.mario_speed_factor
        self.clamp()
        self.rect.centerx, self.rect.centery = self.center.x, self.center.y

    def draw(self):
        self.screen.blit(self.image, self.rect)
