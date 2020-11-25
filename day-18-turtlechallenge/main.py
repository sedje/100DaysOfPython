from turtle import Turtle, Screen
from random import randint


def draw_shape(turtle_object, sides):
    angle = 360 / sides
    for _ in range(sides):
        turtle_object.forward(100)
        turtle_object.right(angle)


def draw_spiro(turtle_object):
    i = 100
    while i > 0:
        for _ in range(2):
            turtle_object.forward(i)
            turtle_object.right(90)
        i -= 10


def dotted_line(turtle_object, number_of_dots):
    for _ in range(number_of_dots):
        turtle_object.forward(10)
        turtle_object.penup()
        turtle_object.forward(10)
        turtle_object.pendown()


def new_position(turtle_object, x, y):
    turtle_object.penup()
    turtle_object.setpos(x, y)
    turtle_object.pendown()


def draw_multiple(turtle_object):
    for i in range(3, 11):
        get_color(turtle_object)
        draw_shape(turtle_object, i)


def get_color(turtle_object):
    new_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    turtle_object.pencolor(new_color)


def random_walk(turtle_object, steps):
    heading = [0, 90, 180, 270]
    turtle_object.width(20)
    for step in range(steps):
        get_color(turtle_object)
        turtle_object.seth(heading[randint(0, 3)])
        turtle_object.forward(50)


def draw_full_spiro(turtle_object, number_of_circles):
    heading = turtle_object.heading()
    step_size = 360/number_of_circles
    for _ in range(number_of_circles):
        turtle_object.circle(100)
        heading += step_size
        turtle_object.seth(heading)
        get_color(turtle_object)


def turtles():
    timmy = Turtle()
    screen = Screen()
    screen.colormode(255)
    timmy.shape("turtle")
    timmy.color("green")
    timmy.speed(100)
    new_position(timmy, -200, 200)
    dotted_line(timmy, 15)
    new_position(timmy, -200, 180)
    draw_shape(timmy, 4)
    new_position(timmy, -90, 180)
    draw_spiro(timmy)
    new_position(timmy, 50, 50)
    draw_multiple(timmy)
    # random_walk(timmy, 200)
    new_position(timmy, -250, -150)
    draw_full_spiro(timmy, 20)
    screen.exitonclick()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    turtles()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
