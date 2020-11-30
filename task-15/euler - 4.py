x = 100
y = 100
max = 0


def answer(num):
    str_num = str(num)
    y = len(str_num) - 1
    x = 0
    while (x < y):
        if(str_num[x] != str_num[y]):
            return False
        x += 1
        y -= 1

    return True


while(x < 999):
    y = 100
    while(y < 999):
        num = x * y
        if (answer(num)):
            if(num > max):
                max = num
        y += 1
    x += 1

print(max)
