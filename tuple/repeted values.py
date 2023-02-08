t=(2,6,8,4,8,3,2,'sree')
rt=[]
lt=list(t)
ee=lt.copy()
for i in lt:
    if lt.count(i) > 1:
        lt.remove(lt[i])
        #print(lt)
        rt.append(i)
x=set(rt)
u=tuple(x)
print('repeated elements :',u)


