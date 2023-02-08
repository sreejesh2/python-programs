# a= int(input("enter first number"))
# b= int(input("enter second number"))

# m=lambda a,b:a*b
#
# print(m(a,b))

#if statement

# lar= lambda a,b:a if a>b else b
# print("largest number :",lar(a,b))

#filter,map,reduce
#
# l=[20,45,23,2,6]
# lst1=list(filter(lambda x:x%2==0,l))
# print(lst1)
# #
l1= [20,45,23,2,6]
# lst2=list(map(lambda n:n*2,l1))
# print(lst2)

from functools import reduce

p=reduce(lambda a,b:a+b,l1)
print(p)




