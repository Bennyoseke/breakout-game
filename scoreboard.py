from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(100, 250)
        self.write(f"Score: {self.score}/50", font=("Courier", 30, "normal"))


    def point(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        self.update_scoreboard()