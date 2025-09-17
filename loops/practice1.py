# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
#          numbers = [11, -2, 3, -4, 5, 6, -7, 8, 9, 10]


numbers = [11, -2, 3, -4, 5, 6, -7, 8, 9, 10]

positive = 0 
for num in numbers :
    if num > 0 :
        positive += 1
        # print(f"Positive number is {num}") --->u se for Positive number print
print(f"Positive Numbers is {positive}")