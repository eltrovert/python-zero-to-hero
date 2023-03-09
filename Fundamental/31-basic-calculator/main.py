from art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def devide(n1, n2):
    return n1 / n2
    
def calculator():
    print(logo)

    num1 = int(input("What's the first number?: "))
    print("Valid operator:")
    for symbol in operations:
        print(symbol)
    
    
    isFinished = False
    while not isFinished:
        operatorValid = False
        while not operatorValid:
            symbol = input("Choose a valid operator: ")
            if symbol in operations:
                operatorValid = True

        num2 = int(input("What's the next number?: "))

        result = operations[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {result}")
        
        nextCalculation = input(f"Type 'y' to continue calculating with {result}, or 'n' to stop calculating. ").lower()
        if nextCalculation == "n":
            isFinished = True
            
        num1 = result

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : devide
}

calculator()