from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def turn_left():
    tim.left(5)


def turn_right():
    tim.right(5)


def reset():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def exit_screen():
    screen.bye()


def main():
    screen.listen()
    screen.onkey(key="Down", fun=move_backwards)
    screen.onkey(key="Up", fun=move_forwards)
    screen.onkey(key="Left", fun=turn_left)
    screen.onkey(key="Right", fun=turn_right)
    screen.onkey(key="Escape", fun=exit_screen)
    screen.onkey(key="c", fun=reset)
    screen.exitonclick()


if __name__ == "__main__":
    main()