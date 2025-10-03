# while loop = execute some code WHILE some condition remains true

name = input("enter your name: ") # starting 

while name == "" : # if the condition is True,the code is executed
    print("enter your *name!!")
    name = input("enter your name: ")
# they exit whenever the condition is False

print(f"your name is {name}")