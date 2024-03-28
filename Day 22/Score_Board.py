from turtle import Turtle

Font = ("TimesNewRoman", 70, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.goto(-100, 180)
        self.write(self.score_l, align="center", font=Font)
        self.goto(100, 180)
        self.write(self.score_r, align="center", font=Font)

    def change_score(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.score_l, font=Font)
        self.goto(100, 180)
        self.write(self.score_r, font=Font)

    def left_scores_point(self):
        self.score_l += 1
        self.change_score()

    def right_scores_point(self):
        self.score_r += 1
        self.change_score()
