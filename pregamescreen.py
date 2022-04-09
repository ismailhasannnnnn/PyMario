import pygame as pg
import sys
from mario import Mario
from vector import Vector
from button import Button
import time

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)
ORANGE = (217, 91, 13)


class PregameScreen:
    menu_bg = pg.transform.rotozoom(pg.image.load("images/menu_bg.png"), 0, 0.65)

    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.menu_finished = False
        self.highscore = game.stats.get_highscore()

        headingFont = pg.font.Font("fonts/8bit.ttf", 30)
        subheadingFont = pg.font.Font("fonts/8bit.ttf", 30)
        font = pg.font.SysFont(None, 48)

        strings = [('WORLD 1-1', WHITE, headingFont),
                   (f'HIGH SCORE = {self.highscore:}', WHITE, subheadingFont),
                   ]

        self.texts = [self.get_text(msg=s[0], color=s[1], msg_font=s[2]) for s in strings]

        self.posns = [100, 230, 340, 400]

        centerx = self.screen.get_rect().centerx

        self.play_button = Button(self.screen, "START GAME", ul=(centerx - 125, 500))

        n = len(self.texts)
        self.rects = [self.get_text_rect(text=self.texts[i], centerx=centerx, centery=self.posns[i]) for i in range(n)]

    def get_text(self, msg_font, msg, color): return msg_font.render(msg, True, color, BLACK)

    def get_text_rect(self, text, centerx, centery):
        rect = text.get_rect()
        rect.centerx = centerx
        rect.centery = centery
        return rect

    def show(self):
        self.draw()
        time.sleep(1)

    def draw_text(self):
        n = len(self.texts)
        for i in range(n):
            self.screen.blit(self.texts[i], self.rects[i])

    def draw(self):
        self.screen.fill(self.settings.bg_color)
        self.draw_text()
        pg.display.flip()
