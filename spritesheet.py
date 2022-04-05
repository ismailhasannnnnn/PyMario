import pygame as pg

class SpriteSheet:

    def __init__(self, filename):

        try:
            self.sheet = pg.image.load(filename).convert_alpha()
        except pg.error as e:
            print("Unable to load spriteshet")
            raise SystemExit(e)


    def image_at(self, rect, colorKey = None):
        rect = pg.Rect(rect)
        image = pg.Surface(rect.size, pg.SRCALPHA)
        image.blit(self.sheet, (0, 0), rect)
        if colorKey is not None:
            if colorKey is -1:
                colorKey = image.get_at((0, 0))
            image.set_colorkey(colorKey, pg.RLEACCEL)

        return image

    def images_at(self, rects, colorKey = None):
        return [self.image_at(rect, colorKey) for rect in rects]

    def load_strip(self, rect, image_count, colorKey = None):
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3]) for x in range(image_count)]
        return self.images_at(tups, colorKey)
