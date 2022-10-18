import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()
    # print("x: ", ball.xcor())
    # print("y: ", ball.ycor())

    # detect collision on upper/lower walls
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # detect collision with paddles
    if (
        ball.distance(right_paddle) <= 40
        and ball.xcor() >= 330
        or ball.distance(left_paddle) <= 40
        and ball.xcor() >= -330
    ):
        ball.bounce_x()

    # left player wins
    if ball.xcor() >= 400:
        scoreboard.update_scores(1, 0)
        ball.reset_position()

    if ball.xcor() <= -400:
        # right player wins
        scoreboard.update_scores(0, 1)
        ball.reset_position()

screen.exitonclick()
