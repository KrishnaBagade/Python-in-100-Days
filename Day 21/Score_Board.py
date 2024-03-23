from turtle import Turtle
alignment = "center"
font_type = ('Timesnewroman', 24, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.write(arg=f"Score = {self.score}", font=font_type, align=alignment)

    def update(self):
        '''Updates the score when the snake eats food balls.'''
        self.score += 1
        self.clear()
        self.write(arg=f"Score = {self.score}", font=font_type, align=alignment)

    def game_over(self):
        '''Shows the Game Over screen when the Game ends.'''
        self.goto(x=0,y=0)
        self.write(arg="Game Over", font=font_type, align=alignment)
