from turtle import Turtle

BALL_SPEED = 2

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        self.forward(BALL_SPEED)


