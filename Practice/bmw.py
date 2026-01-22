import random
print("Welcome to 'Who is wallet?")
names = input(""" You will give me a list of names , and i will pick a person to pay if you are ready 
Enter names separeted by a comma:       
""")
name_string = names.split(", ")
length = len(name_string) - 1
randomnumber = random.randint(0, length)
randomperson = name_string[randomnumber]
print(f"{randomperson} is going to pay today!")