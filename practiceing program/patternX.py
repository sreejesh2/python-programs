num = int(input("Enter the number"))
for i in range (num):
    print(" "* i+ str(i+1) ,end="")
    if i !=num-1:
        print(" "*(2*num-2*i-3)+str(i+1),end = " ")
    print()
for i in range(num-2,-1,-1):
        print(" " * i + str(i + 1), end="")
        if i != num - 1:
            print(" " * (2 * num - 2 * i - 3) + str(i + 1), end=" ")
        print()