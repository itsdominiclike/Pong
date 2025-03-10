import turtle
from turtle import Screen
from event_handlers import KeyPresses
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

# Flag to control game loop
playing = True

def halfway_line():
    """Draws a dashed halfway line in the middle of the screen."""
    line = turtle.Turtle()
    line.hideturtle()
    line.pensize(5)
    line.penup()
    line.goto(0, -290)
    line.left(90)
    line.pencolor("white")
    for _ in range(15):
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(20)

# Initialize screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong Game")

# Create game objects
l_paddle = Paddle("turquoise", -350)  # Left paddle
r_paddle = Paddle("red", 350)  # Right paddle
ball = Ball()                          # Ball instance
scoreboard = Scoreboard()              # Scoreboard instance
p1_keys = KeyPresses()                 # Player 1 key event handler
p2_keys = KeyPresses()                 # Player 2 key event handler

# Draw the halfway line and set initial ball direction
halfway_line()
ball.rand_direction()

# Set up screen event listeners for player controls
screen.tracer(0)  # Disable automatic screen updates (manual refresh)
screen.listen()

# Left paddle controls
screen.onkeypress(p1_keys.up_press, "w")      # Move paddle up
screen.onkeyrelease(p1_keys.up_release, "w")  # Stop moving paddle
screen.onkeypress(p1_keys.down_press, "s")    # Move paddle down
screen.onkeyrelease(p1_keys.down_release, "s")# Stop moving paddle

# Right paddle controls
screen.onkeypress(p2_keys.up_press, "Up")      # Move paddle up
screen.onkeyrelease(p2_keys.up_release, "Up")  # Stop moving paddle
screen.onkeypress(p2_keys.down_press, "Down")  # Move paddle down
screen.onkeyrelease(p2_keys.down_release, "Down")# Stop moving paddle

# Main game loop
while playing:
    screen.update()  # Manually update screen for smooth animation
    ball.move()      # Move the ball

    # Handle player movements
    if p1_keys.up_pressed:
        l_paddle.up()
    if p1_keys.down_pressed:
        l_paddle.down()

    if p2_keys.up_pressed:
        r_paddle.up()
    if p2_keys.down_pressed:
        r_paddle.down()

    # Goal detection: If the ball crosses the left or right edge, update the score and reset
    if ball.xcor() >= 380:
        scoreboard.update_p1_score()
        ball.home()  # Reset ball position to center
        ball.rand_direction()  # Randomize new direction

    if ball.xcor() <= -380:
        scoreboard.update_p2_score()
        ball.home()
        ball.rand_direction()

    # Paddle bounce logic: Detect if the ball is close to the paddle and within paddle range
    if abs(ball.xcor() - 340) < 5:  # Right paddle collision
        if r_paddle.ycor() - 50 <= ball.ycor() <= r_paddle.ycor() + 50:
            ball.bounce()

    if abs(ball.xcor() - (-340)) < 5:  # Left paddle collision
        if l_paddle.ycor() - 50 <= ball.ycor() <= l_paddle.ycor() + 50:
            ball.bounce()

# Close the game window when clicked
screen.exitonclick()