import random
from turtle import Screen, Turtle, colormode

import Color_Used


def making_dots():
  for row in range(10):
    drake.setpos(-200,(-200+(50*row)))
    for _ in range(10):
      drake.dot(20,Color_Used.v[random.randint(0,30)])
      drake.forward(50)


colormode(255)
drake = Turtle()
drake.shape("arrow")
drake.penup()
drake.hideturtle()
making_dots()
screen = Screen()
screen.exitonclick()
