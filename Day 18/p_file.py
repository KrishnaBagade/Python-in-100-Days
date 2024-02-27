from turtle import Turtle, Screen,colormode
import random


def circle():
  for i in range(4):
   leon.forward(100)
   leon.right(90)


def dashed_line(count):
  while count < 10:
    if count % 2 != 0:
      leon.pendown()
      leon.forward(10)
      count += 1
    elif count % 2 == 0:
      leon.penup()
      leon.forward(10)
      count += 1


def angle_of_shape(sides):
  angle_1 = 360/sides
  return angle_1
  

def make_shapes(sides,count):
  while count < 8:
    count += 1
    sides += 1
    angle=angle_of_shape(sides)
    leon.pencolor(random.choice(colors))
    for i in range (sides):
      leon.forward(50)
      leon.right(angle)
      

def random_walk(thickness,speed,keep_going):
  while speed < 10:
    thickness += 0.1
    speed += 0.1
    leon.setheading(random.choice(direction))
    leon.pencolor(random.choice(colors))
    leon.pensize(thickness)
    leon.forward(random.choice(distance))
    leon.speed(speed)


def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  colour_code = (r,g,b)
  #random.choice(colors)
  return colour_code
  

def spirograph(count):
  while count < 100:
    count += 1
    leon.pencolor(random_color())
    leon.speed(10)
    leon.circle(100)
    if count % 2 != 0:
      leon.backward(1)
    elif count % 2 == 0:
      leon.forward(1)
    leon.left(5)
    

colormode(255)
keep_going = True
speed = 0
thickness = 10
distance = [10,20,30,40,50,60,70,80,90]
direction = [0,90,180,270]
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
leon = Turtle()
leon.shape("arrow")
count = 0
sides = 2 
#random_walk(thickness,speed,keep_going)
#make_shapes(sides,count)
spirograph(count)
screen = Screen()
screen.exitonclick()