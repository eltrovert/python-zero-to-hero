import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock, paper, scissors]

yourChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computerChoice = random.randint(0,2)
print(f"{choice[yourChoice]}\n")

print(f"Computer choose:\n{choice[computerChoice]}")


if yourChoice >= 3 and yourChoice < 0:
  print("You choose a number outside the choice!")
elif yourChoice == computerChoice:
  print("Draw.")
elif yourChoice == 0 and computerChoice == 2:
  print("You win.")
elif yourChoice == 2 and computerChoice == 1:
  print("You win.")
elif yourChoice == 1 and computerChoice == 0:
  print("You win.")
else:
  print("You lose")
