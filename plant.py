import pygame as pg
from vector import Vector
from coords import Coords
from enemy import Enemy

class Plant(Enemy):
    plant1_rect = Coords.coords["PLANT_1"]
    plant2_rect = Coords.coords["PLANT_2"]

    def __init__(self, game,ul):
        plant_images = [pg.transform.rotozoom(game.spritesheet.image_at(Plant.plant1_rect), 0, 2),
                        pg.transform.rotozoom(game.spritesheet.image_at(Plant.plant2_rect), 0, 2)]
        super().__init__(game, ul, image_list=plant_images, delay=500, isLoop=True)
        self.v = Vector(0, 0)

    def collision_check(self):
        self.mario = self.game.mario
        self.enemies = self.game.enemies

        collisions = pg.sprite.spritecollide(self.mario, self.enemies.enemies, False)
        if(len(collisions) > 0):
            # self.game.mario.
