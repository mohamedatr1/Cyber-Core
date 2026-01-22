from turtle import Turtle



class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0,-280)
        self.shapesize(1,6)

    def go_right(self):
        self.goto(self.xcor() +40, self.ycor())
    def go_left(self):
        self.goto(self.xcor() -40, self.ycor())