from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.pendown()
        self.color("white")
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.write(f"Score = {self.score}", False, align="center", font=("Arial", 28, "normal"))
        print(self.score)

    def score_point(self):
        self.score += 1
        self.clear()
        self.show_score()
