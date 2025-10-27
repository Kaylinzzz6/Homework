# Lesson 19
# input
number = int(input("Number:"))
factors = 2
is_prime = True # assume true until it's divisable

while factors < number:
    if number % factors == 0:
        is_prime = False #it ain't prime
        break
        factors += 1

if is_prime and number > 1:
    print(f"{number} is a prime number!")
else:
    print(f"{number} is not a prime number!")
