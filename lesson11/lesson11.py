# input
coordinate = input("What are your coordinates? (e.g. 9, 0)")

# split the text to get left side, x-coordinate and right side, y-coordinate
coordinate = coordinate.split(", ")
coordinate = list(map(int, coordinate))

# assign x and y to coordinate
x, y = coordinate
print(f"x = {x}")
print(f"y = {y}")

# assign to quadrants
if x > 0:
    if y > 0:
        print(f"The coordinate {x, y} is on Quadrant 1")
    else:
        print(f"The coordinate {x, y} is on Quadrant 4")
else: 
    if y > 0:
        print(f"The coordinate {x, y} is on Quadrant 2")
    else: 
        print(f"The coordinate {x, y} is on Quadrant 3")

