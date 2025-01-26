#Write a program to calculate the EMI (Equated Monthly Installment) for a loan based on the following formula:
# EMI=\frac{P\ \times\ R\ \times\ {(1+R)}^N}{{(1+R)}^{N\ }-1}\ 
#Where:
#P = Principal loan amount
#R = Monthly interest rate (Annual interest rate / 12 / 100)
#N = Number of monthly installments
loan_amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
monthly_interest_rate = annual_interest_rate / 12 / 100
number_of_installments = int(input("Enter the number of monthly installments: "))
emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_installments) / ((1 + monthly_interest_rate) ** number_of_installments - 1)
print("The EMI is: ", emi)
