# numbers from 1-50
for number in range(51):
    # if divisible by 3 (%3 == 0), print Fizz
    if number % 3 == 0:
        print("Fizz")
    # if divisible by 5 (%5 == 0), print Buzz
    elif number % 5 == 0:
        print("Buzz")
    # if both, (elif %3 and %5 ??) print FizzBuzz
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # otherwise print the number (else print)
    else:
        print(f"{number}")

#YAY I DID THIS IN ONLY 15 MINUTES OMGOGMGOM