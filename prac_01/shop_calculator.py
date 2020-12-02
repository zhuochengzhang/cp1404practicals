total_price = 0
number_of_items = int(input("Number of items: "))
for i in range(0, number_of_items, 1):
    price = float(input("Price of item: "))
    total_price = total_price + price
if total_price >= 100:
    total_price = total_price * 0.9
print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))
