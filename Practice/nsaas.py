fruits = ["Apples", "Bananas"]
mw = ["Milk" , "Water"]
numbers = ["1","2","3"]
listt = [fruits, mw,]
input("Press Enter to change the content...")
new = fruits.insert(0, "Oranges")
fruits.insert(4, "Kiwis")
mw.remove("Water")
mw.append("Tea")
mw.append("Coffee")
listt.insert(3, numbers)
print(f"""Here is the updated basket
      {listt}""")