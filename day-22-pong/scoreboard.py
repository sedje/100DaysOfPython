from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 32, "bold")


class Scoreboard(Turtle):

    def __init__(self, positions):
        super().__init__()
        self.player1 = 0
        self.player2 = 0
        self.penup()
        self.goto(positions)
        self.color("white")
        self.hideturtle()
        self.write(f"{self.player1}   {self.player2}", align=ALIGNMENT, font=FONT)

    def update_score(self, who_scored):
        self.clear()
        if who_scored == 1:
            self.player1 += 1
        else:
            self.player2 += 1
        self.write(f"{self.player1}   {self.player2}", align=ALIGNMENT, font=FONT)
