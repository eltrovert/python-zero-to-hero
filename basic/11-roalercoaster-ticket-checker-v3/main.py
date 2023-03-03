print("Welcome to the roalercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("Congratulation, you can ride the roalercoaster!")

    age = int(input("What is your age? "))

    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age > 18:
        print("Adult tickets are $12")
        bill = 12
    else:
        print("Youth tickets are $7.")
        bill = 7
    
    photoService = input("Do you want a photo taken? Y or N. ")
    
    if photoService == "Y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride this roalercoaster")