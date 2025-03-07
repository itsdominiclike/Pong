from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard

l_paddle = Paddle("turquoise", -350)
r_paddle = Paddle("red", 350)
screen = Screen()


# Detect input
screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


screen.setup(800, 800)
screen.bgcolor("black")
screen.title("My Pong Game")

# playing = True
#
# # while playing:
# #     pass


screen.exitonclick()