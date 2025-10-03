#  conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                           "Print or assign one of two values based on a condition"
#                           --> X if condition else Y

# variables
num = 5
a = 6
b = 7
age = 13
temperature = 20
user_role = "admin"

# one-line if-else statement
print("Positive" if num > 0 else "Negative")  # num = 5
result = "EVEN" if num % 2 == 0 else "ODD"  # num = 4
max_num = a if a > b else b  # a = 6, b = 7
min_num = a if a < b else b  # a = 6, b = 7 
status = "Adult" if age >= 18 else "Child"  # age = 13
weather = "HOT" if temperature > 20 else "COLD"  # temperature = 20
access_level = "Full Access" if user_role == "admin" else "Limited Access"  # user role = "admin"

print(access_level)