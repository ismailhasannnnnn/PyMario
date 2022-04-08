import pygame as pg
from vector import Vector
from pygame.sprite import Sprite
from timer import Timer
from sound import Sound
from coords import Coords


class Mario(Sprite):
    mario_sheet = "images/mario1.png"




    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.image = pg.transform.rotozoom(pg.image.load("images/Blue_Brick.png"), 0, 3)
        self.sheet = Mario.mario_sheet

        self.mario_running_forward = [pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["L_M_F2"]), 0, 3),
                                 pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["L_M_F3"]), 0, 3),
                                 pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["L_M_F4"]), 0, 3),
                                pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["L_M_F3"]), 0, 3)]
        self.mario_running_backward = [
            pg.transform.flip(pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["L_M_F2"]), 0, 3), True, False),
            pg.transform.flip(pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["L_M_F3"]), 0, 3), True, False),
            pg.transform.flip(pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["L_M_F4"]), 0, 3), True, False),
            pg.transform.flip(pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["L_M_F3"]), 0, 3), True, False)]

        self.image = pg.image.load(self.mario_sheet).convert_alpha()

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.center_bottom()
        self.v = Vector()
        self.movingForward = False
        self.movingBackward = False
        self.wasForward = False
        self.wasBackward = False
        self.isJumping = False
        self.sound = Sound()
        self.y_gravity = 2
        self.jump_height = 25
        self.vel_y = self.jump_height

        self.forward_timer = Timer(image_list=self.mario_running_forward, delay=100, start_index=0, is_loop=True)

        self.backward_timer = Timer(image_list=self.mario_running_backward, delay=100, start_index=0, is_loop=True)

    def center_bottom(self):
        self.rect.centerx = self.screen_rect.centerx - 400
        # self.rect.bottom = self.screen_rect.bottom
        self.rect.centery = self.screen_rect.centery + 178

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
        self.enemies = self.game.enemies
        self.entities = self.game.entities

        collisions = pg.sprite.spritecollideany(self, self.enemies.enemies)



        if self.isJumping:
            self.center.y -= self.vel_y
            self.vel_y -= self.y_gravity
            if self.vel_y < -self.jump_height:
                self.isJumping = False
                self.vel_y = self.jump_height

        self.center += self.v * self.settings.mario_speed_factor
        self.clamp()
        self.rect.centerx, self.rect.centery = self.center.x, self.center.y
        # print(f'x: {self.rect.centerx}      y: {self.rect.centery}')

    def draw(self):

        running_forward = self.forward_timer.image()
        running_backward = self.backward_timer.image()
        stand_forward = pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["L_M_FSTAND"]), 0, 3)
        stand_backward = pg.transform.flip(pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["L_M_BSTAND"]), 0, 3), False, False)
        jump_forward = pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["L_M_FJUMP"]), 0, 3)
        jump_backward = pg.transform.rotozoom(self.game.spritesheet.image_at(Coords.coords["L_M_BJUMP"]), 0, 3)

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
