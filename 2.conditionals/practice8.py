# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". 
#          Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter Your Password : ")

pas = (len(password))

if pas < 6 and pas > 0:
    strength = "Password is Weak"
elif pas <= 10 :
    strength = "Password is Medium"
elif pas < 21 :
    strength = "Password is Strong"
else :
    strength = "to long password"

print(strength)