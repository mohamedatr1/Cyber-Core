import os 
import time 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class User():
    def __init__(self, first_name, last_name, email, password, status= "inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password 
        self.status = status
    def display_user(self):
        print(f"First Name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"Email : {self.email}")
        print(f"Status : {self.status}")
        print("_" * 20)


def user_info():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password")
    return User(first_name, last_name, email, password)

new_user = []

while True : 
    print("Welcome to user management")
    enter = input("""Choose an Action :
    1 : Added new user.
    2 : Display all users. 
    3 : Exit
       """).lower()
    if enter == "1":
        new_user.append(user_info())
        print("User added succesfully..")
        time.sleep(2)
    elif enter == "2":
        clear_screen()
        if len(new_user) > 0 :
            for i in new_user:
                i.display_user()
            input("\nSTOP! Press Enter to see the names above...")
      
    elif enter == "3":
        break
    else :
        print("Invalid choice .. Try again!")
        