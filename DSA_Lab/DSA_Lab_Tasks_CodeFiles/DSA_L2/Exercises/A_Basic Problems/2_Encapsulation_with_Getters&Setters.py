#2. Encapsulation with Getters and Setters Create a class BankAccount with private 
#attributes account_number and balance. Use getters and setters to update and retrieve 
#these values. 
# o Input: account_number=12345, balance=10000 
# o Output: Account Number: 12345, Balance: 10000 
class BankAccount:
    def __init__(self, account_number, balance):
        # Private attributes
        self.__account_number = account_number
        self.__balance = balance

    # Getter for account_number
    def get_account_number(self):
        return self.__account_number

    # Setter for account_number
    def set_account_number(self, account_number):
        self.__account_number = account_number

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Setter for balance
    def set_balance(self, balance):
        if balance >= 0:  # Ensure balance is not negative
            self.__balance = balance
        else:
            print("Balance cannot be negative!")

    # Display account details
    def display_details(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")


# Main block for testing
if __name__ == "__main__":
    # Take input from the user
    account_number = int(input("Enter account number: "))
    balance = float(input("Enter initial balance: "))

    # Create BankAccount object
    account = BankAccount(account_number, balance)

    # Display initial details
    print("\nInitial Account Details:")
    account.display_details()

    # Update values using user input
    new_account_number = int(input("\nEnter new account number: "))
    account.set_account_number(new_account_number)

    new_balance = float(input("Enter new balance: "))
    account.set_balance(new_balance)

    # Display updated details
    print("\nUpdated Account Details:")
    account.display_details()
