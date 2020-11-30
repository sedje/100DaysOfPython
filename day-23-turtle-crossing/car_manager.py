from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, screen_size):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(screen_size)
        self.screen_size = screen_size
        self.lanes = []
        self.cars = []
        self.num_lanes = int((screen_size[1]-80)/40)
        print(self.num_lanes)
        for lane in range(self.num_lanes):
            self.lanes.append([lane, []])

    def add_car(self):
        lane_to_add = self.lanes[randint(0, len(self.lanes)-1)][0]
        position = (-(self.screen_size[0]/2), -(self.screen_size[1]/2-60)+(lane_to_add*40))
        newCar = Turtle()
        newCar.shape("square")
        newCar.penup()
        newCar.color(choice(COLORS))
        newCar.setposition(position)
        newCar.shapesize(stretch_wid=1, stretch_len=2)
        self.cars.append(newCar)

    def move(self, level):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE+(MOVE_INCREMENT*level))

    def check_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False
