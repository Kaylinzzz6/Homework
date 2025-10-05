# input
a = int(input("What is your first angle?"))
b = int(input("What is your second angle?"))
c = int(input("What is your third angle?"))
angles = [a, b, c]

# to check if sum is 180
total_angle = sum(angles)

# see if equiladeral, scalene or iscoseles and calc sum
if a == b == c and total_angle == 180 :
    print("You have an equilateral triangle!")
elif a == b or b == c and total_angle == 180:
    print("You have an isosceles triangle!")
elif total_angle == 180:
    print("You have a scalene triangle")
else:
    print("you don't got a triangle...")
