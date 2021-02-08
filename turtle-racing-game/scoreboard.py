
FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1

    def update_score(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f" Level: {self.score}", align="left", font=(FONT))


    def add_point(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER:", align="left", font=(FONT))


