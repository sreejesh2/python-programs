def factorial(num):
    ot=1
    for i in range(2,num+1):
        ot*=i
    return ot
a=int(input("enter a number :"))
print("FACTORIAL: ",factorial(a))