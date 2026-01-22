import random 
words = ["bachir", "abdou", "khalil", "ibrahim", "mohamed", "anes"]
random_choice = random.choice(words)
hangmanpic = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
attemps = 6 
display = ["_"] * len(random_choice)
print(hangmanpic[0])
guessed_letter = []
print(" ".join(display))
while "_" in display and attemps > 0 :
    guessed = input("Please Enter a letter: ").lower()
    if guessed in guessed_letter :
        print("You already guessed that. Try again!")
        print(f"You have {attemps} attemps left")
        continue
    guessed_letter.append(guessed)
    if guessed not in random_choice:
        attemps -= 1 
        print(hangmanpic[6 - attemps])
    for position in range(len(random_choice)):
        if random_choice[position] == guessed :
            display[position] = guessed
    print(display)
    print(f"you have {attemps} attemps left!")
if attemps == 0:
    print("""
******* You Lose! *******
""")        
    print(hangmanpic[-1])
else :
    print("""
******* You win *******
""")    
