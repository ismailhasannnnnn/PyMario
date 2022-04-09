import pygame as pg
from entity import Entity
from coords import Coords

class Tile():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        # self.world_tile = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.x = 0
        self.y = 0
        self.bg_x = game.bg_x
        self.ground_brick = pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["BROKEN_BRICK"]), 0, 2.5).convert_alpha()
        self.empty_brick = pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["BRICK"]), 0, 2.5).convert_alpha()
        self.item_brick = pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["?_1"]), 0, 2.5).convert_alpha()
        self.stair_brick = pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["BLOCK"]), 0, 2.5).convert()
        self.tilemap = open("tiles/world1.txt", 'r')
        self.scaling_factor = 2.5
        self.enemies = game.enemies
        self.entities = game.entities

        self.world_tile = self.tilemap.read()

        with open("tiles/world1.txt") as file:
            for line in file:
                print(line.rstrip())

    def draw(self):

        with open("tiles/world1.txt") as file:
            self.y = 0
            for line in file:
                self.x = 0
                for char in line:
                    if char == 'X':
                        self.entities.create_entity((self.x * 16 * self.scaling_factor, self.y * 16 * self.scaling_factor), self.ground_brick)
                    if char == 'B':
                        self.entities.create_entity(
                            (self.x * 16 * self.scaling_factor, self.y * 16 * self.scaling_factor), self.empty_brick)
                    if char == '?' or char == 'M':
                        self.entities.create_entity(
                            (self.x * 16 * self.scaling_factor, self.y * 16 * self.scaling_factor), self.item_brick)

                    if char == 'G':
                        self.enemies.create_goomba((self.x * 16 * self.scaling_factor, self.y * 16 * self.scaling_factor))
                    if char == 'R':
                        self.entities.create_entity(
                            (self.x * 16 * self.scaling_factor, self.y * 16 * self.scaling_factor), self.stair_brick)
                    self.x += 1
                self.y += 1

        # self.y = 0
        # for row in self.world_tile:
        #     self.x = 0
        #     for tile in row:
        #         if tile == 'X':
        #
        #             self.screen.blit(pg.transform.rotozoom(self.ground_brick, 0, 2.5),
        #                              ((self.x * 40) + self.bg_x, self.y * 40))
        #         self.x += 1
        #     self.y += 1

    def update(self):
        if self.game.scrolling:
            self.bg_x -= 8
