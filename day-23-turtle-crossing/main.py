import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600


def main():
    screen = Screen()
    screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    screen.tracer(0)
    draw_safe_zones()
    new_player = Player()
    level = Scoreboard((-(WINDOW_WIDTH / 2 - 80), WINDOW_HEIGHT / 2 - 40))
    car_man = CarManager((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.onkey(new_player.move, "Up")
    screen.onkey(screen.bye, "Escape")
    screen.colormode(255)
    screen.bgcolor((99, 98, 99))

    game_is_on = True
    while game_is_on:
        screen.listen()
        screen.update()
        time.sleep(0.1)
        car_man.move(level.get_level())
        if new_player.safe():
            new_player.restart()
            level.update_score()

        if car_man.check_collision(new_player):
            level.game_over()
            game_is_on = False

        if randint(0, 3) == 2:
            car_man.add_car()

    screen.exitonclick()

def draw_safe_zones():
    safe_zones = ["bottom", "top"]
    for zone in safe_zones:
        index = safe_zones.index(zone)
        zone = Turtle()
        zone.color("blue")
        zone.shape("square")
        zone.penup()

        if index == 0:
            zone.shapesize(stretch_wid=4, stretch_len=30)
            zone.setposition(0, -(WINDOW_HEIGHT / 2))

        else:
            zone.shapesize(stretch_wid=4, stretch_len=20)
            zone.setposition(100, (WINDOW_HEIGHT / 2))


if __name__ == "__main__":
    main()
