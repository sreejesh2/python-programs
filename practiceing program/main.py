num =5
for i in range(1,num+1):

    for s in range(i):
        print(" ",end="")
        for j in range(1):
            print(i)
        if i!=num:
           for k in range(2*num-2*i-3):
               print("$",end=" ")
           for f in range(num,1):
               print(i)
    print()


