import pygame as pg


class Sound:
    def __init__(self):
        pg.mixer.init()
        self.jump = pg.mixer.Sound('sounds/jump.mp3')


    def play_music(self, music, volume = 0.3):
        pg.mixer.music.unload()  # stop previous music playing before beginning another
        pg.mixer.music.load(music)
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.play(-1, 0.0)

    def busy(self): return pg.mixer.get_busy()

    def play_sound(self, sound): pg.mixer.Sound.play(sound)

    def play_bg(self): self.play_music('sounds/theme.mp3')

    def play_game_over(self):
        self.stop_bg()     # no more background music
        self.play_sound(self.end_theme)
        while self.busy():    # stays here until end_theme finishes playing
            pass

    def stop_bg(self): pg.mixer.music.stop()

    def play_jump(self): self.play_sound(self.jump)