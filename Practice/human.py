class Human():
    def __init__ (self):
        self.energy = 100
    
    def walk(self):
        print("I am now walking!")

class Athlete(Human):
    def __init__(self):
        super().__init__()
    def run(self):
        print("I am now running fast!")

    def walk(self):
        super().walk()
        print("I walk very fast. I am faster than a bullet!")

runner = Athlete()
runner.walk()
