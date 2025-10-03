# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).


student = int(input("Enter your score : "))

if student <=100 and student >=0 :
    if student >= 90 :
        print ("A -grade")
    elif student >= 80 :
        print ("B -grade")
    elif student >= 70 :
        print ("C -grade")
    elif student >= 60 :
        print ("D -grade")
    else:
        print ("F -grade")
else:
    print("wrong score!!")