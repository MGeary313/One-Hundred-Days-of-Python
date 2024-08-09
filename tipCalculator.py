print("Welcome to the tip calculator.")

dinnerBill = float(input("What was the total bill?\n"))
totalTip = int(input("How much would you like to tip? 10, 12, or 15?\n"))
split = int(input("How many people will be splitting the bill?\n"))

totalBill = dinnerBill + totalTip

splitBill = round(totalBill/split, 2)

print(f"Each person should pay: ${splitBill}")