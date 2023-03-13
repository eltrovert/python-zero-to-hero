import random
from art import logo
from art import vs
from data import data

dictionaryKey = ["name", "followersCount", "description", "country"]

def generateData():
    """Get data from random account"""
    return random.sample(data, 2)

def printData(generatedData):
    """Format data into printable format: name, description and country"""
    name = generatedData["name"]
    description = generatedData["description"]
    country = generatedData["country"]
    return f"{name}, a {description}, from {country}"

def compare(dataA, dataB):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong."""
    if dataA["followersCount"] > dataB["followersCount"]:
        return "a"
    else:
        return "b"
    

def game():
    gameOver = False
    score = 0
    while not gameOver:
        print(logo)

        generatedData = generateData()

        if score > 0:
            print(f"You're right! curent score {score}")
        
        print(f"Compare A: {printData(generatedData[0])}.")
        print(vs)
        print(f"Agains B: {printData(generatedData[1])}.")

        higherFollowers = compare(generatedData[0],generatedData[1])
        print(higherFollowers)
        userGuess = input("Who has more followers? Type 'A' or 'B': ").lower()
        print(userGuess)
        if userGuess == higherFollowers:
            score += 1
        else:
            gameOver = True
    print(f"Sorry, that's wrong. Final score: {score}")

game()