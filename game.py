import pygame as pg
import game_functions as gf
from settings import Settings
from vector import Vector


class Game:
    world = pg.image.load("images/level_bg.png")

    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("Super Mario Bros.")

    def update(self):
        pass

    def draw(self):
        self.screen.blit(Game.world, (1200, 120))

    def play(self):
        self.finished = False
        while not self.finished:
            self.draw()
            gf.check_events(game=self)


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
