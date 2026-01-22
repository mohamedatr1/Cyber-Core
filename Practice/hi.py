import random
randomchoice = int(input("""Welcome to the coin guessing game
choose a method to toss the coin:
1.Using random.random ()
2.Using random.randint ()      
Enter your choice ( 1 or 2 )  """))
if randomchoice == "1" :
   ht = input("enter your guess (Heads or Tails) \n").lower()   
   result = "heads" if  random.random() < 0.5 else "tails"
   if ht == result :
      print ("Congraluation you win!!") 
   else : 
      print("Sorry! you are not win ")
      print(f"the computer guess was {result} ")
elif randomchoice == "2" :
    ht = input("enter your guess (Heads or Tails) \n").lower()
    if random.randint (1,2) == 1 :
         result = "heads"
    else :"tails"
    if ht == result :
       print("Congraluation! you win!!")
    else :
       print("Sorry you lose !")  
       print(f"The computer guess was {result}") 
else :
   print("follow the rules")       
