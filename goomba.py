import pygame as pg
from pygame.sprite import Sprite
from vector import Vector
from coords import Coords


class Goomba(Sprite):

    def __init__(self, game, ul):
        super().__init__()
        self.game = game

        self.screen = game.screen
        self.spritesheet = game.spritesheet
        self.settings = game.settings
        self.ul = ul
        self.goomba1_rect = Coords.coords["GOOMBA_1"]
        self.goomba_image = self.spritesheet.image_at(self.goomba1_rect, -1)
        self.image = pg.transform.rotozoom(self.goomba_image, 0, 2)

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.v = Vector()

    def update(self):
        self.mario = self.game.mario
        if pg.sprite.collide_mask(self, self.game.mario):
            print(pg.sprite.collide_mask(self, self.game.mario))

    def draw(self):
        self.enemies = self.game.enemies
        self.screen.blit(self.image, (self.ul[0] + self.enemies.bg_x, self.ul[1]))
