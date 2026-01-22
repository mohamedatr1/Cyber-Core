from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,350)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("arial", 24, "normal"))


    def increase_score(self, points):
        self.score += points
        self.update_score()
    
    def reset_score(self):
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=("arial", 36, "bold"))