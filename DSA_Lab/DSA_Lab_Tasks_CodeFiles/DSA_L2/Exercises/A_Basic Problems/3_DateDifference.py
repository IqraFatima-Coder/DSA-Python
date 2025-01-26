#3. Date Difference Write a program to calculate the number of days between two given 
#dates. 
##o Output: Difference: 14 days
from datetime import datetime

def date_difference(date1_str, date2_str):
    # Convert the string dates to datetime objects
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    
    # Calculate the difference in days
    difference = (date2 - date1).days
    
    return difference

# Input dates
date1 = "2025-01-01"
date2 = "2025-01-15"

# Calculate and print the difference
days_difference = date_difference(date1, date2)
print("Difference:", days_difference, "days")
