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
    snake = Snake(16)
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
        screen.update()
        time.sleep(0.09)
        snake.move()
        if snake.head.distance(food) <= 15:
            snake.eat()
            food.eaten()
            scoreboard.score_point()
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            snake.die()
            scoreboard.game_over()
            game_is_on = False
        for segment in snake.snake[1:]:
            if snake.head.distance(segment) < 10:
                segment.color("red")
                scoreboard.game_over()
                game_is_on = False

        screen.update()

    screen.exitonclick()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
