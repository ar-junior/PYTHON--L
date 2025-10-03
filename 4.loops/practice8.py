# while loop

num = int(input("Enter number between 1 to 10 : "))

while num > 10 or num < 0 :
    print(f"{num} is not valid")
    num = int(input("Enter number between 1 to 10 : "))


print(f"you number is {num}")