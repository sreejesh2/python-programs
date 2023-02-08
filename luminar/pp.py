num = int(input("Enter a number"))
for i in range(num):
    for s in range(i):
        print(" ",end="")
    for j in range(num-i):
        print(" * ",end="")
    print("\n\n")
