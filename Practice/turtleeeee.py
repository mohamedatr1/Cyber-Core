from turtle import Turtle, Screen 


sam = Turtle()
sam.shape("arrow")
sam.color("medium purple")

sam.speed("fast")
window = Screen()
sam.pensize(1)
sam.circle(100)
sam.pendown()


window.exitonclick()