import os


class Stats:

    def __init__(self, game):
        self.game = game

        self.settings = game.settings
        self.reset_stats()

        self.lives = 3
        self.score = 0
        self.high_score = self.load_high_score()

    def __del__(self):
        self.save_high_score()

    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read())
        except:
            return 0

    def save_high_score(self):
        try:
            with open("highscore.txt", "w+") as f:
                f.write(str(round(self.high_score, -1)))
        except:
            print("highscore.txt not found")

    def get_score(self):
        return self.score

    def get_highscore(self):
        return self.high_score

    def get_lives(self):
        return self.lives

    def death(self):
        self.lives -= 1

    def reset_stats(self):
        pass

