from turtle import  Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.highscore = self.get_highscore()
        self.color("White")
        self.penup()
        self.goto(0, 350)
        self.hideturtle()
        self.update_score()

    def get_highscore(self):
        with open("highscore.txt","r") as file:
            return int(file.read())
        
    def save_highscore(self):
        with open("highscore.txt","w") as file:
            file.write(str(self.highscore))


    def update_score(self):
        self.write(f"Score: {self.score}   High Score: {self.highscore}", align = "center", font =("arial", 22 , "normal"))
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.screen.bgcolor("darkred")
        self.goto(0,0)
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.write(f"---------------Game Over!---------------\n\nFinal Score: {self.score} \n\nHigh Score: {self.highscore}", align = "center", font = ("arial", 24 , "normal"))
        




