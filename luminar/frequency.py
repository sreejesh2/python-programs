str ='sreejesh'
count =0
d=[]

def isexist(c):
    for i in d:
        if i==c:
            return False
    return True





for i in str:
    if isexist(i):
        d.append(i)
        for j in str:
            if i==j:
               count+=1
        print(i," ",count)
        count=0


