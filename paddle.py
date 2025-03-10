from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20
X_POS = -350

class Paddle(Turtle):
    def __init__(self, color, x_pos):
        super().__init__()
        self.paddle_color = color
        self.x_pos = x_pos
        self.create_paddle()
        self.new_y = 0


    def create_paddle(self):
        self.penup()
        self.goto(self.x_pos, 0)
        self.color(self.paddle_color)
        self.shape("square")
        self.shapesize(5,1, None)


    # Movement (can't go off the screen)
    def up(self):
        if self.ycor() < 230:
            self.new_y += MOVE_DISTANCE
            self.goto(self.x_pos, self.new_y)
            return self.ycor()

    def down(self):
        if self.ycor() > -220:
            self.new_y -= MOVE_DISTANCE
            self.goto(self.x_pos, self.new_y)
            return self.ycor()

