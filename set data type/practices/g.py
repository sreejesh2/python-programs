# s="Let’s google the pineapple"
# r=""
# t=s.split()
# for i in t:
#     y=set(i)
#     h=list(y)
#     for e in h:
#         r=r+e
# print(r)




#
#
# str='cat rat mat cat rat mat sat'
# a=str.split()
# d={}
# for i in a:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)
#
# n=int(input())
#
# for i in range(1,n+1):
#     c.append(i)
# d=str(c)
# print(d)
n = int(input("Enter id"))
count=0
for i in range(2,n):
    if n%i==0:
        count+=1
if count==2:
    print("prime number")
else:
    print("not prime")