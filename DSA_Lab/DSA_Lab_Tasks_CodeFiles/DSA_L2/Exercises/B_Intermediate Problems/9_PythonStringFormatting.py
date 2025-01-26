def generate_invoice(item, price, quantity):
    total = price * quantity
    invoice = (
        f"Item: {item}\n"
        f"Price: Rs. {price}\n"
        f"Quantity: {quantity}\n"
        f"Total: Rs. {total}"
    )
    return invoice
# Input
item = input("Enter item name: ")
price = float(input("Enter price: "))
quantity = float(input("Enter quantity: "))
# Generate and print invoice
invoice = generate_invoice(item, price, quantity)
print(invoice)

