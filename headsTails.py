import random


while True:

    flipChoice= input("Heads or Tails?").lower()

    flip = random.randint(0, 1)
    if flipChoice == "heads" and flip == 0:
        print("Heads! You win!")
    elif flipChoice == "heads" and flip == 1:
        print("Tails. You lose.")
    elif flipChoice == "tails" and flip == 0:
        print("Heads. You lose.")
    elif flipChoice == 'tails' and flip == 1:
        print ("Tails. you win.")
    else:
        print ("Please choose Heads or Tails.")