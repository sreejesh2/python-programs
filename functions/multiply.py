def multi(num):
    out = 1
    for i in num:
        out *= i
    return out
print(multi([8, 2, 3, 6, 7]))