num=int(input("enter num"))
try:
    for i in range(2,int(num/2)+1):
        if num % i ==0:
            print("not")
            break
        else:
            print("prime")
except Exception as e:
    print("not prime",e)

