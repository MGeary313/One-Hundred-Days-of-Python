import random

print("Welcome to password generator")

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]


#ask user how many letters, numbers, and symbols in their PW'
passwordLetters = int(input("How many letters do you want in your password? "))
passwordNumbers = int(input("How many numbers do you want in your password? "))
passwordSymbols = int(input("How many symbols do you want in your password? "))

password = []

pwL = 0
pwN = 0
pwS = 0

while pwL < passwordLetters:
    password.append(random.choice(letters))
    pwL+=1

while pwN < passwordNumbers:
    password.append(random.choice(numbers))
    pwN+=1

while pwS < passwordSymbols:
    password.append(random.choice(symbols))
    pwS+=1        

random.shuffle(password)

passwordString = "".join(password)

print(f"Your new password is {passwordString}")


