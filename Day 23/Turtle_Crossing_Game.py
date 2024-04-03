import time
from turtle import Screen
from Player import player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint
from math import sqrt

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player_ = player()
game_is_on = True
scoreboard_ = Scoreboard()
car_spawner = CarManager()
car_spawner.create_bot_cars()
while game_is_on:
    time.sleep(0.1)
    for car in car_spawner.cars:
      car.forward(1+(scoreboard_.level**2))
    difficulty = 10-round(sqrt(scoreboard_.level))
    spawn_now = randint(0,difficulty)
    if spawn_now == 1:
        car_spawner.create_bot_cars()
    for car_check in car_spawner.cars:
        if player_.distance(car_check) < 25:
            scoreboard_.game_over()
            game_is_on = False
    screen.update()
    screen.listen()
    screen.onkey(key="Up",fun=player_.move)
    if player_.ycor() > 290:
        scoreboard_.update_level()
        player_.reset_()
screen.exitonclick()