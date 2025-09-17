# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

number = int(input("Enter Number : "))

count = 0

for i in range (1,number+1) :
    if i % 2 == 0 :
        count+=1
print(f"Total Even Number is : {count}")

#               start,  end,   step
# for num in range(2, number+1, 1) :
#     print (f"Even Number is {num}") ---> use for even number print