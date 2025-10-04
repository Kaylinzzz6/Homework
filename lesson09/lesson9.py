from random import choice # get choice from random

# Ask user to input rock, paper, or scissors
user_choice = input("Choose between rock, paper, and scissors!")

# import choice () from random file (which can ask an AI to calc a response to input)
myset = ["rock", "paper", "scissors"]
random_item = choice(myset)
print(f"Computer chose {random_item}")

# determine if user won
if random_item == user_choice:
    print("It's a tie!")
elif (user_choice == "rock" and random_item == "scissors") \
    or (user_choice == "paper" and random_item == "rock") \
    or (user_choice == "scissors" and random_item == "paper"):
    print("You Win!")
else:
    print("You Lost!")

