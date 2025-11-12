# Lesson 36
def factorsfind(num):
    factors = []
    for x in range(1, num+1):
        if num % x == 0:
            factors.append(x)
    return factors

def primesfind(factors):
    if len(factorsfind(factors)) == 2:
        return "prime!"
    else:
        return "not prime!"

testy = primesfind(13)
print(testy)