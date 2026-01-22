from turtle import Screen
from snake import Snake
import time
from food import Food 
from score import Score
window = Screen()
window.tracer(0)
window.bgcolor("black")
window.setup(800, 800)
window.title("Snake Game")

sam = Snake()
food = Food()
score = Score()

game_on = True
while game_on:
    sam.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(sam.up, "Up")
    window.onkey(sam.down, "Down")
    window.onkey(sam.right, "Right")
    window.onkey(sam.left , "Left")
    if sam.head.distance(food) < 15 :
        food.appear()
        sam.extend()
        score.increase_score()

    if sam.head.xcor() > 370 or sam.head.xcor() < -370 or sam.head.ycor() > 370 or sam.head.ycor() < -370 :
        game_on = False
        score.game_over()

    for segment in sam.turtles[:-1]:
            if sam.head.distance(segment) < 10 :
                game_on = False
                score.game_over()
       
    











window.exitonclick()