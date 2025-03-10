from turtle import Turtle

# Constants for text alignment and font styling
ALIGNMENT = 'center'
FONT = ('Courier', 40, 'normal')

class Scoreboard(Turtle):
    """Handles the display and updating of the game scoreboard."""

    def __init__(self):
        """Initializes the scoreboard, setting up the visual properties."""
        super().__init__()
        self.hideturtle()  # Hide the turtle cursor (only text should be visible)
        self.pencolor("white")  # White text for visibility
        self.penup()  # Lift pen to prevent drawing lines
        self.p1_score = 0  # Player 1's score
        self.p2_score = 0  # Player 2's score
        self.goto(0, 250)  # Position the scoreboard at the top of the screen
        self.update_scoreboard()  # Display initial score

    def update_scoreboard(self):
        """Clears and redraws the scoreboard with updated scores."""
        self.clear()
        self.write(f"{self.p1_score}  {self.p2_score}", align=ALIGNMENT, font=FONT)

    def update_p1_score(self):
        """Increases Player 1's score by 1 and updates the display."""
        self.p1_score += 1
        self.update_scoreboard()  # Refresh the scoreboard

    def update_p2_score(self):
        """Increases Player 2's score by 1 and updates the display."""
        self.p2_score += 1
        self.update_scoreboard()  # Refresh the scoreboard