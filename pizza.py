print ("Welcome to pizza builder")

size = input("What size pizza do you want? S, M, or L:\n").title()
pepperoni = input("Do you want pepperoni? Y or N:\n").title()
extraCheese = input("Do you want extra cheese? Y or N:\n").title()

cost = 0

small = 15
medium = 20
large = 25
smallPepperoni = 2
mediumLargePepperoni = 3
cheese = 1



if size == "S":
    cost = cost + small
elif size == "M":
    cost = cost + medium
elif size == "L":
    cost = cost + large
elif size != "S" and size != "M" and size != "L":
    print("Please choose a size S, M, or L")

if size == "S" and pepperoni == "Y":
    cost = cost + smallPepperoni
elif size == "S" and pepperoni == "N":
    cost = cost
elif size == "M" or size == "L" and pepperoni == "Y":
    cost = cost + mediumLargePepperoni
else:
    cost = cost

if extraCheese == "Y":
    cost = cost + cheese
else:
    cost = cost

print(f"Your total bill is: ${cost}")
