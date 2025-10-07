#  mini - project ⭐️

#  Quiz game -
#  Create a quiz game to ask the user 5 questions and check their answers.
#  using loops, conditional statements, and data structures.

# questions for the quiz
questions = ("How many elements are in the periodic table?",
            "Which animal lays the largest eggs?",
            "What is the most abundant gas in Earth's atmosphere?",
            "How many bones are in the human body?",
            "Which planet in the solar system is the hottest?")

# options for the questions
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
            ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
            ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
            ("A. 206", "B. 207", "C. 208", "D. 209"),
            ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answer = ("C","D","A","A","B")
score = 0
question_num = 1

# print the question and options
for question in questions:
    print("---------------------------\n")
    print(f"{question_num}).{question}")
    for option in options[question_num-1]:
        print(option)
    print()
    select = input("Enter your answer(A,B,C,D): ").upper()
    while select not in ("A","B","C","D") : # check the valid option 
        print("----enter valid option----\n")
        select = input("Enter your answer(A,B,C,D): ").upper()

    # check the answer and calculate the score
    if select == answer[question_num-1]:
        print("--> CORRECT")
        score += 1
    else:
        print("--> INCORRECT!")
        print(f"{answer[question_num-1]} is the correct answer")
    question_num += 1

# print the result of the quiz 
print("---------------------------")
print("          RESULT          ")
print("---------------------------\n")

print(f"Your Correct answer is {score} out of {len(questions)}.")
print(f"Your Score is - {score/len(questions)*100:.2f}%\n")
