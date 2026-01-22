total_minutes = input ("Enter the total number of minutes: \n ") 
int_minutes = int(total_minutes)
hours = int_minutes // 60
minutes = int_minutes % 60
second = minutes % 60
print("this cours is : " + str (hours)  + " " + "hours " + " " + str (minutes) + " minutes and " + str(second) + " seconds" ) 