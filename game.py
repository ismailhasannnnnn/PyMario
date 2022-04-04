import pygame as pg
import game_functions as gf
from settings import Settings
from mario import Mario
from vector import Vector


class Game:
    world = pg.image.load("images/level_bg.png")

    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("Super Mario Bros.")
        self.mario = Mario(game=self)
        self.bg_x = 0
        self.scrolling = False


    def scrollBg(self):
        if self.mario.rect.centerx >= self.screen.get_rect().centerx and self.mario.movingForward:
            self.bg_x -= 8
            self.scrolling = True
            self.mario.v = Vector(0, self.mario.v.y)
        self.scrolling = False

    def update(self):
        self.scrollBg()
        self.mario.update()


    def draw(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(pg.transform.rotozoom(Game.world, 0, 2.4), (self.bg_x, 0))
        self.mario.draw()
        pg.display.update()

    def play(self):
        self.finished = False
        clock = pg.time.Clock()
        while not self.finished:
            self.update()
            self.draw()
            gf.check_events(game=self)
            clock.tick(144)


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
