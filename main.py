import turtle
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

playing = True

# halfway line will be here for now
def halfway_line():
    line = turtle.Turtle()
    line.hideturtle()
    line.penup()
    line.goto(0, -290)
    line.left(90)
    line.pencolor("white")
    for _ in range(15):
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(20)

# turtles/objects
screen = Screen()
l_paddle = Paddle("turquoise", -350)
r_paddle = Paddle("red", 350)
ball = Ball()
scoreboard = Scoreboard()
halfway_line()
ball.rand_direction()


# Detect input - Currently cannot press both at once
screen.listen()
# move left paddle
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
# move right paddle
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")


screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong Game")




while playing:

    ball.move() # temp - slows down when a key is pressed (not ideal)
    # ball 'goal' detection
    if ball.xcor() >= 380:
        scoreboard.update_p1_score()
        ball.home()
        ball.rand_direction()
    if ball.xcor() <= -390:
        scoreboard.update_p2_score()
        ball.home()
        ball.rand_direction()

    # paddle bounce logic
    if abs(ball.xcor() - 350) < 4:
        if r_paddle.ycor() - 50 <= ball.ycor() <= r_paddle.ycor() + 50:
            ball.bounce()
            print("Contact")
    if abs(ball.xcor() - (-350)) < 4:
        if l_paddle.ycor() - 50 <= ball.ycor() <= l_paddle.ycor() + 50:
            ball.bounce()
            print("Contact")


screen.exitonclick()