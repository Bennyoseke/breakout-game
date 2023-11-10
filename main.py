from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Hit Game")
screen.tracer(0)


paddle = Paddle((0, -250))
ball = Ball()
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for row in range(5):
    for col in range(10):
        brick = Brick(random.choice(colors), col, row)
        bricks.append(brick)

score = Scoreboard()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")


while True:
    screen.update()
    ball.move()


    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.ycor() < -300:
        for brick in bricks:
            brick.hideturtle()

        bricks = []

        colors = ["red", "orange", "yellow", "green", "blue"]
        for row in range(5):
            for col in range(10):
                brick = Brick(random.choice(colors), col, row)
                bricks.append(brick)

        ball.reset_position()
        score.reset()


    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.bounce_x()



    if (ball.ycor() < -250) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.bounce_y()

    for brick in bricks:
        if (
                (brick.xcor() - 30 < ball.xcor() < brick.xcor() + 30) and
                (brick.ycor() - 10 < ball.ycor() < brick.ycor() + 10)
        ):
            brick.hideturtle()
            score.point()
            ball.bounce_x()
            bricks.remove(brick)




screen.exitonclick()