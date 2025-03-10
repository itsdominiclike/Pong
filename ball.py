from turtle import Turtle
import random

BALL_SPEED = 4

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)

    # lets make it random for now
    def direction(self):
        self.randangle = random.randint(0, 270)
        self.setheading(self.randangle)
        return self.randangle

    def move(self):
        self.forward(BALL_SPEED) # continuous ball movement
        # bounce logic off ceiling and floor
        if self.ycor() >= 290 or self.ycor() <= -280:
            self.randangle = 360 - self.randangle
            self.setheading(self.randangle)


    def bounce(self):
        # bounce logic off ceiling and floor
        if self.ycor() >= 290 or self.ycor() <= -280:
            self.randangle = 360 - self.randangle
            self.setheading(self.randangle)
        # self.randangle = 360 - self.randangle
        # bounce logic for paddles
        self.randangle = 180 - self.randangle
        self.setheading(self.randangle)






