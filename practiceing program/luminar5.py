num = int(input("enter the number"))
asci=65
for i in range(num):
    for k in range(num-i):
        print(" ",end= "")
    for j in range(i+1):
        print(chr(asci),end= " ")
        asci+=1
    print()