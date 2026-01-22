from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Score
window = Screen()
window.setup(800, 600)
window.bgcolor("black")
window.title("ATR: PingPong")
window.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))

ball = Ball()

window.listen()
window.onkey(r_paddle.go_up,"Up")
window.onkey(r_paddle.go_down, "Down")
window.onkey(l_paddle.go_up,"w")
window.onkey(l_paddle.go_down, "s")

right_score = Score((100, 200))
left_score = Score((-100, 200))
default_speed = 0.1
game_on = True
while True:
    window.update()
    #بدء تحريك الكرة
    time.sleep(default_speed)
    ball.goto(ball.xcor()+ ball.x_move, ball.ycor()+ball.y_move)
    #اكتشاف التصادم مع الحائط العلوي والسفلي
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_move *= -1    
        default_speed *= 0.9
    #اكتشاف التصادم مع المضرب
    if (ball.xcor() >= 330 and ball.distance(r_paddle) <= 50) or (ball.xcor() <=-330 and ball.distance(l_paddle) <= 50):
        ball.bounce_x() 
    #اذا خرجت من جهة اليمين
    if ball.xcor() > 400 :
        ball.goto(0,0)
        ball.x_move *= -1
        default_speed = 0.1
        left_score.increase_score()
        
    #اذا خرجت من جهة اليسارwe
    elif ball.xcor() < -400:
        ball.goto(0,0)
        ball.x_move *= -1
        default_speed = 0.1
        right_score.increase_score()
        


      
     









window.exitonclick()