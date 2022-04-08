import pygame as pg
from vector import Vector
from coords import Coords
from enemy import Enemy

class Fireball(Enemy):

    fire_ball = Coords.coords["FIREBALL"]

    def __init__(self, game, ul):
        goomba_images = [pg.transform.rotozoom(game.spritesheet.image_at(Fireball.fire_ball), 0, 2.5),
                         ]
        super().__init__(game, ul, image_list=goomba_images, delay=500, isLoop=True)
        self.v = Vector(32, 6)
