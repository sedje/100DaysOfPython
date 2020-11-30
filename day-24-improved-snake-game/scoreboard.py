from turtle import Turtle
from os import path

FONT = ("Courier", 28, "normal")
ALIGNMENT = "center"
SCORE_FILE = 'highscore.txt'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        if path.isfile(SCORE_FILE):
            with open(SCORE_FILE, 'r') as file:
                self.highscore = int(file.readline())
        else:
            self.highscore = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score = {self.score} | Highscore = {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def score_point(self):
        self.score += 1
        self.show_score()

    def game_over(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(SCORE_FILE, 'w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.show_score()
