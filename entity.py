import pygame as pg
from pygame.sprite import Sprite, Group
from vector import Vector

class Entities:

    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.entities = Group()

    def create_entity(self, ul, image):
        entity = Entity(self.game, ul, image)
        self.entities.add(entity)

    def update(self):

        for entity in self.entities:
            entity.update()

    def draw(self):

        for entity in self.entities:
            entity.draw()

class Entity(Sprite):

    def __init__(self, game, ul, image):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.ul = ul
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = ul

    def update(self):
        self.mario = self.game.mario
        self.enemies = self.game.enemies
        self.center = Vector(self.rect.centerx, self.rect.centery)

    def draw(self):
        self.enemies = self.game.enemies
        if -100 <= self.rect.x + self.enemies.bg_x < 1400:
            self.screen.blit(self.image, (self.rect.x + self.enemies.bg_x, self.rect.y))

