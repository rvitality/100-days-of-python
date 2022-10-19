from turtle import Turtle

ALIGNMENT = "center"
FONT_LIGHT = ("Courier", 19, "normal")
FONT_BOLD = ("Courier", 19, "bold")

saved_high_score = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()

        self.score = 0

        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()

        self.write(
            f"Score: {self.score}   High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT_BOLD,
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.clear()
        # self.goto(0, 0)
        if self.score > self.high_score:
            with open("data.txt", "w") as file:
                file.write(f"{self.score}")
            self.high_score = self.score

        self.score = 0
        self.write(
            f"Score: {self.score}   High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT_BOLD,
        )

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(
    #         "Game Over!",
    #         align=ALIGNMENT,
    #         font=FONT_BOLD,
    #     )
