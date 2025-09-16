# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book,
#          Snowy - Build a snowman).



person = input("weather condition? : ")
weather = person.upper()

if "SUNNY" in weather :
    print("Go for a walk")
elif "RAINY" in weather :
    print("Read a book")
elif "SNOWY" in weather :
    print("Build a snowman")
else:
    print("enter valid weather condition!!")