import pygame as pg
from vector import Vector
from coords import Coords
from enemy import Enemy

class Goomba(Enemy):

    goomba1_rect = Coords.coords["GOOMBA_1"]
    goomba2_rect = Coords.coords["GOOMBA_2"]



    def __init__(self, game, ul):
        goomba_images = [pg.transform.rotozoom(game.spritesheet.image_at(Goomba.goomba1_rect), 0, 2.5),
                         pg.transform.rotozoom(game.spritesheet.image_at(Goomba.goomba2_rect), 0, 2.5)]
        super().__init__(game, ul, image_list=goomba_images, delay=500, isLoop=True)
        self.v = Vector(-4, 0)


    def collision_check(self):
        collision_tolerance = 10
        if self.rect.colliderect(self.mario.rect):
            if abs(self.mario.rect.bottom - self.rect.top) < 10:
                self.kill()
            else:
                self.mario.kill()

