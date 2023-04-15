import random

print("Welcome to the dice roller!")

while True:

    print(" _______ ")
    print("|       |")
    print(f"|   {random.randint(1, 6)}   |")
    print("|_______|")


    roll_again = input("Do you want to roll the die again? (y/n): ")


    if roll_again.lower() != "y":
        print("Goodbye!")
        break
