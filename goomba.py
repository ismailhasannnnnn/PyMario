import pygame as pg
from pygame.sprite import Sprite
from vector import Vector
from coords import Coords
from timer import Timer


class Goomba(Sprite):

    goomba1_rect = Coords.coords["GOOMBA_1"]
    goomba2_rect = Coords.coords["GOOMBA_2"]

    def __init__(self, game, ul):
        super().__init__()
        self.game = game

        self.screen = game.screen
        self.spritesheet = game.spritesheet
        self.settings = game.settings
        self.ul = ul

        self.goomba_images = [pg.transform.rotozoom(self.spritesheet.image_at(Goomba.goomba1_rect), 0, 2),
                              pg.transform.rotozoom(self.spritesheet.image_at(Goomba.goomba2_rect), 0, 2)]
        self.image = self.goomba_images[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = ul
        self.timer = Timer(self.goomba_images, 0, 500, True)
        self.screen_rect = self.screen.get_rect()

        self.v = Vector(-4, 0)

    def update(self):
        self.mario = self.game.mario
        self.enemies = self.game.enemies
        self.center = Vector(self.rect.centerx, self.rect.centery)
        self.lastBg_x = 0
        self.center += self.v

        self.rect.centerx += self.enemies.bg_x - self.lastBg_x
        self.lastBg_x = self.game.bg_x

        collisions = pg.sprite.spritecollide(self.mario, self.enemies.enemies, True)

        self.rect.centerx, self.rect.centery = self.center.x, self.center.y


    def draw(self):
        self.image = self.timer.image()
        self.enemies = self.game.enemies
        self.screen.blit(self.image, (self.rect.x + self.enemies.bg_x, self.rect.y))


