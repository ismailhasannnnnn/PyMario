import sys
import pygame as pg
from vector import Vector

def check_events(game):
    for e in pg.event.get():
        print(e.type)
        if e.type == pg.QUIT:
            game.finished = True