import pygame as pg
import game_functions as gf
from settings import Settings
from stats import Stats
from mario import Mario
from vector import Vector
from menu import Menu
from scoreboard import Scoreboard
from sound import Sound


class Game:
    world = pg.image.load("images/world1.png")

    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.stats = Stats(game=self)
        self.bg_color = self.settings.bg_color
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.sb = Scoreboard(game=self)
        pg.display.set_caption("Super Mario Bros.")
        self.sound = Sound()

        self.mario = Mario(game=self)
        self.bg_x = 0
        self.scrolling = False


    def scrollBg(self):
        if self.mario.rect.centerx >= self.screen.get_rect().centerx and self.mario.movingForward:
            if (-(Game.world.get_rect().width * 2.5) + 1200) < self.bg_x: # multiplier 3.18 works
                self.bg_x -= 8
                self.scrolling = True
                # self.mario.v = Vector(0, self.mario.v.y)
                self.mario.v.x = 0
            else:
                self.bg_x = (-(Game.world.get_rect().width * 2.5) + 1200)
                self.scrolling = False
                self.mario.v.x = 1
        self.scrolling = False

    def update(self):
        self.scrollBg()
        self.sb.update()
        self.mario.update()


    def draw(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(pg.transform.rotozoom(Game.world, 0, 2.5), (self.bg_x, 0))
        self.sb.draw()
        self.mario.draw()
        pg.display.update()

    def play(self):
        self.finished = False
        self.sound.play_bg()
        clock = pg.time.Clock()
        while not self.finished:
            self.update()
            self.draw()
            gf.check_events(game=self)
            clock.tick(1000)


def main():
    g = Game()
    menu = Menu(game=g)
    menu.show()
    g.play()


if __name__ == '__main__':
    main()
