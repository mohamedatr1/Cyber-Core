color1 = input("Add the first color you like : \n")
colors = []
colors.append(color1)
color2 = input("Do you want to add more colors? (Yes) or (No)?")
if color2.lower() == "yes":
    color2 = input("Add the second color you like : \n")
    colors.append(color2)
    print(f"The colors you like are : \n {colors}")
else :
    print(f"the color you like is : \n {color1}")    




class1 = ["mohamed", "yassine", "ahmed"]
class2 = ["sara", "amina", "yasmine"]
class1.remove("yassine")
class2.append("yassine")
print(f"the new class1 is : {class1}")