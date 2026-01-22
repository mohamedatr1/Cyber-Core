total_seconds = int(input("Enter the duration in seconds : \n"))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds =total_seconds % 60 
print("this cours is : " + str (hours)  + " " + "hours " + " " + str (minutes) + " minutes and " + str(seconds) + " seconds" )
