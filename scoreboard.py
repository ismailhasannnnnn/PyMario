import pygame as pg
from mario import Mario

WHITE = (255, 255, 255)
BLUE = (0, 162, 232)

class SbElement:

    def __init__(self, screen, bg_color, ul, font, get_lives, round=True):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bg_color = bg_color
        self.ul = ul
        self.font = font
        self.round = round
        self.text_color = WHITE
        self.get_lives = get_lives
        self.update()

    def update(self):
        self.score_image = self.font.render(str(self.get_lives), True,
                                            self.text_color, self.bg_color)
        self.score_rect = self.score_image.get_rect()

    def draw(self):
        self.screen.blit(self.score_image, self.score_rect)


class Scoreboard:

    def __init__(self, game):
        self.game = game
        self.stats = game.stats
        self.screen = game.screen
        self.sr = self.screen.get_rect()
        self.bg_color = BLUE
        font = pg.font.Font("fonts/8bit.ttf", 20)

        self.lives = SbElement(screen=self.screen, bg_color=self.bg_color, ul=(self.sr.right - 40, 20), font=font, get_lives=self.stats.get_lives())

        self.update()

    def update(self):
        self.lives.update()

    def draw(self):
        self.lives.draw()



