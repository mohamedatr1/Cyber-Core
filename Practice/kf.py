tasks = input("Enter your tasks for today separated by a comma: ").split(", ")
donetasks = []
ongoingtasks = []
for task in tasks :
    print ("\n" + task + "\n")
    yesno = input(f"Did you finish {task} already ? ")
    if yesno.lower() == "yes":
        print("Nice job!!")
        donetasks.append(task)
    elif yesno.lower() == "no":
        print("Try not to put if off !")
    print("-----")     
    ongoingtasks.append(task)
ha = input("Do u wanna see ur today's progress (yes or no)? ")
if ha.lower() == "yes":
    print("""
    ******Done tasks******
""")
    print(donetasks)
    print("""
******Ingoing tasks******
""")
    print(ongoingtasks)
else :
    print("Okay as u like!")    
     