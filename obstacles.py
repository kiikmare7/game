from turtle import Turtle
import random
colour=["blue","green", "blue", "red", "red"]


class Obstacles():
    def __init__(self):
        # super().__init__()
        self.new=[]
        self.create_new()
        self.speed=5

    def create_new(self):
        chance = random.randint(1,6)
        if chance == 1 or chance == 6:
            x = random.randint(-150, 250)
            name = Turtle()
            name.shape("square")
            # name.speed("slowest")
            name.penup()
            name.color(random.choice(colour))
            name.goto(750, x)
            self.new.append(name)

    def move(self):
        for i in self.new:
            i.backward(self.speed)

    def level_up(self):
        self.speed += 5