from turtle import Turtle
from config import FONT


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self._load_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(
            f"Score: {self.score}  High Score: {self.high_score}",
            align="center",
            font=FONT
        )

    def increase(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()
        self.score = 0
        self.goto(0, 260)
        self.update()

    def _load_high_score(self):
        try:
            with open("data.txt") as f:
                return int(f.read())
        except Exception:
            return 0

    def _save_high_score(self):
        with open("data.txt", "w") as f:
            f.write(str(self.high_score))
