from turtle import Turtle

POSITIONS = [(-370, 20), (370, 20)]


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.setposition(position)
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        self.sety(self.ycor()+20)

    def down(self):
        self.sety(self.ycor() - 20)

    def hit(self, ball):
        if self.distance(ball) < 10:
            return True
