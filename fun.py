item = float
price = item( input("Enter the price of the item"))
rate = 0.06875
def calculate_tax():
    tax =price * rate
    print (f"{item} cost ${price} dollars before tax and ${price + tax} after tax")
calculate_tax()