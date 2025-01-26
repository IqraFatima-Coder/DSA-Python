class BankAccount: 
 def __init__(self, account_number, balance): 
  self.__account_number = account_number  # Private attribute 
  self.__balance = balance 
 def deposit(self, amount): 
  self.__balance += amount 
 def withdraw(self, amount):
  if amount <= self.__balance: 
    self.__balance -= amount 
  else:
    print("Insufficient funds")
 def display_balance(self): 
  print(f"Account Number: {self.__account_number}, Balance: {self.__balance}") 
# Create an object of BankAccount 
account = BankAccount("123456789", 1000) 
account.deposit(500) 
account.withdraw(200) 
account.display_balance()