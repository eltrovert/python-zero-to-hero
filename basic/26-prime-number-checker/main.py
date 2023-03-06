def prime_checker(number):
    prime = True
    if number > 2:
        for i in range(2, number):
            if number % i == 0:
                prime = False
    elif number <= 0:
        print("Number below 0 is invalid format, enter a positive number!")
    else:
        print("It's a prime number.")

    if prime:
        print("It's a prime number.")
    else: 
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
