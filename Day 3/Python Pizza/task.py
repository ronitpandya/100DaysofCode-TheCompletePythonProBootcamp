

print("Welcome to Python Pizza Deliveries!")
cost = int("0")
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    cost += 15
elif size == "M":
    cost += 20
elif size == "L":
    cost += 25

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        cost += 2
    else :
        cost += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    cost += 1
else :
    cost += 0

print(f"Your final bill is: ${cost}.")