from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Roboto", 15, "normal")


class ScoreCard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f"Current Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.goto(0, 270)
        self.clear()
        self.update_scoreboard()
