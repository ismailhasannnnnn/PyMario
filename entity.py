import pygame as pg
from pygame.sprite import Sprite, Group
from vector import Vector
from coords import Coords

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
        self.item_brick = Coords.coords["?_1"]
        for entity in self.entities:
            entity.draw()



class Entity(Sprite):

    def __init__(self, game, ul, image):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.entities = game.entities
        self.ul = ul
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = ul
        self.lastBg_x = 0
        self.mushroom = pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["MUSHROOM"]), 0,
                                          2.5).convert_alpha()

    def check_collision(self):

        # if abs(self.mario.rect.x - self.rect.x) < self.rect.w  abs(self.mario.rect.centery - self.rect.y) < self.rect.h:
        #     self.mario.v = Vector(0, 0)
        collision_tolerance = 10
        if self.rect.colliderect(self.mario.rect):
            self.mario.colliding = True
            if abs(self.mario.rect.top - self.rect.bottom) < collision_tolerance:
                print('1')
                self.entities.create_entity((self.rect.x * 16 * 2.5, (self.rect.y + 16) * 16 * 2.5), self.mushroom)
                self.entities.draw()
            if abs(self.mario.rect.bottom - self.rect.top) < collision_tolerance and self.mario.isJumping:
                print('2')
                self.mario.onGround = True
                self.mario.v.y = 0
            # if abs(self.mario.rect.left - self.rect.right) < collision_tolerance:
            #     print('3')
            #     if self.game.scrolling:
            #         self.game.canScroll = False
            #     else:
            #         self.game.scrolling = True
            #     self.mario.v.x = 0
            # if abs(self.mario.rect.right - self.rect.left) < collision_tolerance:
            #     print('4')
            #     if self.game.scrolling:
            #         self.game.canScroll = False
            #     else:
            #         self.game.scrolling = True
            #     self.mario.v.x = 0
            else:
                self.mario.onGround = False
                self.mario.colliding = False

            # if self.mario.v.x < 0:
            #     print('1')
            #     self.mario.rect.x = self.rect.x + self.rect.w
            #
            # if self.mario.v.x > 0 or self.game.scrolling:
            #     print('2')
            #     self.mario.rect.x = self.rect.x - self.rect.w
            # if self.mario.v.y < 0:
            #     print('3')
            #     self.mario.rect.y = self.rect.y + self.rect.h
            #     self.mario.v.y = 0
            # if self.mario.v.y > 0:
            #     print('4')
            #     self.mario.rect.y = self.rect.y - self.rect.h - 16
            #     self.mario.v.y = 0
        # print(self.mario.onGround)


    def update(self):
        self.mario = self.game.mario
        self.enemies = self.game.enemies
        self.check_collision()
        self.center = Vector(self.rect.centerx, self.rect.centery)

        self.difference = self.enemies.bg_x - self.lastBg_x



        self.rect.centerx += self.difference

        self.lastBg_x = self.enemies.bg_x



    def draw(self):

        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        # pg.draw.rect(self.screen, (0, 0, 0), self.rect)

