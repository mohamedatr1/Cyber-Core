from turtle import Turtle , Screen

sam = Turtle()
window = Screen()

window.bgcolor("black")
window.setup(width = 800, height= 800)
sam.shape("turtle")
sam.color("white")
sam.speed("fastest")
sam.pensize(3)
#بداية الدوائر
def draw_circles():
    sam.penup()
    sam.goto(x = -300, y = -300)
    sam.pendown()
    for _ in range(10):
        sam.circle(25)
        sam.left(360 / 10)


user_name = window.textinput(title = "لحطة من قضلك", prompt="اكتب اسمك:")






#نهاية تاع الدوائر


#بداية المربعات
def draw_squares():
    sam.penup()
    sam.goto(x = 0, y = 0)
    sam.pendown()
    for _ in range(10):
        sam.left(360 / 10)
        for _ in range(4):
            sam.forward(50)
            sam.left(90)

#نهاية المربعات

#بداية المثلثات
def draw_triangles():
    sam.penup()
    sam.goto(x= 300, y = 300)
    sam.pendown()
    for _ in range(10):
        sam.left(360 / 10)
        for _ in range (3):
            sam.forward(50)
            sam.left(360/3)



#نهاية المثلثات
draw_circles()  
draw_squares()
draw_triangles()



window.exitonclick()