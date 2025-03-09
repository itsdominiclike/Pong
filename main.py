from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
l_paddle = Paddle("turquoise", -350)
r_paddle = Paddle("red", 350)
ball = Ball()



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






p1_score = Scoreboard(-100)
p2_score = Scoreboard(100)

p1_score.halfway_line() #temp, not clean

playing = True

while playing:

    ball.move() # temp - slows down when a key is pressed (not ideal)
    # ball 'goal' detection
    if ball.xcor() >= 380 or ball.xcor() <= -390:
        ball.home()
    #basic ceiling detection
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.home()


screen.exitonclick()