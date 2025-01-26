from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Credit Card Payment of Rs. {amount}")

class PaypalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal Payment of Rs. {amount}")

# Input
payment_type = input("Enter payment type('Credit Card' or 'Pay Pal'): ")     
amount = float(input("Enter amount: "))

if payment_type == "Credit Card":
    payment = CreditCardPayment()
elif payment_type == "PayPal":
    payment = PaypalPayment()

# Output
payment.process_payment(amount)  # Output: Processing Credit Card Payment of Rs. 1000
