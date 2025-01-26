#3-	Monthly Budget Planner
#Write a program to help a user plan their monthly budget.
#Input the monthly income and expenses for categories 
# like rent, food, transportation, and savings. Calculate the remaining balance or deficit.
mincome = float(input("Enter your monthly income: "))
rent = float(input("Enter your rent expense: "))
food = float(input("Enter your food expense: "))
transportation = float(input("Enter your transportation expense: "))
savings = float(input("Enter your savings: "))
total_expense = rent + food + transportation + savings
remaining_balance = mincome - total_expense
if remaining_balance > 0:
    print("You have a remaining balance of $", remaining_balance)
else:
    print("You have a deficit of $", -remaining_balance)
    