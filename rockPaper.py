import random

print("Welcome to Rock, Paper, Scissors.")

gameChoices = ["Rock", "Paper", "Scissors"]

playerchoice = input("Choose 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
computerChoice = random.choice(gameChoices)

if playerchoice == "0" and computerChoice == gameChoices[1]:
    print ("Computer chose Rock. Computer wins")
elif playerchoice == "0" and computerChoice == gameChoices[0]:
    print ("Tie game, you both chose rock.")
elif playerchoice == "0" and computerChoice == gameChoices[2]:
    print ("Computer chose Scissors. You win.")

if playerchoice == "1" and computerChoice == gameChoices[1]:
    print ("Computer chose paper. Tie game.")
elif playerchoice == "1" and computerChoice == gameChoices[0]:
    print ("Computer chose Rock. You win.")
elif playerchoice == "1" and computerChoice == gameChoices[2]:
    print ("Computer chose Scissors. Computer wins.")

if playerchoice == "2" and computerChoice == gameChoices[1]:
    print ("Computer chose paper. You win.")
elif playerchoice == "2" and computerChoice == gameChoices[0]:
    print ("Computer chose rock. Computer wins.")
elif playerchoice == "2" and computerChoice == gameChoices[2]:
    print ("Computer chose scissors. Tie game.")