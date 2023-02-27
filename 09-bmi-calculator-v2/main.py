# Get an input of the user height
height = input("enter your height in m: ")
# Get an input of the user weight
weight = input("enter your weight in kg: ")

# Calculate BMI based on BMI Formula. The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)
# Convert the weight into integer or float, and the height into float
bmi = round(float(weight) / (float(height) ** 2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")