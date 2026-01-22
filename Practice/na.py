import random
names = input("""Welcome to who is wallet?
      you will give me a list of names , and i will pick a person to pay if you are ready 
      Enter names separeted by a comma,
      if you are ready enter the list name:
""").split(", ")
print(f"please ask {random.choice(names)} to take his wallet out to pay")
