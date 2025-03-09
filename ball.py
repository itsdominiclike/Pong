from turtle import Turtle
import random

BALL_SPEED = 2

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    # lets make it random for now
    def direction(self):
        self.randangle = random.randint(0, 270)
        self.setheading(self.randangle)

    def move(self):
        self.forward(BALL_SPEED)



