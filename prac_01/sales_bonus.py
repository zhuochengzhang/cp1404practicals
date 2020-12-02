"""
    Program to calculate and display a user's bonus based on sales.
    If sales are under $1,000, the user gets a 10% bonus.
    If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))

while 1:
    if sales < 0:
        break
    elif sales >= 1000:
        print("Discount: " + str(sales * 0.15))
    else:
        print("Discount: " + str(sales * 0.1))
    sales = float(input("Enter sales: $"))
