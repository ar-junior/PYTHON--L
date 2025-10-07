#  mini - project ⭐️

#  Python compound interest calculator -
#  A = p(1+r/n)**t
#  using while loop 

principle = 0
rate = 0
time = 0

while True : # principle <=0 :
    principle = float(input("Enter the principal amount : "))
    if principle <0 :
        print("Principle can't be less than or equal to zero\n")
    else:
        break

while True : # rate <=0 :
    rate = float(input("Enter the interest rate: "))
    if rate <0 :
        print("Rate can't be less than or equal to zero\n")
    else:
        break

while True : # time <=0 :
    time = int(input("Enter the time in years: "))
    if time <0 :
        print("Time can't be less than or equal to zero\n")
    else: 
        break


total = principle* pow((1+rate/100),time)

print(f"Balance after {time} year/s: ₹{total:.2f}")
