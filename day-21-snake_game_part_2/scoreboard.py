from turtle import Turtle

FONT = ("Courier", 28, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.show_score(f"Score = {self.score}")

    def show_score(self, message):
        self.write(message, False, align=ALIGNMENT, font=FONT)
        print(self.score)

    def score_point(self):
        self.score += 1
        self.clear()
        self.show_score(f"Score = {self.score}")

    def game_over(self):
        self.goto(0,0)
        self.show_score(f"GAME OVER")
