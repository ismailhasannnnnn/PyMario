import pygame as pg
import sys
from mario import Mario
from vector import Vector
from button import Button


GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)
ORANGE = (217, 91, 13)


class Menu:

    menu_bg = pg.transform.rotozoom(pg.image.load("images/menu_bg.png"), 0, 0.65)

    def __init__(self, game):
        self.hover = False
        self.screen = game.screen
        self.menu_finished = False
        self.highscore = game.stats.get_highscore()

        headingFont = pg.font.Font("fonts/8bit.ttf", 80)
        subheadingFont = pg.font.Font("fonts/8bit.ttf", 50)
        font = pg.font.Font("fonts/8bit.ttf", 20)

        strings = [('SUPER', WHITE, headingFont), ('MARIO', WHITE, headingFont), ('BROS.', WHITE, subheadingFont),
                   (f'HIGH SCORE = {self.highscore:}', GREEN, font)]

        self.texts = [self.get_text(msg=s[0], color=s[1], msg_font=s[2]) for s in strings]

        self.posns = [100, 230, 340, 420]

        centerx = self.screen.get_rect().centerx

        self.play_button = Button(self.screen, "START GAME", ul=(centerx - 125, 500))

        n = len(self.texts)
        self.rects = [self.get_text_rect(text=self.texts[i], centerx=centerx, centery=self.posns[i]) for i in range(n)]

    def get_text(self, msg_font, msg, color): return msg_font.render(msg, True, color, ORANGE)

    def get_text_rect(self, text, centerx, centery):
        rect = text.get_rect()
        rect.centerx = centerx
        rect.centery = centery
        return rect




    def mouse_on_button(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        return self.play_button.rect.collidepoint(mouse_x, mouse_y)

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            if e.type == pg.KEYUP and e.key == pg.K_p:  # pretend PLAY BUTTON pressed
                self.menu_finished = True
            elif e.type == pg.MOUSEBUTTONDOWN:
                if self.mouse_on_button():
                    self.menu_finished = True
            elif e.type == pg.MOUSEMOTION:
                if self.mouse_on_button() and not self.hover:
                    self.play_button.toggle_colors()
                    self.hover = True
                elif not self.mouse_on_button() and self.hover:
                    self.play_button.toggle_colors()
                    self.hover = False

    def update(self):
        pass

    def show(self):
        while not self.menu_finished:
            self.update()
            self.draw()
            self.check_events()

    def draw_text(self):
        n = len(self.texts)
        for i in range(n):
            self.screen.blit(self.texts[i], self.rects[i])

    def draw(self):
        self.screen.blit(Menu.menu_bg, (0,-60))
        self.draw_text()
        self.play_button.draw()
        pg.display.flip()

