class Device():
    def __init__(self):
        self.energy = 100

    def electric(self):
        print("The Device was connected with electric!")

    def restart(self):
        print("The device was restart!")

class Laptob(Device):
    def __init__(self):
        super().__init__()

    def electric(self):
        super().electric()

    def restart(self):
        yes = input("Do you want to restart the device ? :")
        if yes == "yes":
            super().restart()
        yn = input("do You want to open the apps after restart? ")
        if yn == "yes":
            print("Done ! the apps will open after the restart")
        else:
            print("Done! the apps will not open after the restart")
        
    def program(self):
        app = input("Do you want to open the app?")
        if app == "yes":
            print("The program was opened")

        else :
            print("The program was closed")

    

lap = Laptob()
lap.__init__()
lap.electric()
lap.restart()
lap.program()
