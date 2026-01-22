import random 

words = ["mohamed", "khalil", "bachir", "ibrahim"]
random_word = random.choice(words)
display = ["_"] * len(random_word)

attemps = 6
print(" " .join(display)) 
while "_" in display and attemps > 0 :
    guessed = input("Please Enter a letter: ").lower()
    if guessed not in random_word :
        attemps -=1 
    for position in range(len(random_word)) :
        if random_word[position] == guessed :
            display[position] = guessed
    print(display)
    print(f"you have {attemps} attemps left")
if attemps == 0 :
        print("""You lose 
          =========
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
    """)        

    
else :
     print("You win")