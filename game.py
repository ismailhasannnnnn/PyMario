import pygame as pg
import game_functions as gf
from settings import Settings
from stats import Stats
from mario import Mario
from menu import Menu
from scoreboard import Scoreboard
from sound import Sound
from spritesheet import SpriteSheet
from enemies import Enemies
from tilemap import Tile
from entity import Entities


class Game:



    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.stats = Stats(game=self)
        self.bg_color = self.settings.bg_color
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.sb = Scoreboard(game=self)
        pg.display.set_caption("Super Mario Bros.")
        self.sound = Sound()
        self.world = pg.image.load("images/level_bg.png").convert_alpha()
        self.filename = "images/allsprites.png"
        self.spritesheet = SpriteSheet(filename=self.filename)
        self.bg_x = 0
        self.mario = Mario(game=self)
        self.enemies = Enemies(game=self)
        self.entities = Entities(game=self)
        self.tile = Tile(game=self)
        self.scrolling = False

        self.enemies.create_goomba(ul=(1300, 485))
        self.enemies.create_koopa(ul=(600, 470))
        self.enemies.create_plant(ul=(800, 470))

        self.tile.draw()

        # self.enemies.create_goomba(ul=(1340, 485))


    def scrollBg(self):
        if self.mario.rect.centerx >= self.screen.get_rect().centerx and self.mario.movingForward:
            if (-(self.world.get_rect().width * 2.5) + 1200) < self.bg_x: # multiplier 3.18 works
                self.bg_x -= 8
                self.scrolling = True
                # self.mario.v = Vector(0, self.mario.v.y)
                self.mario.v.x = 0
            else:
                self.bg_x = (-(self.world.get_rect().width * 2.5) + 1200)
                self.scrolling = False
                self.mario.v.x = 1
        if not self.mario.movingForward or self.mario.movingBackward:
            self.scrolling = False


    def update(self):
        self.scrollBg()
        self.sb.update()
        self.mario.update()
        self.enemies.update()
        self.tile.update()
        self.entities.update()
        # print(f'Mario: {self.mario.rect.x}         {self.mario.rect.y}')
        # print(f'Mario: {self.mario.rect.x}         {self.mario.rect.y}')
        # print(self.scrolling)


    def draw(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(pg.transform.rotozoom(self.world, 0, 2.5), (self.bg_x, 0))
        self.sb.draw()
        self.mario.draw()
        self.enemies.draw()
        self.entities.draw()
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
