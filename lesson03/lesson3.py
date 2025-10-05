from math import floor

# input
tiles = int(input("Tiles amount:"))

# square root tiles and get side length, it's ** 0.5
side_length = tiles ** 0.5
side_length = floor(side_length)

# ouput
print(f"The side length of of the square from your tiles is {side_length}")