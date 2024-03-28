from turtle import Screen
from time import sleep
from snake import Snake
from Food import Food
from Score_Board import ScoreBoard
snake_body = []
screen = Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
serpent = Snake()
food = Food()
scoreboard = ScoreBoard()
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
    #if snake eats food
    if serpent.head.distance(food) < 15:
        food.new_spot()
        scoreboard.update()
        tail_pos = (serpent.segment[-1].xcor(),serpent.segment[-1].ycor())
        serpent.grow(tail_pos)
    # if snake goes out of play-area
    snake_body = serpent.segment[1:len(serpent.segment)-1]
    if serpent.head.xcor() > 290 or serpent.head.xcor() < -290 or serpent.head.ycor() > 290 or serpent.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
    for segment in snake_body:
        if serpent.head.distance(segment) < 5:
          game_is_on = False
          scoreboard.game_over()

screen.exitonclick()