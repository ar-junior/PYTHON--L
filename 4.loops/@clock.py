#  mini - project ⭐️

#  countdown timer program -
import time

user = int(input("Enter time in seconds : "))

for x in range(user,-1,-1):
    second = x % 60 
    minute = int(x/60) % 60
    hour = int(x/3600)
    time.sleep(1)
    print(f"{hour:02}:{minute:02}:{second:02}")

print("Time's  up!!")