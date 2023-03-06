import math

def paintCalculator(height, width, cover):
    totalCans = math.ceil((height * width) / cover)
    print(f"You'll need {totalCans} cans of paint.")

wallHeight = int(input("Height of wall: "))
wallWidth = int(input("Width of wall: "))
coverage = 5
paintCalculator(height=wallHeight, width=wallWidth, cover=coverage)

