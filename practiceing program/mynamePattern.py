str = ['S','R','E','E','J','E','S','H']
for i in range(10):
    for j in range(0,8):
        if( i==0 or i==9 ):
            print(str[j],end =" ")
        elif(j==0 or j==8-1):
            print(str[i-1],end =" ")
        else:
            print(" ",end =" ")
    print()
