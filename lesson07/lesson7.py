# Lesson 7 Baldur's Gate 3

import random

# Program takes in a single integer reps DC
DC = int(input("What is the difficulty set by the dungeon master?"))

# rolls a number from 1-20, reps the modifier
D20 = int(random.randrange(1,21))

# if DC < rolled number, task was successful
if DC < D20:
    print("Player has succeeded!")
else:
    print("Player was not successful.")