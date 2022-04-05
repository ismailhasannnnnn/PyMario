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
        self.rect.x = ul[0]
        self.rect.y = ul[1]
        self.timer = Timer(self.goomba_images, 0, 500, True)
        self.screen_rect = self.screen.get_rect()

        self.v = Vector()

    def update(self):
        self.mario = self.game.mario
        self.enemies = self.game.enemies
        collisions = pg.sprite.spritecollide(self.mario, self.enemies.enemies, True)
        # print(f'Goomba: {self.rect.x}         {self.rect.y}')
        # print(collisions)

    def draw(self):
        self.image = self.timer.image()
        self.enemies = self.game.enemies
        self.screen.blit(self.image, (self.ul[0] + self.enemies.bg_x, self.ul[1]))
