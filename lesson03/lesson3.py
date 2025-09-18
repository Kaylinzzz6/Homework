# Lesson 3 CCC Squares Problem

# called import statements, makes it so the number from sqrt is always rounded down
from math import sqrt, floor

tiles_amount = int(input("Number of Tiles:"))

# **0.5 is another way of square rooting
# can also write as side_length = floor(sqrt(tiles_amount))
side_length = sqrt(tiles_amount)
side_length = floor(answer)

print(f"The largest square has a side length of {side_length}.")