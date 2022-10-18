import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)


bob = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.onkey(bob.move_up, "Up")
# screen.onkey(bob.move_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    time.sleep(0.1)
    screen.update()

    car_manager.start_cars()

    # check if player reaches finish line
    if bob.ycor() >= 295:
        bob.reset_position()

        scoreboard.update_level()
        car_manager.increase_speed()

    # detect check car collision
    for car in car_manager.cars:
        if bob.distance(car) <= 20:
            scoreboard.game_over()
            game_is_on = False
            break


screen.exitonclick()
