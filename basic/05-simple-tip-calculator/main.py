print("Welcome to the tip calculatpr\n")

# Get an input of the bill and save it as float variable name bill
bill = float(input("What was the total bill? $"))
# Get an input of the tip perscentage and save it as integer variable name tipPercentage
tipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# Get an input of the number of people to split the bill and save it as integer variable name totalPeople
totalPeople = int(input("How many people to split the bill? "))

# Count the tip that we want to give
tip = tipPercentage/100 * bill
# Count the total bill including the tip
totalBill = tip + bill
# Split the bill to the total number of people and round it to two decimal places
splitBill = "{:.2f}".format(round(totalBill / totalPeople, 2))

# Print the split bill value per person 
print(f"Each person sould pay: ${splitBill}")