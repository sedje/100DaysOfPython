from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from random import randint
import time


def main():
    # Setup board and its components
    game_board = Screen()
    game_board.setup(width=800, height=600)
    game_board.bgcolor("black")
    game_board.tracer(0)
    game_board.listen()
    scoreboard = Scoreboard((0, game_board.window_height()/2-40))
    paddle_one = Paddle(((game_board.window_width()/2)-40, 25))
    paddle_two = Paddle((-(game_board.window_width()/2)+40, 25))
    ball = Ball()

    # Setup generic keys
    game_board.onkey(game_board.bye, "Escape")
    game_board.onkey(ball.increase_speed, "KP_Add")
    game_board.onkey(ball.decrease_speed, "KP_Subtract")
    # Setup player keys
    game_board.onkey(paddle_one.up, "Up")
    game_board.onkey(paddle_one.down, "Down")
    game_board.onkey(paddle_two.up, "q")
    game_board.onkey(paddle_two.down, "a")

    # Run the game
    game_is_on = True
    while game_is_on:
        game_board.update()
        time.sleep(ball.game_speed)
        ball.move()

        # bounce off top/bottom wall
        if ball.ycor() > (game_board.window_height()/2-20) or ball.ycor() < -game_board.window_height()/2+20:
            ball.change_direction()

        # hit paddle
        if (ball.xcor() > game_board.window_width()/2 - 70 and paddle_one.distance(ball) < 50) or \
                (ball.xcor() < -game_board.window_width()/2 + 70 and paddle_two.distance(ball) < 50):
            ball.change_direction(True)
            # Randomly increase the game speed a little
            if randint(0, 3) == 2:
                ball.game_speed *= 0.9

        # hit back wall and score point
        if ball.xcor() > game_board.window_width()/2 - 20:
            scoreboard.update_score(1)
            ball.reset_game()
        if ball.xcor() < -game_board.window_width()/2 + 20:
            scoreboard.update_score(0)
            ball.reset_game()

    game_board.exitonclick()


if __name__ == "__main__":
    main()
