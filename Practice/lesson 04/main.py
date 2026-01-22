import pandas
file = pandas.read_csv("info.csv")

# popular_method = file.payment_method.mode()
# print(popular_method)
# payment_counts = file.payment_method.value_counts()
# payment_counts.to_csv("reports/payment_counts.csv")


average = file.groupby("location")["sales"].sum()
print(average)
average.to_csv("reports/payment_location.csv")
mean = file.groupby("location")["sales"].mean()
print(mean)
mean.to_csv("reports/mean_location.csv")
median = file.groupby("location")["sales"].median()
print(median)
median.to_csv("reports/median_loction.csv")