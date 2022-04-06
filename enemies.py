import pygame as pg
from vector import Vector
from goomba import Goomba
from koopa import Koopa
from pygame.sprite import Sprite, Group

class Enemies:

    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.bg_x = game.bg_x

        self.enemies = Group()


    def create_goomba(self, ul):
        goomba = Goomba(self.game, ul)
        self.enemies.add(goomba)

    def create_koopa(self, ul):
        koopa = Koopa(self.game, ul)
        self.enemies.add(koopa)


    def update(self):

        if self.game.scrolling:
            self.bg_x -= 8

        for enemy in self.enemies:
            enemy.update()

    def draw(self):

        for enemy in self.enemies:
            enemy.draw()

