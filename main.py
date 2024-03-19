from quiz_database import question_bank
from quiz_database import options
print("***************************")
print("Welcome to My Quiz Game!!!!!")

score = 0
def check_answer(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False
for question_num in range(len(question_bank)):
    print("*********************************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
    guess = input("Enter Your answer(A/B/C/D): ").upper()
    is_correct = check_answer = (guess, question_bank[question_num]["answer"])
    if is_correct:
        print("Correct_answer")
        score += 1
    else:
        print("Incorrect_answer")
        print(f"The correct answer is {guess, question_bank[question_num]['answer']}")
    print(f"The correct answer is {score}/{question_num+1}")
print(f"Your have given {score} correct answer")
print(f"Your score is {(score/len(question_bank))*100}%")
