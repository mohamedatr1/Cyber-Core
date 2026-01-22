from turtle import Turtle , Screen
from paddle import Paddle
from stuff import Stuff
from score import Score
import time
window = Screen()
window.bgcolor("black")
window.setup(800,800)
window.tracer(0)
paddle = Paddle()

all_stuff = []
counter = 0
window.listen()

window.onkey(paddle.go_right,"Right")
window.onkey(paddle.go_right,"d")
window.onkey(paddle.go_left,"Left")
window.onkey(paddle.go_left,"a")
paddle_is_small = False
time_down = 0
score = Score()
game_on = True
while game_on:
    time.sleep(0.05)
    window.update()
    counter += 1
    if paddle_is_small:
        if time.time() - time_down > 5:
            paddle.shapesize(1,6)
            paddle.color("white")
            paddle_is_small = False
    if counter == 30:
        stuff = Stuff()
        all_stuff.append(stuff)
        counter = 0
    for item in all_stuff:
        item.move()

        if item.distance(paddle) < 40 and item.ycor() < -250:
            
            shape = item.shape()
            color = item.pencolor()
            if shape == "turtle":
                if color == "white":
                    score.game_over()
                    game_on = False
                else :
                    score.increase_score(6)
            elif shape == "triangle":
                score.reset_score()

            elif shape == "circle":
                score.increase_score(1)
            elif shape == "square":
                paddle.shapesize(1,2)
                paddle.color("red")
                paddle_is_small = True
                time_down = time.time()

            item.hideturtle()
            all_stuff.remove(item)
        elif item.ycor() < -400:
            item.hideturtle()
            if item in all_stuff: 
                all_stuff.remove(item)





window.exitonclick()