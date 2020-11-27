from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    snake = Snake(6)
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Escape", fun=screen.bye)
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) <= 15:
            snake.eat()
            food.eaten()
            scoreboard.score_point()
        screen.update()

    screen.exitonclick()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
