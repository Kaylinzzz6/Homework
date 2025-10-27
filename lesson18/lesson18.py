# Lesson 18
# Using While Loop
# number = int(input("Number:"))
# factors = 1

# while factors < number:
#     if number % factors == 0:
#         print(f"{factors} is a factor!")
#     factors += 1

# Using For Loops:
number = int(input("Number:"))

for factors in range(1, number+1):
    if number % factors == 0:
        print(f"{factors} is a factor!")