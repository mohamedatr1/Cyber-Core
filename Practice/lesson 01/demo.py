with open("data.txt", "w+") as myfile:
    myfile.write("Hi there, how is it going?")
    myfile.seek(0)
    content = myfile.read()
    print(content)