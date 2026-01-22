from turtle import Turtle , Screen
import random
window = Screen()
window.title("Python : Turtles race")
window.setup(width= 600 , height= 400)
colors = ("red", "blue", "green")
y_positions = (-70, 0, 70)
turtles = []
user_input = window.textinput(title="Make your bet", prompt = "Guess the winner \n Type a color : Red , Blue , green:").lower()
for i in range(3):
    new_turtle = Turtle(shape = ("turtle"))
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x = -280, y = y_positions[i])
    turtles.append(new_turtle)
    
def race_turtles():
    game_on =True 
    while game_on:
        for turtle in turtles:
            if turtle.xcor() > 280:
                game_on = False
                wining_color = turtle.pencolor()
                display_result(wining_color == user_input)
            else :
                turtle.forward(random.randint(1,5))



def display_result(is_winner):
    result_turtle = Turtle()
    result_turtle.hideturtle()
    result_turtle.penup()
    result_turtle.goto(0, 0)
    result_turtle.pendown()
    
    
    if is_winner:
        window.bgcolor("dark green")
        result_turtle.color("white")
        result_turtle.write("You win!", font= ("arial", 28, "normal"), align= "center")

    else:
        window.bgcolor("medium violet red")
        result_turtle.color("white")
        result_turtle.write("You lose!", font= ("arial", 28, "normal"), align= "center")
    

race_turtles()








window.exitonclick()