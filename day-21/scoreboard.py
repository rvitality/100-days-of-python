from turtle import Turtle

ALIGNMENT = "center"
FONT_LIGHT = ("Courier", 19, "normal")
FONT_BOLD = ("Courier", 19, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()

        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f"Score: {self.score}",
            align=ALIGNMENT,
            font=FONT_LIGHT,
        )

    def increase_score(self):
        self.score += 1
        self.clear()

        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "Game Over!",
            align=ALIGNMENT,
            font=FONT_BOLD,
        )
