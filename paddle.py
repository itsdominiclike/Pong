import turtle
from turtle import Turtle
class Paddle():
    def __init__(self):
        self.create_paddle()

    def create_paddle(self):
        tubby = turtle.Turtle()
        tubby.penup()
        tubby.goto(-350, 0)
        tubby.color("turquoise")
        tubby.shape("square")
        tubby.shapesize(5,1, None)



