# Lesson 38
def palincheck(num):
    return num == num[::-1]

palindrom_nums = []

for num1 in range (999, 99, -1):
    for num2 in range(999, 99, -1):
        current_product = num1 * num2

        if palincheck(str(current_product)):
        # have palin number
            palindrom_nums.append(current_product)

print(max(palindrom_nums))