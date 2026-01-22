from turtle import Turtle
import random
stuffs = ("square", "circle", "triangle", "turtle")
colors = ("red", "white", "blue", "green", "yellow", "purple")
sizes = [1,1.2,1.5,1.7]
class Stuff(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(colors))
        self.shape(random.choice(stuffs))
        self.shapesize(random.choice(sizes))
        self.penup()
        self.refresh()

    def refresh(self):
        random_x = random.randint(-380, 380)
        self.goto(random_x, 400)

    def move(self):
        self.sety(self.ycor() -10)



