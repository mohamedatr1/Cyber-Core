
import random

print("Welcome to the coin guessing game!")
randomchoice = input("""choose a method to toss the coin:
1.using random.random()
2.using random.randint()
Enter your choice (1 or 2): """)

if randomchoice == "1":
    ht = input("Enter your guess (Heads or Tails): \n").lower()
    result = "heads" if random.random() < 0.5 else "tails"
    if ht == result:
        print("Congratulations! You win")
    else:
        print("Sorry! You lost")
    print(f"The computer coin toss result was {result}")

elif randomchoice == "2":
    ht = input("Enter your guess (Heads or Tails): \n").lower()
    result = "heads" if random.randint(1, 2) == 1 else "tails"
    if ht == result:
        print("Congratulations! You win")
    else:
        print("Sorry! You lost")
    print(f"The computer coin toss result was {result}")

else:
    print("Follow the rules")
