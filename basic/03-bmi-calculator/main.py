# Get an input of the user height
height = input("enter your height in m: ")
# Get an input of the user weight
weight = input("enter your weight in kg: ")

# Calculate BMI based on BMI Formula. The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)
# Convert the weight into integer or float, and the height into float
bmi = float(weight) / (float(height) ** 2)

# Print BMI result as integer to make sure it written as whole number
print(int(bmi))