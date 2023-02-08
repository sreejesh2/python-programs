def prime(num):
    for i in range(2,int(num/2)+1):
        if num % i==0:
            c="not prime"
            break
        else:
           c="prime number"

    return c
n=int(input("enter"))
print(prime(n))