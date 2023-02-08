num = int(input("Enter a number"))

def fact(num):
    outp=1
    for i in range(2,num+1):
        outp*=i
    return outp

print(fact(num))
