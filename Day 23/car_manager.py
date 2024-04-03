from turtle import Turtle
from random import choice,randint
from scoreboard import Scoreboard
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
score = Scoreboard()

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []

    def create_bot_cars(self):
        for bot in range(score.level):
            car = Turtle()
            car.color(choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(x=290, y=randint(-250, 260))
            car.setheading(180)
            self.cars.append(car)
            # for car_check in self.cars:
            #     if self.distance(car_check) < 15:
            #         self.clear()
            #         car.goto(x=290, y=randint(-250, 260))

    def car_move(self):
        self.forward(STARTING_MOVE_DISTANCE)