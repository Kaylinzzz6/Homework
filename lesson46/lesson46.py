# Lesson 46
def collatz(n):
    count = 0
    while n >= 1:
        count += 1
        if n == 1:
            return count
        elif n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1

print(collatz(13))

longestChain = 0
num = 0
for i in range(1, 1000000):
    if collatz(i) > longestChain:
        longestChain = collatz(i)
        num = i
        print(i)
print(num)
