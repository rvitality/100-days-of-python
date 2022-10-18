from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUM_OF_CARS = 15


class CarManager:
    def __init__(self):
        self.cars = []
        self.add_cars()
        self.move_speed = STARTING_MOVE_DISTANCE

    def add_cars(self):
        for index in range(NUM_OF_CARS):
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setpos(
                random.randint(-300, 300),
                random.randint(-260, 280),
            )
            self.cars.append(new_car)

    def start_cars(self):
        for car in self.cars:
            # car.goto(car.xcor() - self.move_speed, car.ycor())
            car.backward(self.move_speed)

            # reset car position
            if car.xcor() < -305:
                random_x_pos = random.randint(310, 320)
                random_y_pos = random.randint(-300, 300)

                car.setpos(
                    random_x_pos,
                    random_y_pos,
                )

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
