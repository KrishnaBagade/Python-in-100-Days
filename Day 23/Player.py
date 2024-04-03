from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x=0,y=-280)
        self.setheading(90)

    def move(self):
        self.forward(20)

    def reset_(self):
        self.goto(x=0,y=-280)

