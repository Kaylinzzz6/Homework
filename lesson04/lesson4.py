# Lesson 4 Painting Fences

section1 = input("Enter planks in section 1: ")
section2 = input("Enter planks in section 2: ")
section3 = input("Enter planks in section 3: ")

#len() short form for length, counts characters in a string or items in a list- basically anything with countable data
cans = len(section1) + len(section2) + len(section3)

# import statement -> used to bring one module to another, we took ceil from math module
from math import ceil

# need to round up because you can have too many planks because they'll just be left over but too less won't have enough planks
# ceil() rounds the # up
boxes = ceil(cans / 12)
leftover = 12*boxes - cans

total_cost = 14.95 * boxes

# outputs
print(f"We need {cans} cans of paint")
print(f"We have {leftover} leftover")
print(f"The project will cost ${total_cost}.")
