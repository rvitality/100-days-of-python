import random
from turtle import Screen, Turtle

colors = ["red", "green", "purple", "blue", "orange", "brown"]

screen = Screen()
screen.setup(width=500, height=400)
user_color_choice = screen.textinput(
    "Make your bet!", prompt="Which turtle will win the race? Enter turtle color: "
).lower()

turtles = []
y_pos = 100
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_pos)
    y_pos -= 40
    turtles.append(new_turtle)

is_race_on = True
winning_color = ""
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            break

        turtle.forward(random.randint(0, 10))

screen.exitonclick()

if user_color_choice == winning_color:
    print(f"You've won! Winning turtle: {winning_color}")
else:
    print(f"You've lost! Winning turtle: {winning_color}")
