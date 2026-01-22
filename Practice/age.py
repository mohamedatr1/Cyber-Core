old = int(input("How Old are You? \n"))
print(f"You were born in : {2025 - old}")

nationality = input("Are you Algerian? \n")
if nationality.lower() == "yes":
       age = int(input("How old r u ? \n"))
       if age >= 18:
              print("you are accepted")
       else:
              print("Sorry, You cant do that . wait to be 18 yo to do that")
else:
       print("Sorry u r not algerian .")
 