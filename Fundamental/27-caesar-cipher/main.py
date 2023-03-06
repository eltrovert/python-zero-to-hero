from data import alphabet
from art import logo

def caesar(originalText, shiftAmount, cipherDirection):
    cipherResult = ""
    if cipherDirection != "decode" or cipherDirection != "encode":
        print("You input wrong chiper direction!")
    else:
        if cipherDirection == "decode":
            shiftAmount *= -1

        for char in originalText:
            if char in alphabet:
                charPosition =  alphabet.index(char)
                cipherPosition = charPosition + shiftAmount
                cipherResult += alphabet[cipherPosition]
            else:
                cipherResult += char
        print(f"Here's the {cipherDirection}d result: {cipherResult}")

print(logo)

endProgram = False
while not endProgram:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(originalText=text, shiftAmount=shift, cipherDirection=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    endProgram = True
    print("Goodbye")