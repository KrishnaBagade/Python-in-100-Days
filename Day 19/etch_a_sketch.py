from turtle import Screen, Turtle


def forward():
  rayleigh.setheading(0)
  rayleigh.forward(10)

def backward():
  rayleigh.setheading(180)
  rayleigh.forward(10)

def clockwise():
  rayleigh.tilt(+1)

def counterclockwise():
   rayleigh.tilt(-1)


rayleigh = Turtle()
rayleigh.shape("arrow")
screen = Screen()
screen.listen()
screen.onkeypress(key="W", fun=forward)
screen.onkey(key="S", fun=backward)
screen.onkey(key="A", fun=clockwise)
screen.onkey(key="D",fun=counterclockwise)

screen.exitonclick()



