#password :abc
password = input("Enter the password: \n")
if password == "abc":
    print("the password is correct")
else :
    print("the password is incorect")   
#yes no maybe:      
enter = input("Enter :Yes ، No ، Maybe:")
if enter == "Yes":
    print("You wrote : Yes")
elif enter == "No":
    print("You wrote : No")
elif enter == "Maybe":
    print ("You wrote :Maybe")
else :
    print("Follow the instructions")        


number = int(input ("guess the number :"))
if number == 7 :
    print("you are correct")   
else :
    print("you are incorrect")   



area = input("Chose an area : (Medea) ، (Berrouaghia) ،(Alger):")   
if area.lower() == "medea" or area.lower ()== "berrouaghia" or area.lower ()== "alger":
    print(f"{area} is in our list")
else:
    print(f"{area} is not in our list")



name = input("Enter your Name : \n")
password = input("Please enter your password : \n")
if name.lower () == "mohamed" and password == "bachirMohamed" :
    print(f"Welcome back {name}!!")
else :
    print ("Sorry،Wrong name or password !")   

age = int(input("Enter your age : \n"))
license = input("Do you have a License? \n")
if age > 18 and license.lower () == "yes" :
    print("You can drive the car!")
else :
    print("Sorry ،You cant drive the car!") 



nationality = input("Are you Algerian? \n") 
if nationality.lower () == "yes" :   
   age = int(input ("How old r u ? \n"))
else :
    print("Sorry u r not algerian .")
if age >= 18 :
    print ("you are accepted")
else :
    print("Sorry, You cant do that")    
