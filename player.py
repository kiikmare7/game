from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(0,-250)

    def up(self):
        self.setheading(90)
        self.forward(20)
