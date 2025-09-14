# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over),
#.         $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter Your Age : "))
day = input("is today the day? : ")

today = day.upper()
price = 12 if age >= 18 else 8  

if today == "WEDNESDAY" :
    # price = price-2
    price -= 2
    print(f"Special discount for today!!\nticket price is {price}")
else:
    print(f"ticket price is {price}")