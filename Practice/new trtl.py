import random
from turtle import Turtle , Screen
window = Screen()
window.setup(width=1000 , height=1000)
window.bgcolor("black")
rangee = (10, 15, 20, 25, 30, 35)
sam = Turtle()
sam.shape("turtle")
sam.color("white")
sam.speed("fastest")
sam.pensize(5)

rey = Turtle()

rey.shape("square")
rey.color("orange")
rey.speed("fast")
rey.pensize(5)

my_angles = (0, 90, 180, 270)
my_distance = (20, 30, 40, 50, 60, 70, 80, 90, 100) #Tuple

def draw_random(turtle_name):
    for _ in range(random.choice(rangee)):
        turtle_name.forward(random.choice(my_distance))
        turtle_name.left(random.choice(my_angles))

for _ in range(20):
    sam.circle(100)
    sam.left(360 / 20)
window.exitonclick()
