from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 8, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def hightscore(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()

    # def game_over(self):
    # self.goto(0, 0)
    # self.write("game over!", align=ALIGNMENT, font=FONT)

    def calculate_score(self):
        self.score += 1
        self.update()
