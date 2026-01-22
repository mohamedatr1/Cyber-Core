number = int(input("Enter the PIN Number: \n"))
number = str(number)
if len(str(number)) == 4 :
    import random
    my_random = random.randint(1000,9999) 
    if number == my_random:
        print("Congraluation! you are win")
    else:
        print("failure! PIN Code did not much")    
        print(f"The Computer generated this PIN : {my_random}")
else :
    print("PIN must be 4 digits")