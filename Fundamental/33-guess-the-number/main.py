import random
from art import logo

EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5

def setDificulty():
    difficultty = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if difficultty == "easy":
        return EASY_LEVEL_LIVES
    else:
        return HARD_LEVEL_LIVES

def compare(guess, number, lives):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess < number:
        print("Too low.")
        return lives - 1
    elif guess > number:
        print("Too high.")
        return lives -1
    elif guess == number:
        print(f"You got it! The answer {guess}")
    else:
        print("Wrong format")

def guess():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    misteryNumber = random.randint(1, 101)
    print(f"Pssst, the mistery number is {misteryNumber}")
    lives = setDificulty()

    guess = 0
    while guess != misteryNumber:
        print(f"You have {lives} attemps remaining to guess the number")
        guess = input("Make a guess: ")
        
        if guess.isdigit():
            guess = int(guess)
            lives = compare(guess, misteryNumber, lives)
            if lives == 0:
                print("You've run out of guesses, you lose.")
                return
            elif guess != misteryNumber:
                print("Guess again. ")
        else:
            print("You did not type a number")
            lives -= 1

guess()



