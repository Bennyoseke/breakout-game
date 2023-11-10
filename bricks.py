from turtle import Turtle


class Brick(Turtle):

    def __init__(self, color, col, row):
        super().__init__()
        self.shape("square")
        self.fillcolor(color)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(-370 + col * 80, 250 - row * 30)
        self.col = col
        self.row = row