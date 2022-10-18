from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 230)
        self.hideturtle()

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"{self.left_score}    {self.right_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def update_scores(self, left, right):
        self.left_score += left
        self.right_score += right
        self.update_scoreboard()
