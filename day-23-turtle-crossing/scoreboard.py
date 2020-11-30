from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.setposition(position)
        self.write(f"Level: {self.level}", font=FONT, align=ALIGNMENT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.clear()
        self.color("red")
        self.write(f"Level: {self.level}", font=FONT, align=ALIGNMENT)
        t = Turtle()
        t.hideturtle()
        t.write(f"GAME OVER", font=FONT, align=ALIGNMENT)

    def get_level(self):
        return self.level