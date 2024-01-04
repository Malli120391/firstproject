import random
import logo_img
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen=='hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("Your guess is too low")
        return attempts-1
    else:
        print(f"Your guess is right... The answer was {attempts}")

def game():
    print(logo_img.logo)
    print("Let me think of a number between 1 to 50.")
    answer=random.randint(1,50)
    #print(answer)
    level=input("Choose level of difficulty...type 'easy' or 'hard': ")
    attempts=set_difficulty(level)
    if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
        print("You have entered wrong difficulty level... play again.!")
        return
    guessed_number=0
    while guessed_number!=answer:
      print(f"You have {attempts} reamining to guess the numbers. ")
      guessed_number=int(input("Guess a number:"))
      attempts=check_answer(guessed_number,answer,attempts)
      if attempts==0:
        print("Your are out of guesses... you lose.")
        return
      else:
        print("Guess again")
game()
