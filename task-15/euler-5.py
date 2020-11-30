from math import gcd
from functools import reduce


def LCM(a, b):
    return a // gcd(a, b) * b


N = int(input())
print(reduce(LCM, range(N//2+1, N+1)))
