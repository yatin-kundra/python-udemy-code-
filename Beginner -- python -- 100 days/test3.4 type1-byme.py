# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
total = 0
if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            total = 15 + 2 + 1
            print(f"yo+ur grand total is ${total}")

        else:
            total -= 1
            print(f"yo+ur grand total is ${total}")

    else:
        if extra_cheese == "Y":
            total = 15 + 1
            print(f"yo+ur grand total is ${total}")

        else:
            total -= 1
            print(f"yo+ur grand total is ${total}")

# medium size

elif size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            total = 20 + 2 + 1
            print(f"yo+ur grand total is ${total}")

        else:
            total -= 1
            print(f"yo+ur grand total is ${total}")

    else:
        if extra_cheese == "Y":
            total = 20 + 1
            print(f"yo+ur grand total is ${total}")

        else:
            total -= 1
            print(f"yo+ur grand total is ${total}")

# large size

elif size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            total = 25 + 2 + 1
            print(f"yo+ur grand total is ${total}")

        else:
            total -= 1
            print(f"yo+ur grand total is ${total}")

    else:
        if extra_cheese == "Y":
            total = 25 + 1
            print(f"yo+ur grand total is ${total}")

        else:
            total -= 1
            print(f"yo+ur grand total is ${total}")


else:
    print("invald input")




