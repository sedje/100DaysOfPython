import colorgram
import random
from turtle import Turtle, Screen

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]


def new_position(turtle_object, x, y):
    turtle_object.penup()
    turtle_object.setpos(x, y)
    turtle_object.pendown()


def draw_circles(turtle_object):
    new_position(turtle_object, -200,200)
    color = 0
    for i in range(10):
        for j in range(10):
            turtle_object.dot(20, random.choice(color_list))
            turtle_object.penup()
            turtle_object.forward(50)
            if color+1 == len(color_list):
                color = 0
            else:
                color += 1
        turtle_object.back((10*50))
        turtle_object.right(90)
        turtle_object.forward(50)
        turtle_object.left(90)

def main():
    timmy = Turtle()
    screen = Screen()
    screen.colormode(255)
    timmy.shape("turtle")
    timmy.color("green")
    timmy.speed(100)
    draw_circles(timmy)
    screen.exitonclick()

def get_colors():
    rgb_colors = []
    colors = colorgram.extract('image.jpg', 30)
    # for color in colors:
    #     r = color.rgb.r
    #     g = color.rgb.g
    #     b = color.rgb.b
    #     new_color = (r, g, b)
    #     rgb_colors.append(new_color)

    # print(rgb_colors)


if __name__ == "__main__":
    main()