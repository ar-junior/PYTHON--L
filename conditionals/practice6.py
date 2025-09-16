# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance 
#          (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

km = int(input("Enter Your distance (km) : "))

if km < 3 and km > 0 :
    transp = "Walk"
elif km < 16 :
    transp = "Bike"
elif km < 101:
    transp = "Car"
elif km > 100:
    transp = "public transfer"
else:
    transp = "enter valid distance"

print(f"recommends you the transport of:{transp}")