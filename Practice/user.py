class User():
    def __init__(self, first_name, last_name, email, password, status= "inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status 
def create_user():
        first_name = input("Enter Your first name : ")
        last_name = input("Enter your last name : ")
        email = input("Enter your email : ")
        password = input("Enter your password")
        return User(first_name , last_name, email, password)



user1 = create_user()

print(user1.first_name)
print(user1.last_name)
print(user1.email)
print(user1.password)
print(user1.status)