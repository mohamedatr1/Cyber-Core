from turtle import Turtle , Screen
sam = Turtle()
window = Screen()
sam.speed("fast")
window.bgcolor("white")
window.setup(width = 800, height= 800)

list = ["مربع", "مثلث", "دائرة", "square", "triangle", "circle"]
game_on = True

def draw_square():
    for _ in range(4):
        sam.shape("turtle")
        sam.color("red")
        sam.pensize(4)
        sam.forward(100)
        sam.left(90)
def draw_circle():
     for _ in range(1):
                sam.shape("square")
                sam.color("black")
                sam.circle(100)
                sam.pensize(2)

def draw_triangle():
       for _ in range(3):
              sam.shape("square")
              sam.color("purple")
              sam.pensize(3)
              sam.forward(100)
              sam.left(360 / 3)
        

while game_on:


    user_input = window.textinput(title="لحظة من فضلك", prompt="ما الذي تريد رسمه؟ (دائرة, مثلث, مربع) أو اكتب 'خروج':")

    if user_input in list:
        if user_input == "دائرة" or user_input == "circle":
            draw_circle()

        elif user_input == "مربع" or user_input == "square":
            draw_square()

        elif user_input == "مثلث" or user_input =="triangle":
            draw_triangle()

    elif user_input == "خروج" or user_input == "exit":   
        game_on = False
        window.clear()
        sam.color("black")
        window.bgcolor("LightCyan1")
        sam.write("Press any Key to exit" , font = ("arial", 35, "bold"), align= "center" )
        sam.color("darkgray")
        sam.penup()
        sam.goto(x = 0 , y = -50)
        sam.pendown()
        sam.write("اضغط في اي مكان للخروج", font = ("arial", 25, "normal"), align= "center" )        
            

window.exitonclick()