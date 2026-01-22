import random
import string 
password = ""
print("Welcome to the password generator!")
total = input("enter the total number of characters in the password : ")
letters_count = int(input("enter the number of letters in the password: "))
digits_count = int(input("enter the number of digits in the password: "))
symbols_count = int(input("Enter the number of symbols in the password: "))
letters = random.choices(string.ascii_letters, k=letters_count)
digits= random.choices(string.digits, k=digits_count)
symbols = random.choices(string.punctuation, k=symbols_count)
password_list = letters + digits + symbols
random.shuffle(password_list)
for x in password_list :
    password += x
if len(password) == int(total):
        print("Your generated password is : " , password)
else:
        print("the total number of characters does not match the sum of letters, digits, and symbols.")    


