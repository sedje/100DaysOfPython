from turtle import Turtle
from random import choice

TOP_RIGHT = 45
TOP_LEFT = 135
BOTTOM_LEFT = 225
BOTTOM_RIGHT = 315
DIRECTIONS = [TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.game_speed = 0.05
        self.speed("fastest")
        self.color("white")
        self.setheading(choice(DIRECTIONS))

    def move(self):
        self.forward(10)

    def change_direction(self, paddle=False):
        if paddle:
            if self.heading() == TOP_RIGHT:
                self.setheading(TOP_LEFT)
            elif self.heading() == TOP_LEFT:
                self.setheading(TOP_RIGHT)
            elif self.heading() == BOTTOM_LEFT:
                self.setheading(BOTTOM_RIGHT)
            else:
                self.setheading(BOTTOM_LEFT)
        else:
            if self.heading() == TOP_RIGHT:
                self.setheading(BOTTOM_RIGHT)
            elif self.heading() == TOP_LEFT:
                self.setheading(BOTTOM_LEFT)
            elif self.heading() == BOTTOM_LEFT:
                self.setheading(TOP_LEFT)
            else:
                self.setheading(TOP_RIGHT)

    def reset_game(self):
        self.hideturtle()
        self.clear()
        self.goto(0, 0)
        self.game_speed = 0.05
        self.showturtle()
        self.setheading(choice(DIRECTIONS))

    def increase_speed(self):
        if self.game_speed < 40:
            self.game_speed *= 0.9
            print(f"game speed now: {self.game_speed}")

    def decrease_speed(self):
        if self.game_speed > 0:
            self.game_speed /= 0.9
            print(f"game speed now: {self.game_speed}")
