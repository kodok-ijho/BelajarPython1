# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

price = 0

if extra_cheese == "Y" or extra_cheese == "y" :
    price += 1

if size == "S" or size == "s":
    price += 15
    if add_pepperoni == "Y" or add_pepperoni == "y":
        price += 2
if size == "M" or size == "m":
    price += 20
    if add_pepperoni == "Y" or add_pepperoni == "y":
        price += 3
if size == "L" or size == "l":
    price += 25
    if add_pepperoni == "Y" or add_pepperoni == "y":
        price += 3

print(f"Your final bill is: ${price}.")