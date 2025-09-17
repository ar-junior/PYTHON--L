# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input("Enter No : "))

for i in range(1,11) :
    if i == 5:
        continue
        # iteration skip 
    print (f"{i} X {number} = {i*number}")
