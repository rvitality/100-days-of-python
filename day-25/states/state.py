import turtle


class State(turtle.Turtle):
    def __init__(self, state_name, coords):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(coords)

        # print(str(guessed_state.values))

        self.write(arg=state_name, font=("Courier", 10, "bold"))
