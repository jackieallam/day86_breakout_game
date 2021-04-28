from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")
BIG_FONT = ("Courier", 40, "bold")
FULL = 3


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 350)
        self.color("white")
        self.penup()
        self.lives = FULL
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Lives: {self.lives} Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=BIG_FONT)

    def lose_a_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def next_level(self):
        self.level += 1
        self.lives = FULL
        self.update_scoreboard()
