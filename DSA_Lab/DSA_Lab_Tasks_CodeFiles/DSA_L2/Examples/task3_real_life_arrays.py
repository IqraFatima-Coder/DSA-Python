import array 
# Problem: Calculate the average rainfall over a year 
rainfall = array.array('f', [2.3, 1.5, 0.0, 1.2, 3.4, 2.0, 4.5, 3.2, 0.8, 1.9, 2.4, 3.1]) 
total_rainfall = sum(rainfall) 
average_rainfall = total_rainfall / len(rainfall)
print("Total rainfall:", total_rainfall) 
print("Average monthly rainfall:", round(average_rainfall, 2)) 
# Identify months with above-average rainfall 
above_average = [i + 1 for i, value in enumerate(rainfall) if value > average_rainfall] 
print("Months with above-average rainfall:", above_average)