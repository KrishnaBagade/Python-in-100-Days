from turtle import Turtle
alignment = "center"
font_type = ('Timesnewroman', 24, 'normal')
with open("Highscore.txt",mode="r") as file_:
    highscore = file_.read()
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(highscore)
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.write(arg=f"Score = {self.score} Highscore = {self.highscore} `Press 'o' to exit game.`", font=font_type, align=alignment)

    def update(self):
        """Updates the score when the snake eats food balls."""
        self.score += 1
        self.clear()
        self.write(arg=f"Score = {self.score} Highscore = {self.highscore} `Press 'o' to exit game.`", font=font_type, align=alignment)

    def game_over(self):
        """Shows the Game Over screen when the Game ends."""
        self.goto(x=0, y=0)
        self.write(arg="Game Over", font=font_type, align=alignment)

    def reset_(self):
        if self.highscore < self.score:
            self.highscore = self.score
            with open("Highscore.txt",mode="w") as file_a:
                file_a.write(f"{self.highscore}")
        self.score = 0
        self.update()
