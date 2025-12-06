# Lesson 39
# Create a function that returns the greatest common divisor between two numbers.
# regular solution
# def gdc(num1, num2):
#     for dividers in range(min(num1, num2), 0, -1):
#         # taking the min, so smallest number because you can't divide the small num by a bigger num, the bigger num has no way to be a factor of small num
#         # 0 to count down, we're doing GDC so we're ocunting down greatest to smallest, first one it finds will therefore be the biggest
#         if num1 % dividers == 0 and num2 % dividers == 0:
#             # if the first numbers and second number are dividible by the divider, it's a common factor
#             return dividers
#     return 1

# do it recursively

def e_gdc(num1, num2):
    if num2 == 0:
        return num1
    else:
        return e_gdc(num2, num1 % num2)