import pygame as pg
from vector import Vector
from pygame.sprite import Sprite
from timer import Timer



class Mario(Sprite):
    mario_sheet = "images/mario1.png"

    mario_running_forward = [pg.image.load("images/mario2.png"), pg.image.load("images/mario3.png"),
                             pg.image.load("images/mario4.png")]
    mario_running_backward = [pg.transform.flip(pg.image.load("images/mario2.png"), True, False),
                              pg.transform.flip(pg.image.load("images/mario3.png"), True, False),
                              pg.transform.flip(pg.image.load("images/mario4.png"), True, False)]



    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.image = pg.transform.rotozoom(pg.image.load("images/Blue_Brick.png"), 0, 3)
        self.sheet = Mario.mario_sheet


        self.image = pg.image.load(self.mario_sheet).convert_alpha()

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.center_bottom()
        self.v = Vector()
        self.movingForward = False
        self.movingBackward = False
        self.wasForward = False
        self.wasBackward= False
        self.isJumping = False

        self.forward_timer = Timer(image_list=self.mario_running_forward, delay=200, start_index=0, is_loop=True)

        self.backward_timer = Timer(image_list=self.mario_running_backward, delay=200, start_index=0, is_loop=True)
    def center_bottom(self):
        self.rect.centerx = self.screen_rect.centerx - 400
        # self.rect.bottom = self.screen_rect.bottom
        self.rect.centery = self.screen_rect.centery + 195
        self.center = Vector(self.rect.centerx, self.rect.centery)

    def inc_add(self, other):
        self.v += other

    def clamp(self):
        rw, rh = self.rect.width, self.rect.height
        srw, srb = self.screen_rect.width, self.screen_rect.bottom
        x, y = self.center.x, self.center.y

        self.center.x = min(max(x, rw / 2), srw - rw / 2)
        self.center.y = min(max(y, rh / 2), srb - rh / 2)

    def update(self):

        # if self.v.y < 1:
        #     self.inc_add(Vector(0, 1))

        self.center += self.v * self.settings.mario_speed_factor
        self.clamp()
        self.rect.centerx, self.rect.centery = self.center.x, self.center.y


    def draw(self):

        running_forward = self.forward_timer.image()
        running_backward = self.backward_timer.image()
        stand_forward = pg.image.load("images/mario1.png")
        stand_backward = pg.transform.flip(pg.image.load("images/mario1.png"), True, False)
        jump_forward = pg.image.load("images/mario5.png")
        jump_backward = pg.transform.flip(pg.image.load("images/mario5.png"), True, False)

        # print("moving Forward")
        # print(self.wasForward)
        # print(self.wasBackward)
        # print(running_backward)

        if self.isJumping:
            if self.wasBackward:
                self.screen.blit(jump_backward, self.rect)
            else:
                self.screen.blit(jump_forward, self.rect)
        elif self.movingForward:
            self.screen.blit(running_forward, self.rect)
        elif self.movingBackward:
            self.screen.blit(running_backward, self.rect)
        elif self.wasBackward:
            self.screen.blit(stand_backward, self.rect)
        else:
            self.screen.blit(stand_forward, self.rect)