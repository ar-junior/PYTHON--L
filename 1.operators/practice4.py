#  or operator -
#  (only one condition is True then everything is True)
temp = 2
raining = False

if temp > 35 or temp < 0 or raining:
    print("The outdoor event is cancelled")
else:  
    print ("The outdoor event is still scheduled")

#  and operator -
#  (all condition must be true)

temp = 36
sunny = True

if temp > 35 and sunny:
    print("It is HOT outside")

# not operator -
name = "ar"

if not name == "ar" :
    print("hello")
else:
    print("error")