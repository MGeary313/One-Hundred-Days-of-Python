print("Welcome to Treasure Island\n")
print("Your mission is to find the treasure\n")

while True:
    crossroad = input("You're at a cross road. Where do you want to go? Left or Right?\n").title()
    if crossroad == "Right":
        print("You fall into a hole. Game over.")
        break
    elif crossroad == "Left":
        while True:
            river = input("You come to a raging river. Do you want to attempt to swim across? Yes or No:\n").title()
            if river == "Yes":
                print("You drown attempting to cross the river. Game over.")
                break
            elif river == "No":
                while True:
                    door = input("A wagon comes along and offers you a ride. Do you get in through the Red, Blue, or Yellow door?\n").title()

                    if door == "Red":
                        print("The door was booby trapped. Game over.")
                        break
                    elif door == "Blue":
                        print("The horse panics and kicks you, breaking your legs. Game over.")
                        break
                    elif door == "Yellow":
                        print("You win! You have made it to the end of the game.")
                        break
                    else:
                        print("Please choose Red, Blue, or Yellow\n")
                        continue
                break
            else:
                print("Please choose Yes or No.")
                continue
        break
    else:
        print("Please choose Left or Right.\n")
