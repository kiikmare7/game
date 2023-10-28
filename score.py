from turtle import  Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.write(f"level {self.score}",align="center",font=("Align",25,"normal"))
        self.goto(290,260)
        self.hideturtle()
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"level {self.score}",align="center",font=("Align",25,"normal"))

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER!",align="center",font=("Align",20,"normal"))