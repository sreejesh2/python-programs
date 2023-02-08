num = int(input("enter the number"))
k=(2*num)-2
for i in range(0,num):
    for j in range(1,num-i):
        print(end=" ")

    for j in range(0,i+1):
        print("*",end=" ")
    print()
