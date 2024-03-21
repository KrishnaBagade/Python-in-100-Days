from turtle import Turtle
from turtle import Screen

screen = Screen()
starting_positions = [(0,0),(-20,0),(-40,0)]
Move_Distance = 20
Up = 90
Down = 270
Left = 180
Right = 0
class Snake:
    def __init__(self):
       self.segment = []
       self.create_snake()
       self.head = self.segment[0]

    def create_snake(self):
        for position in starting_positions:
            block = Turtle()
            block.shape("square")
            block.color("white")
            block.penup()
            block.goto(position)
            self.segment.append(block)

    def up(self):
        if self.head.heading() != Down:
          self.head.setheading(Up)

    def left(self):
        if self.head.heading() != Right:
          self.head.setheading(Left)

    def down(self):
        if self.head.heading() != Up:
          self.head.setheading(Down)

    def right(self):
        if self.head.heading() != Left:
          self.head.setheading(Right)

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(Move_Distance)
