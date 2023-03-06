import random 
from hangman_art import logo
from hangman_art import stages
from hangman_words import wordList

chosenWord = random.choice(wordList)
wordLenght = len(chosenWord)
gameOver = False
userLives = 6

# Testing word 
print(logo)
print(f'Pssst, the solution is {chosenWord}.')

# Create blank 
display = []
for letter in range(len(chosenWord)):
    display.append("_")

while not gameOver:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(wordLenght):
        if chosenWord[position] == guess:
            display[position] = guess

    if guess not in chosenWord: 
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        userLives -= 1
        if userLives == 0:
            gameOver = True
            print("You lose!")
      
    print(f"{''.join(display)}")

    if "_" not in display:
        gameOver = True
        print("You win!")

    print(stages[userLives])  
