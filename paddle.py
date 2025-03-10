from turtle import Turtle

# Constants for movement and positioning
UP = 90
DOWN = 270
MOVE_DISTANCE = 5  # Distance the paddle moves per key press
X_POS = -350  # Default X position for left paddle

class Paddle(Turtle):
    """Represents a paddle in the Pong game, inherited from Turtle."""

    def __init__(self, color, x_pos):
        """
        Initializes a paddle with a specific color and position.

        :param color: String representing the paddle's color.
        :param x_pos: Integer representing the paddle's starting X coordinate.
        """
        super().__init__()  # Call the parent Turtle class constructor
        self.paddle_color = color
        self.x_pos = x_pos
        self.create_paddle()
        self.new_y = 0  # Tracks the new Y position after movement

    def create_paddle(self):
        """Creates and positions the paddle at its initial location."""
        self.penup()  # Prevent drawing when moving
        self.goto(self.x_pos, 0)  # Start at given X position, center Y
        self.color(self.paddle_color)  # Set paddle color
        self.shape("square")  # Use a square shape
        self.shapesize(stretch_wid=5, stretch_len=1)  # Make it a vertical rectangle

    def up(self):
        """Moves the paddle up if it's not at the top boundary."""
        if self.ycor() < 230:  # Upper limit to prevent moving off-screen
            self.new_y += MOVE_DISTANCE
            self.goto(self.x_pos, self.new_y)
            return self.ycor()  # Return new Y position for reference

    def down(self):
        """Moves the paddle down if it's not at the bottom boundary."""
        if self.ycor() > -220:  # Lower limit to prevent moving off-screen
            self.new_y -= MOVE_DISTANCE
            self.goto(self.x_pos, self.new_y)
            return self.ycor()  # Return new Y position for reference