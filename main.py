import time
from turtle import Turtle, Screen
from player import Player
from score import Score
from background import  Background
from obstacles import Obstacles
screen = Screen()
player1 = Player()
score1 = Score()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
# this the back ground in the game x= 800 y = 600
r=Background()
o=Obstacles()
screen.onkey(fun=player1.up,key="Up")
game=True

while game:
    screen.update()
    time.sleep(0.1)
    o.create_new()
    o.move()
    if player1.ycor() > 250:
        player1.goto(0,-250)
        score1.increase_score()
        o.level_up()
    for i in o.new:
        if i.distance(player1)<15:
            score1.gameover()
            game = False
    # player1.distance(o.new)<15:




screen.exitonclick()
