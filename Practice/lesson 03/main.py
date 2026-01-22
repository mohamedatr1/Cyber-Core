import pandas

data = pandas.read_csv("./lesson 03/workout.csv")

average = data.burned_calaroies.mean()
print(average)
minimum = data.burned_calaroies.min()  
print(minimum)
