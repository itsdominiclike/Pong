import turtle


UP = 90
DOWN = 270
MOVE_DISTANCE = 20
X_POS = -350


class Paddle():
    def __init__(self, color, x_pos):
        self.color = color
        self.x_pos = x_pos
        self.create_paddle()


    def create_paddle(self):
        self.tubby = turtle.Turtle()
        self.tubby.penup()
        self.tubby.goto(self.x_pos, 0)
        self.tubby.color(self.color)
        self.tubby.shape("square")
        self.tubby.shapesize(5,1, None)
        self.new_y = 0


    def up(self):
        self.new_y += MOVE_DISTANCE
        self.tubby.goto(self.x_pos, self.new_y)


    def down(self):
        self.new_y -= MOVE_DISTANCE
        self.tubby.goto(self.x_pos, self.new_y)





