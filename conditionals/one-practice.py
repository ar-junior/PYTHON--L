# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

person = int(input("Enter Your Age:"))

if person >0 and person < 110:
    if person < 13 :
        print("You are a Child.")
    elif person <=19 :
        print("You are a Teenager.")
    elif person <= 59 :
        print("You are an Adult.")
    else:
        print("You are a senior.")
else:
    print("wrong age")