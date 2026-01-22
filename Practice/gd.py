print("*****WELCOME TO THE MULTIPLICATION TABLE*****")
number = int(input("Enter the number: "))
for i in range(1, 11):
 result = number * i
 print(f"{number} * {i} ={result}")