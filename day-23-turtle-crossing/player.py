from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 40
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.color("orange")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.restart()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.setposition(STARTING_POSITION)

    def safe(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False
