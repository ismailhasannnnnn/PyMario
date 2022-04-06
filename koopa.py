import pygame as pg
from vector import Vector
from coords import Coords
from enemy import Enemy

class Koopa(Enemy):

    koopa1_rect = Coords.coords["KOOPA_1"]
    koopa2_rect = Coords.coords["KOOPA_2"]
    koopa3_rect = Coords.coords["KOOPA_3"]
    koopa4_rect = Coords.coords["KOOPA_4"]

    def __init__(self, game, ul):
        koopa_images = [pg.transform.rotozoom(game.spritesheet.image_at(Koopa.koopa1_rect), 0, 2),
                        pg.transform.rotozoom(game.spritesheet.image_at(Koopa.koopa2_rect), 0, 2)]
        super().__init__(game, ul, image_list=koopa_images, delay=300, isLoop=True)
        self.v = Vector(-1, 0)
