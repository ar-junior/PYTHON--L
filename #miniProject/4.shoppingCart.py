#  mini - project ⭐️

#  shopping cart program -
#  using lists, loops, and conditional statements.

card = [] # to store the items
prices = 0

while True : 
    item = input("Enter the item to purchase ('done' to finish): ")
    if item.lower() == "done": 
        break
    price = float(input(f"Enter the price of {item}: ₹"))
    card.append((item, price))
    prices += price
    print(f"{item} has been added to the cart.\n")

print("Items in your cart:")
for item, price in card:
    print(f"- {item}: ₹{price}")

print(f"Total price: ₹{prices}")
print("Thank you for shopping with us!")
