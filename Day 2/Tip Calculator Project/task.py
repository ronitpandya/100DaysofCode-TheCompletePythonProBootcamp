print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
totalbill = bill * ((tip/100) + 1)
final = round((totalbill / people), 2)
print(f"Everyone should pay {final} amount")

