print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combinedName = name1 + name2

t = combinedName.lower().count('t')
r = combinedName.lower().count('r')
u = combinedName.lower().count('u')
e = combinedName.lower().count('e')
l = combinedName.lower().count('l')
o = combinedName.lower().count('o')
v = combinedName.lower().count('v')

firstDigit = t + r + u + e 
secondDigit = l + o + v + e
score = int(str(firstDigit) + str(secondDigit))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")