from turtle import Turtle

FONT = ("Courier", 20, "normal")
FONT_LARGE = ("Courier", 25, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-240, 240)
        self.hideturtle()

        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f"Level: {self.level}",
            font=FONT,
        )

    def update_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align="center",
            font=FONT_LARGE,
        )
