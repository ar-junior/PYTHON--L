# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = input("Order size -(Small,Medium,Large) : ")

Extra_short = input("Extra short (Yes/No) : ")
short = Extra_short.upper()

if "YES" in short:
    print(f"You ordered a {order_size} coffee. with Espresso")

elif "NO" in short:
    print(f"You ordered a {order_size} coffee.")
else:
    print("Enter Valid Input")