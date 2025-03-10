import turtle
from turtle import Screen

from event_handlers import KeyPresses
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import event_handlers


p1_keys = KeyPresses()
p2_keys = KeyPresses()

screen = Screen()
screen.listen()
screen.onkeypress(p1_keys.up_press, "w")
screen.onkeyrelease(p1_keys.up_release, "w")
screen.onkeypress(p1_keys.down_press, "s")
screen.onkeyrelease(p1_keys.down_release, "s")

screen.onkeypress(p2_keys.up_press, "Up")
screen.onkeyrelease(p2_keys.up_release, "Up")
screen.onkeypress(p2_keys.down_press, "Down")
screen.onkeyrelease(p2_keys.down_release, "Down")



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
# screen.listen()
# move left paddle
# screen.onkeypress(l_paddle.up, "w")
# screen.onkeypress(l_paddle.down, "s")
# # move right paddle
# screen.onkeypress(r_paddle.up, "Up")
# screen.onkeypress(r_paddle.down, "Down")


screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong Game")

def update_ball():
    ball.move()
    screen.update()
    screen.ontimer(update_ball, 20)  # Call again in 20ms

update_ball()  # start the timer

while playing:

    ball.move()  # temp - slows down when a key is pressed (not ideal)

    if p1_keys.up_pressed:
        l_paddle.up()
    if p1_keys.down_pressed:
        l_paddle.down()

    if p2_keys.up_pressed:
        r_paddle.up()
    if p2_keys.down_pressed:
        r_paddle.down()


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
    if abs(ball.xcor() - 350) < 6:
        if r_paddle.ycor() - 50 <= ball.ycor() <= r_paddle.ycor() + 50:
            ball.bounce()
    if abs(ball.xcor() - (-350)) < 6:
        if l_paddle.ycor() - 50 <= ball.ycor() <= l_paddle.ycor() + 50:
            ball.bounce()

screen.exitonclick()