import pygame as pg


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
        self.ground_brick = pg.image.load("images/Ground_Brick.png")
        self.empty_brick = pg.image.load("images/Empty_Brick.png")
        self.item_brick = pg.image.load("images/Item_brick.png")
        self.tilemap = open("tiles/world1.txt", 'r')
        self.scaling_factor = 2.5

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
                        self.screen.blit(pg.transform.rotozoom(self.ground_brick, 0, self.scaling_factor),
                                         ((self.x * 40) + self.bg_x, self.y * 40))
                    if char == 'B':
                        self.screen.blit(pg.transform.rotozoom(self.empty_brick, 0, self.scaling_factor),
                                         ((self.x * 16 * self.scaling_factor) +
                                          self.bg_x, self.y * 16 * self.scaling_factor))
                    if char == '?':
                        self.screen.blit(pg.transform.rotozoom(self.item_brick, 0, self.scaling_factor),
                                         ((self.x * 40) + self.bg_x, self.y * 40))

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
