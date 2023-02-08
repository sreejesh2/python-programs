def even_or_odd(num):
    if num % 2==0:
        c="number is even"
    else:
        c='number is odd'
    return c
n=int(input("Enter a number"))
print(even_or_odd(n))