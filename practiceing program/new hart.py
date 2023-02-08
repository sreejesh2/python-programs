num = int(input("Enter a number"))
half = round(num/2)

for i in range(2,half):
    for s in range(half-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    for s in range(half-i):
        if s==half:
            print(" ",end="")
        print("  ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
for i in range(num,0,-1):
    print(" "*(num-i)+"*"*(2*i-1))
