class Light():
    def __init__(self):
        self.energy = 100

    def turn_on(self):
        print("The light is on!")

    def turn_off(self):
        print("The light is off!")

    
class Intelegent(Light):
    def __init__(self):
        super().__init__()

    def turn_on(self):
        super().turn_on()

    def turn_off(self):
        print("""
1
2
3
4
5
              """)
        super().turn_off()

    def wifi(self):
        print("The light is connected with wifi")


light = Intelegent()

light.turn_on()
light.turn_off()
light.wifi()