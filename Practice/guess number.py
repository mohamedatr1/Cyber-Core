import random 
guess = int(input("Welcome to the guess number ! \n enter a number 1 to 10 "))
randomnumber = random.randint(1, 10)
while guess != randomnumber :
    if guess > randomnumber:
        print("Too high!")
        guess = int(input("Try again: "))    
    elif guess < randomnumber :
        print("Too low!")  
        guess = int(input("Try again: "))
    else :
        print("Enter a number")  
        guess = int(input("Try again: ")) 
print("Correct!!!")        
