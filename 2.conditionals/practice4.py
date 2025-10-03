# 4. Fruit Ripeness Checker(banana,apple)
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe,
#          Yellow - Ripe, Brown - Overripe)

fruit = input("Fruit Name : ")
fruit_color = input("Fruit Color : ")
color = fruit_color.upper()

# if "banana" in fruit :
#     if "GREEN" in color :
#         print("Banana is Unripe")
if fruit.upper() == "BANANA"  :
    if color == "GREEN" :
        print(f"{fruit} is Unripe")
    elif color == "YELLOW" :
        print(f"{fruit} is Ripe")
    elif color == "BROWN" :
        print(f"{fruit} is Overripe")
    else:
        print("The color does not match!!")

if fruit.upper() == "APPLE"  :
    if color == "GREEN" :
        print(f"{fruit} is Unripe")
    elif color == "RED" :
        print(f"{fruit} is Ripe")
    elif color == "BROWN" :
        print(f"{fruit} is Overripe")
    else:
        print("The color does not match!!")


else:
    print("sorry... only two fruits available-(banana,apple)")