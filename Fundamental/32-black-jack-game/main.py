import random
from art import logo

def drawCard():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cardDrawn = random.choice(cards)
    return cardDrawn
    
def firstDraw(hand):
    hand.append(drawCard())
    hand.append(drawCard())
    return hand

def totalScore(hand):
    """Take a list of cards and return the score calculated from the cards"""
    if len(hand) == 2 and sum(hand) == 21:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(userScore, dealerScore):
    if userScore > 21 and dealerScore > 21:
        return "You went over. You lose 😤"
    elif userScore == dealerScore:
        return "It's a Draw 😤"
    elif dealerScore == 0:
        return "Dealer got BlackJack! You lose 😤."
    elif userScore == 0:
        return "Congratulation you got BlackJack! You Win"
    elif userScore > 21:
        return "You went over. You lose 😤"
    elif dealerScore > 21:
        return "Dealer went over. You Win"
    elif userScore > dealerScore:
        return "You Win"
    else:
        return "You lose"

def blackjack():
    print(logo)
    userHand = []
    dealerHand = []
    endGame = False

    firstDraw(userHand)
    firstDraw(dealerHand)
    
    while not endGame:
        userScore = totalScore(userHand)
        dealerScore = totalScore(dealerHand)

        print(f"   Your cards: {userHand}, current score: {userScore}")
        print(f"   Computer's first card: {dealerHand[0]}")        

        if userScore == 0 or dealerScore == 0 or userScore > 21:
            endGame = True
        else:  
            continueGame = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if continueGame == "y":
                userHand.append(drawCard())
            else:
                endGame = True
    
    while dealerScore < 17 and dealerScore != 0:
        dealerHand.append(drawCard())
        dealerScore = totalScore(dealerHand)

    print(f"   Your final hands: {userHand}, current score: {userScore}")
    print(f"   Dealers final card: {dealerHand[0]}")

    print(compare(userScore, dealerScore))

blackjack()