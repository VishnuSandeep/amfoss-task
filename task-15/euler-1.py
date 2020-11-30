def sum(n, k):
    v = n // k
    return k * (v * (v+1)) // 2


def answer(n):
    return sum(n, 3) + sum(n, 5) - sum(n, 15)


t = int(input().strip())
for i in range(t):
    N = int(input().strip())
    print(answer(N-1))
