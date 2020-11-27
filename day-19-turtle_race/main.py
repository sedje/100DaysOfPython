from turtle import Turtle, Screen
from random import randint

turtles_colors = ["red", "green", "purple", "blue", "yellow", "orange"]
turtles = []


def main():
    screen = Screen()
    screen.setup(width=500, height=800)
    user_bet = turtles_colors.index(screen.textinput(title="Make your bet", prompt="Which turtle color will win?"))
    start_position = 0
    for turtle in turtles_colors:
        color = turtle
        turtle = Turtle()
        turtles.append(turtle)
        turtle.penup()
        turtle.color(color)
        turtle.shape("turtle")
        turtle.setposition(((-int(screen.window_width() / 2)+40), int(screen.window_height()/2)-50 - start_position))
        start_position += 30

    winner = race((int(screen.window_width() / 2) - 40))
    for turtle in turtles:
        print(turtles_colors[turtles.index(turtle)].title() + " finished at: " + str(turtle.position()[0]))
    check_win(winner, user_bet)


    screen.exitonclick()


def race(race_length):
    winner = None
    race_is_on = True

    while race_is_on:
        for turtle in turtles:
            turtle.forward(randint(0, 10))
            end_pos = turtle.xcor()
            if end_pos >= race_length and winner is None:
                race_is_on = False
                winner = turtles.index(turtle)

    return winner


def check_win(winner, user_bet):
    if winner == user_bet:
        print("Congratulations, You are the winner!")
    else:
        print(f"Better luck next time, {turtles_colors[winner]} has won!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
