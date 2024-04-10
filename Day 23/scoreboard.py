from turtle import Turtle
FONT = ("Courier", 30, "normal")
with open("highscore.txt",mode="r") as file:
    highscore = file.read()
highest_level = int(highscore)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.highscore = highest_level
        self.hideturtle()
        self.penup()
        self.goto(x=-290,y=270)
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.goto(x=-290, y=270)
        self.write(arg=f"Level: {self.level} High_Score: {self.highscore}",font=FONT)

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(x=-90,y=0)
        self.write(arg="Game Over!",font=FONT)


