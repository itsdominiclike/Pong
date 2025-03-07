from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 40, 'normal')

class Scoreboard(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.hideturtle()  # Hide the turtle cursor (only text should be visible)
        self.pencolor("white")
        self.penup()
        self.p1_score = 0 #temp
        self.p2_score = 0 #temp
        self.score = 0 #temp
        self.goto(x_pos, 350)
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT) #temporary

    # could maybe put halfway line code here, unsure if it should be in scoreboard however
    def halfway_line(self):
        self.hideturtle()
        self.penup()
        self.goto(0, -390)
        self.left(90)
        self.pencolor("white")
        for _ in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
