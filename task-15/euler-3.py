import math


def answer(n):
    maxPrime = -1

    while n % 2 == 0:
        maxPrime = 2
        n >>= 1

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n //= i

    return n if n > 2 else maxPrime


t = int(input().strip())
for _ in range(t):
    N = int(input().strip())
    print(answer(N))
