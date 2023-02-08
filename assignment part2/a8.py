str= input("enter a string")
d=[]
for i in str:
    count=0
    for j in str:
        if i==j :
            count+=1
        if count>1:
            break
    if count==1:
        print(i)

