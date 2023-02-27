# Get user current age as age variable
age = input("What is your current age? ")

# Count the ages left of the user with assumtion that all people died at the age 90. Save it to age_left variable as integer
age_left = 90 - int(age)
# Count the days left of the user by multiply by 365 (days a year) and save it to days_left variable as string
days_left=str(age_left * 365)
# Count the weeks left of the user by multiply by 52 (weeks a year) and save it to weeks_left variable as string
weeks_left=str(age_left * 52)
# Count the months left of the user by multiply by 12 (months a year) and save it to months_left variable as string
months_left=str(age_left * 12)

# Print the days, weeks, and months left of the user
print("You have " + days_left + " days, " + weeks_left + " weeks, and " + months_left + " months left.")




