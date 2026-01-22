import random
print("Welcome to the Rock, Paper, Scissors game!")
helpp = input("Press Enter to continue or type (Help) for the rules: ").capitalize()
game = ("Rock", "Paper", "Scissors")
comp = random.choice(game)
if helpp == "Help" :
    print (""" ****The Rules***
           1) You choose and the computer chooses.
           2) Rock smashes scissors = Rock wins!
           3) Scissors cut paper = Scissors wins!
           4) Paper cover rock = paper wins! """)
else :
    ent = input ("Enter your choice (Rock, Paper, Scissors): ").capitalize()
    if  ent not in game :
        print("Invalid choice!!!")
    else :
     if ent == "Paper":
        print (f"""Your chose : {ent}
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

""")
     elif ent == "Rock":
      print (f""" Your chose : {ent}
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

""")
     elif ent == "Scissors":
        print(f"""Your chose :{ent}
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
              
""")
        
     else :
        print("Invalid choice")
    if comp not in game :
     print ("Invalid choice")
    else :
      if comp == "Paper":
        print (f"""The computer chose : {comp}
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

""")
      elif comp == "Rock":
       print (f""" The computer chose : {comp}
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

""")
      elif comp == "Scissors":
        print(f"""The computer chose :{comp}
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
              
""")
        
      else :
        print("Invalid choice")
      if ent == comp:
          print("It's a tie!")
      elif (ent == "Rock" and comp == "Scissors") or \
           (ent == "Scissors" and comp == "Paper") or \
           (ent == "Paper" and comp == "Rock"):
          print("🎉 You win!")
      else:
          print("💻 Computer wins!")    
     






     