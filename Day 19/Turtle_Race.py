from turtle import Turtle,Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
start_race = False

with open("bid_value.txt",mode="r") as file:
    bet_amount = file.read()
bid_amount = int(bet_amount)
if bid_amount <= 0:
    bid_amount += 100
user_chose = screen.textinput(title=f"Make your bet from ${bid_amount} ",prompt="Which turtle do you choose to bet on ?")
red_turtle = Turtle(shape="turtle")
red_turtle.color("red")
red_turtle.penup()
red_turtle.goto(x=-220, y=-150)
orange_turtle = Turtle(shape="turtle")
orange_turtle.color("orange")
orange_turtle.penup()
orange_turtle.goto(x=-220, y=-100)
yellow_turtle = Turtle(shape="turtle")
yellow_turtle.color("yellow")
yellow_turtle.penup()
yellow_turtle.goto(x=-220, y=-50)
green_turtle = Turtle(shape="turtle")
green_turtle.color("green")
green_turtle.penup()
green_turtle.goto(x=-220, y=0)
blue_turtle = Turtle(shape="turtle")
blue_turtle.color("blue")
blue_turtle.penup()
blue_turtle.goto(x=-220, y=50)
purple_turtle = Turtle(shape="turtle")
purple_turtle.color("purple")
purple_turtle.penup()
purple_turtle.goto(x=-220, y=100)
turtle_list = [red_turtle,orange_turtle,yellow_turtle,green_turtle,blue_turtle,purple_turtle]
turtle_speed = [0,5,10,15]
if user_chose:
    start_race = True
while start_race:
    for turtle in turtle_list:
        if turtle.xcor() > 210:
            start_race = False
            winner = turtle.pencolor()
            if winner == user_chose:
                print(f"You win! The winning turtle is {winner}.")
                bid_amount += bid_amount
            else:
                print(f"You lose! The winning turtle is {winner}.")
                bid_amount -= bid_amount
        turtle.forward(turtle_speed[randint(0,3)])
with open("bid_value.txt",mode="w") as file_:
    file_.write(f"{bid_amount}")
screen.exitonclick()
