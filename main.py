from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

screen = Screen()
l_paddle = Paddle("turquoise", -350)
r_paddle = Paddle("red", 350)
ball = Ball()




# Detect input - Currently cannot press both at once
screen.listen()
# move left paddle
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
# move right paddle
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")



screen.setup(800, 800)
screen.bgcolor("black")
screen.title("My Pong Game")


# temp halfway line code
halfway_line = Turtle()
halfway_line.hideturtle()
halfway_line.penup()
halfway_line.goto(0,-390)
halfway_line.left(90)
halfway_line.pencolor("white")
for _ in range(20):
    halfway_line.pendown()
    halfway_line.forward(20)
    halfway_line.penup()
    halfway_line.forward(20)



p1_score = Scoreboard(-100)
p2_score = Scoreboard(100)


# playing = True
#
# # while playing:
# #     pass


screen.exitonclick()