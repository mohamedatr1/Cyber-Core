import random 
words = ["mohamed", "khalil", "bachir", "djamel"]
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
random_word = random.choice(words)
display = ["_"] * len(random_word)
print(hangmanpic[0])
attemps = 6 
guessed_letters = []
print(" ".join(display))
while "_" in display and attemps > 0 :
    guessed = input("Please Enter a letter: ").lower()
    if guessed in guessed_letters :
        print("You already guessed that. Try again!")
        print(f"You have {attemps} attemps left.")
        continue
    guessed_letters.append(guessed)
    if guessed not in random_word :
        attemps -= 1
        print(hangmanpic[6-attemps])
    for position in range(len(random_word))  :
        if random_word[position] == guessed :
            display[position] = guessed
    print(display)        
    print(f"You have {attemps} attemps left.")
if attemps == 0:
    print("""
   **** You Lose ! ****
""")
    print(hangmanpic[-1])
else :
    print("""
   **** You Win ! ****
""") 


