from turtle import Screen, Turtle


def forward():
  rayleigh.forward(10)

def backward():
  rayleigh.backward(10)

def clockwise():
  rayleigh.left(+10)

def counterclockwise():
   rayleigh.right(+10)

def clear():
    rayleigh.clear()
    rayleigh.penup()
    rayleigh.home()
    rayleigh.pendown()


rayleigh = Turtle()
rayleigh.shape("arrow")
screen = Screen()
screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s",fun=backward)
screen.onkeypress(key="a",fun=clockwise)
screen.onkeypress(key="d",fun=counterclockwise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()
