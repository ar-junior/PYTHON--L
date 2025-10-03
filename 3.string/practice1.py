# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

name = input("Enter your name : ")

if len(name) > 12 :
    error = "Your username can't be more than 12 characters"
elif name.find(" ") != -1: # elif not name.find(" ") == -1
    error = "no space allowed"
elif name.isalpha() == False: # elif not name.isalpha():
    error = "no digits allowed"
else :
    error = (f"Welcome {name}")

print(error)
