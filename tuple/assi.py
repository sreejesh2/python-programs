t = (1,2,40,30,20)
#print(t[-1])

#x=all(t)
#print(x)
#2
tp=(1,2,40,[10,2,39],(30,20,10),40)
f=tp[4][1]
print(f)
lt=list(tp)
for i in lt:
    if lt.count(i)>1:
        lt.remove(i)
        print(lt)

''''''''''''''''''''''''''''''
v=[]
v.append(tp[1])
print(v)

k=t
t=tp
tp=k
print(tp)

