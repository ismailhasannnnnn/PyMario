import pygame as pg
from vector import Vector
from pygame.sprite import Sprite
from timer import Timer



class Mario(Sprite):
    mario_sheet = "images/mario1.png"
    mario_images = [pg.image.load("images/mario2.png"), pg.image.load("images/mario3.png"),
                    pg.image.load("images/mario4.png")]

    is_running = False

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.sheet = Mario.mario_sheet


        self.image = pg.image.load(self.mario_sheet).convert_alpha()

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.center_bottom()
        self.v = Vector()

        self.timer = Timer(image_list=self.mario_images, delay=200, start_index=0, is_loop=True)

    def center_bottom(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = Vector(self.rect.centerx, self.rect.centery)

    def inc_add(self, other):
        self.v += other

    def update(self):
        self.center += self.v * self.settings.mario_speed_factor
        self.rect.centerx, self.rect.centery = self.center.x, self.center.y

    def draw(self):

        running = self.timer.image()
        stand = pg.image.load("images/mario1.png")

        if self.is_running:
            self.screen.blit(running, self.rect)
        else:
            self.screen.blit(stand, self.rect)


