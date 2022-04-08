import sys
import pygame as pg
from vector import Vector
from mario import Mario
from sound import Sound

LEFT, RIGHT, UP, DOWN, STOP = 'left', 'right', 'up', 'down', 'stop'

dirs = {LEFT: Vector(-1, 0),
        RIGHT: Vector(1, 0),
        UP: Vector(0, -1),
        DOWN: Vector(0, 1),
        STOP: Vector(0, 0)}

dir_keys = {pg.K_LEFT: LEFT, pg.K_a: LEFT,
            pg.K_RIGHT: RIGHT, pg.K_d: RIGHT,
            pg.K_UP: UP, pg.K_w: UP,
            pg.K_DOWN: DOWN, pg.K_s: DOWN}

def check_events(game):

    mario = game.mario

    for e in pg.event.get():
        if e.type == pg.QUIT:
            game.finished = True
        elif e.type == pg.KEYDOWN:
            if e.key in dir_keys:
                v = dirs[dir_keys[e.key]]
                if v == Vector(1, 0):
                    game.mario.movingForward = True
                    game.mario.wasBackward = False
                elif v == Vector(-1, 0):
                    game.mario.movingBackward = True
                    game.mario.wasBackward = True

                mario.inc_add(v)
            if e.key == pg.K_SPACE:
                if not mario.isJumping:
                    Sound.play_jump(Sound())
                mario.isJumping = True

            if e.key == pg.K_k:
                # game.entities.create_entity((mario.rect.centerx + game.enemies.bg_x, mario.rect.centery), pg.image.load("images/mario1.png"))
                game.enemies.create_fireball((mario.rect.centerx - game.enemies.bg_x, mario.rect.centery - 40))

        elif e.type == pg.KEYUP:
            if e.key in dir_keys:
                v = dirs[dir_keys[e.key]]
                if mario.v == Vector(0, 0):
                    mario.v = Vector(0, 0)
                else:
                    mario.inc_add(-v)
                if v == Vector(1, 0):
                    game.mario.movingForward = False

                elif v == Vector(-1,0):
                    game.mario.movingBackward = False

            # if e.key == pg.K_SPACE and mario.isJumping is True:
            #     mario.isJumping = False
