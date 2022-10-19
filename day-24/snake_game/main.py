import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) <= 15:
        food.refresh()
        snake.extend_tail()
        scoreboard.increase_score()

    # detect collision with wall
    if (
        snake.head.xcor() >= 295
        or snake.head.xcor() <= -295
        or snake.head.ycor() >= 295
        or snake.head.ycor() <= -295
    ):
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
