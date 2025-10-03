name = input("Enter your full name: ")
number = input("Enter your phone number: ")


result = len(name)
find = name.find(" ") # return- int, first "space" index
rfind = name.rfind("a") # return- Int, last "a" index
            # r = reverse
cap = name.capitalize() # return- new str, first latter capital
upper = name.upper() 
lower = name.lower()
digit = name.isdigit() # return- bool(True,False), only digit string-True
alpha = name.isalpha() # return- bool(True,False), only alphabets string-True
count = number.count("-") # return- Int, count "-" in a number variable
replace = number.replace("-", "_") # return- new str, replace = 12-21 to 12_21


print(replace)