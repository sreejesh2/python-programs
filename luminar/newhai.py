num = int(input("enter a number"))
for i in range (num):
    for j in range (num):
        if i+j==2 or   i-j==2 or i+j==6 or i==1 and j==num-2 :
          print("*",end=" ")
        else:
            print(" ",end="")
    print()