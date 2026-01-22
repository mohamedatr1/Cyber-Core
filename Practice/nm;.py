import turtle
import math
import time

t = turtle.Turtle()
t.speed(0)
t.color("red")
t.width(2)

turtle.bgcolor("black")

def heart(x):
    return 15 * math.sin(x)**3

def heart_y(x):
    return (12 * math.cos(x)
            - 5 * math.cos(2*x)
            - 2 * math.cos(3*x)
            - math.cos(4*x))

t.penup()
t.goto(0, 0)
t.pendown()

for i in range(1000):
    x = heart(i * 0.02)
    y = heart_y(i * 0.02)
    t.goto(x * 10, y * 10)

t.hideturtle()
turtle.done()
