print("Welcom !")
list = [['☘️', '☘️', '☘️'], ['☘️', '☘️', '☘️'], ['☘️', '☘️', '☘️']]
print (f"{list[0]} \n{list[1]} \n{list[2]}")
print("Wher should the rabbit go? 🐇")
position = input("Please choose a row and a column")
row = int(position[0])
column = int(position[1])
list[row-1][column-1] = "🐇"
print("\n Sucess!!")
print (f"{list[0]} \n{list[1]} \n{list[2]}")