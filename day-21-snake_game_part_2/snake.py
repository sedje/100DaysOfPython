from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, length):
        self.length = length
        self.snake = []
        self.add_segments(length)
        self.head = self.snake[0]

    def add_segments(self, length):
        for i in range(length):
            self.snake.append(Turtle("square"))
            self.snake[i].color("white")
            self.snake[i].penup()
            self.snake[i].setx(-int(i * 20))

    def eat(self):
        t = Turtle("square")
        self.snake.append(t)
        self.snake[-1].setx(self.snake[-2].xcor() - 20)

    def move(self):
        for element in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[element - 1].xcor()
            new_y = self.snake[element - 1].ycor()
            self.snake[element].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def die(self):
        for element in self.snake:
            element.color("red")
        print(len(self.snake))
