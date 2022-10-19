from turtle import Turtle


class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def show_msg(self, content):
        self.clear()
        self.goto(0, 100)
        self.write(
            arg=content,
            align="center",
            font=("Courier", 15, "bold"),
        )

    def clear_msg(self):
        self.clear()
