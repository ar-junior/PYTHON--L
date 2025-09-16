# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age.
#          (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = input("Enter Pet Species : ")
pet = pet.upper()
age = int(input("Enter Your Pet Age : "))

if "DOG" in pet :
    if (age < 2 and age > 0) :
        food = "Puppy Food"
    elif age >= 2 :
        food = "Rotli 😁"

elif "CAT" in pet :
    if (age < 5 and age > 0) :
        food = "Dudh 😁"
    elif age >= 5 :
        food = "Senior cat food"
    
print(f"Recommend food is {food}")