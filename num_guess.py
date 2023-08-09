#Number guesser
import random
try_again = True

def generate():
    ans_num = random.randint(1,100)
    return ans_num

def compare(ans_num,user_num):
    user_status = ""
    if user_num > ans_num:
        user_status = "High"
    elif user_num < ans_num:
        user_status = "Low"
    else:
        user_status = "Win"
    return user_status

while try_again == True:
    attempts = 10
    win = False

    ans_num = generate()
    
    print("--------------------------------")
    print("Welcome to the Number Guessing Game!")

    difficulty = input("Choose a difficulty: Easy or hard\n").lower()
    if difficulty == "hard":
        attempts = 5
    
    print("I'm thinking of a number between 1 and 100.")
    
    while attempts > 0:
        print(f"You have {attempts} attempt(s)")
    
        user_num = int(input("Guess the number: "))
        user_status = compare(ans_num,user_num)
    
        if user_status == "High":
            attempts = attempts - 1
            print("Too high")
        elif user_status == "Low":
            attempts = attempts - 1
            print("Too low")
        else:
            print("-----")
            print(f"You win! The answer was {ans_num}")
            attempts = 0
            win = True
            
        if attempts == 0 and win == False:
            print("-----")
            print(f"The answer was {ans_num}")
            
    if attempts == 0:
        ask_tryagain = input("Try again?: ").lower()
        if ask_tryagain == "yes":
            try_again = True
        else:
            try_again = False