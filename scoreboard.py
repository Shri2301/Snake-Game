from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)  # Slightly lower to center better with smaller font
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.score} | High Score: {self.high_score}",
            align="center",
            font=("Courier", 14, "normal")
        )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
