from turtle import Turtle


class Background(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(750, 250)
        self.pendown()
        self.goto(-750, 250)
        self.penup()
        self.goto(750, 150)
        self.pendown()
        self.goto(-750, 150)
        self.penup()
        self.goto(750, 50)
        self.pendown()
        self.goto(-750, 50)
        self.penup()
        self.goto(750, -50)
        self.pendown()
        self.goto(-750, -50)
        self.penup()
        self.goto(750, -150)
        self.pendown()
        self.goto(-750, -150)
        self.penup()
