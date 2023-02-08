str = input("enter the values")
st = len(str)
a=str.upper()
for i in range(st+2):
    for j in range(0, st):
        if i == 0 or i == st+1:
           print(a[j], end=" ")
        elif j == 0 or j == st-1:
            print(a[i-1], end=" ")
        else:
            print(" ", end=" ")
    print()


