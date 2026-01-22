print("***** Welcom to iShop calculator *****")
how = int(input("How many items there in your basket today? "))
ite = []
hey = []
print("Let's get to counting them...")
for items in range (1, how + 1):
   
    it = input(f"Please tell me the name of the item number {items} :")
    price = float(input(f"What is the price of {it} \n $"))
    hey.append(price)
yesno = input("Would you like to see your entire basket items ?")
if yesno.lower()== "yes":
    print(ite)
else:
    print("Okay")
sd = input ("Would you like to see how much it'll cost? ")  
if sd.lower() == "yes":
    print(f"{sum(hey)} $")

        