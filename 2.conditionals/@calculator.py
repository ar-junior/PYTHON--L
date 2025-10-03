#  mini - project ⭐️
#  calculator

operator = (input("enter an operator (+ - * /) : "))
num1 = float(input("enter the 1st number = "))
num2 = float(input("enter the 2nd number = "))

if operator == "+" :
    result = num1 + num2

elif operator == "-" :
    result = num1 - num2

elif operator == "*" :
    result = num1 * num2
    
elif operator == "/" :
    result = num1 / num2

else:
    result = (f"--> '{operator}' is not a valid operator")
    

print(result)