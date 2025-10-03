# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

string = input("String : ")

for chr in string :
    if string.count(chr) == 1:
        print(f"First non-repeated character is --> {chr}")
        break
        # After the find chr loop ends