from turtle import Turtle
import random

BALL_SPEED = 4  # Speed at which the ball moves

class Ball(Turtle):
    """Represents the ball in the Pong game."""

    def __init__(self):
        """Initializes the ball with a circular shape, white color, and no trail."""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()  # Prevents drawing lines
        self.speed(0)  # Fastest animation speed for smooth movement

    def rand_direction(self):
        """Sets a random starting direction for the ball."""
        self.randangle = random.randint(0, 270)  # Random angle from 0 to 270 degrees
        self.setheading(self.randangle)
        return self.randangle  # Returns the chosen angle for reference

    def move(self):
        """Moves the ball forward continuously and handles ceiling/floor bounces."""
        self.forward(BALL_SPEED)

        # Bounce off ceiling and floor
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.randangle = 360 - self.randangle  # Reflects angle vertically
            self.setheading(self.randangle)

    def bounce(self):
        """Handles bounce when the ball hits a paddle."""
        self.randangle = 180 - self.randangle  # Reflects angle horizontally
        self.setheading(self.randangle)