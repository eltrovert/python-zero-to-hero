print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

firstStep = input('You are at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()

if firstStep == "left":
    secondStep = input('You have come across a beautiful lake, and there is an islan in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()

    if secondStep == "wait":
        thirdStep = input('You arrive at the island unharmed. There is a castle with 3 door. Red, yellow, and blue. Which colour do you choose?\n').lower()

        if thirdStep == "yellow":
            print("Congratulations! You have come to the treasure room and found the treasure chest")
        elif thirdStep == "red":
            print("Ouch. You are burn by a fire trap. Game Over!")
        elif thirdStep == "blue":
            print("Woahhhh. You are eaten by a beasts. Game Over!")
        else:
            print("Game Over!")
    else: 
        print("You are attacked by trout. Game Over!")
else:
    print("You are fallen to a hole. Game Over!")