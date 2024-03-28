from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.home()
        self.angle_increase = 0
        self.setheading(45+self.angle_increase)
        self.speed_increase = 1
        #self.speed(1+self.speed_increase)
        self.speed(0)

    def move(self):
        self.forward(20)

    def collision_with_wall(self):
        if self.ycor() > 280 or self.ycor() < -270:
            self.left(120)

    def speed_increment(self):
        self.speed_increase += 0.5

    def ball_direction_change(self):
        self.angle_increase += 10

    #def collision_with_paddle(self,paddle):
        #paddle_size_x = (paddle.ycor()-20,paddle.ycor(),paddle.ycor()+20)
        #paddle_size_y = (paddle.xcor()-20,paddle.xcor(),paddle.xcor()+20)
        #for paddle_space in range(len(paddle_size_x)-1):
