from turtle import Screen
from time import sleep
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
serpent = Snake()
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    serpent.move()
    screen.listen()
    screen.onkey(key="Left", fun=serpent.left)
    screen.onkey(key="Right", fun=serpent.right)
    screen.onkey(key="Up", fun=serpent.up)
    screen.onkey(key="Down", fun=serpent.down)
screen.exitonclick()