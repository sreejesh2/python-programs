num = int(input("Enter the number"))
for i in range(0,num+1):
    print(" "*(num-i)+" *"*(i+1))
for i in range(num-1,-1,-1):
    print(" "*(num-i)+" *"*(i+1))
