from turtle import Screen
from time import sleep
from paddle_command import paddle
from ball_class import Ball
from Score_Board import ScoreBoard
from random import choice

game_speed = 0.1
direction_l = [225,135]
direction_r = [45,315]
screen = Screen()
r_paddle = paddle((380,0))
l_paddle = paddle((-390,0))
screen.tracer(0)
screen.title(titlestring="Pong-Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor("black")
pong_ball = Ball()
scoreboard = ScoreBoard()
#For the create paddle method use position and position_1 for making paddle of p1 and p2
game_is_on = True
while game_is_on:
    screen.update()
    sleep(game_speed)
    pong_ball.move()
    pong_ball.collision_with_wall()
    # pong_ball.collision_with_paddle(l_paddle)
    # pong_ball.collision_with_paddle(r_paddle)
    if pong_ball.distance(r_paddle) < 50:
        #pong_ball.angle_increase()
        #pong_ball,speed_increment()
        pong_ball.left(90)
        #game_speed *= 0.9
    elif pong_ball.distance(l_paddle) < 50:
        # pong_ball.angle_increase()
        # pong_ball,speed_increment()
        # game_speed *= 0.9
        pong_ball.left(90)
    if pong_ball.xcor() > 390:
        scoreboard.left_scores_point()
        #game_speed = 0.1
        pong_ball.home()
        ball_rolling = choice(direction_l)
        pong_ball.setheading(ball_rolling)
    elif pong_ball.xcor() < -390:
        scoreboard.right_scores_point()
        #game_speed = 0.1
        pong_ball.home()
        ball_rolling = choice(direction_r)
        pong_ball.setheading(ball_rolling)
    screen.listen()
    screen.onkey(key="Up", fun=r_paddle.move_up)
    screen.onkey(key="Down", fun=r_paddle.go_down)
    screen.onkey(key="w", fun=l_paddle.move_up)
    screen.onkey(key="s", fun=l_paddle.go_down)
    # screen.onkey(key="e",fun=screen.bye)
screen.exitonclick()
