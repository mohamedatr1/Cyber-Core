correct_password = "ab1cd2"
entered_password = input ("Please enter your password: ")
while entered_password != correct_password :
    print("Incorrect password. Please try again.")
    entered_password = input ("Please enter your password: ")
print("Access granted. Welcome!")