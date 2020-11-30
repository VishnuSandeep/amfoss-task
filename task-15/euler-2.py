def answer(n):
    xn_2 = 1
    xn_1 = 1
    sum = 0
    while True:
        xn = xn_2 + xn_1
        if xn >= n:
            return sum
        if xn % 2 == 0:
            sum += xn
        xn_2, xn_1 = xn_1, xn


t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    print(answer(n))
