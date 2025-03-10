from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 40, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()  # Hide the turtle cursor (only text should be visible)
        self.pencolor("white")
        self.penup()
        self.p1_score = 0 #temp
        self.p2_score = 0 #temp
        self.score = 0 #temp
        self.goto(0, 250)
        self.write(f"{self.p1_score} {self.p2_score}", align=ALIGNMENT, font=FONT) #temporary

    def update_p1_score(self):
        self.clear()
        self.p1_score +=1
        self.write(f"{self.p1_score} {self.p2_score}", align=ALIGNMENT, font=FONT)

    def update_p2_score(self):
        self.clear()
        self.p2_score +=1
        self.write(f"{self.p1_score} {self.p2_score}", align=ALIGNMENT, font=FONT)

