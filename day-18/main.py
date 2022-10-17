import random
import turtle as t

colors = [
    (237, 224, 80),
    (205, 4, 73),
    (236, 50, 130),
    (198, 164, 8),
    (111, 179, 218),
    (204, 75, 12),
    (219, 161, 103),
    (234, 224, 4),
    (11, 23, 63),
    (29, 189, 111),
    (22, 107, 174),
    (16, 28, 177),
    (216, 134, 179),
    (8, 186, 216),
    (229, 167, 200),
    (210, 25, 148),
    (122, 190, 160),
    (7, 49, 26),
    (34, 136, 72),
    (63, 20, 7),
    (126, 219, 234),
    (190, 14, 4),
    (109, 87, 215),
    (140, 217, 202),
    (238, 64, 34),
    (71, 10, 28),
]

bob = t.Turtle()
bob.shape("turtle")
bob.penup()


t.colormode(255)

bob.setpos(-250, -150)
# bob.hideturtle()
bob.speed("fastest")

directions = [0, 90, 180, 270]

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)

#     return (r, g, b)


num_dots = 100
corner = 1

for index in range(1, num_dots + 1):
    bob.dot(20, random.choice(colors))
    bob.forward(50)

    # corner
    if index % 10 == 0:

        # print("turn right")
        if (index / 10) % 2 == 0:
            # turn right
            bob.right(90)
            bob.forward(50)
            bob.right(90)
            bob.forward(50)
        else:
            # print("turn left")
            bob.left(90)
            bob.forward(50)
            bob.left(90)
            bob.forward(50)


screen = t.Screen()
screen.exitonclick()
