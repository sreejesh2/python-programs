# l1=[x%2==0 for x in [1,4,6,7]]
#
# print(l1)
#
# l=[x for x in range(1,26) if x%2==0]
#
# print(l)

str1=input("enter a string")
# vowels = ['a','e','i','o','u',]
# l=[x for x in str1 if x in vowels]
# print(l)
#
c=str1.split()
a=[i[-1] for i in c]
print(a)
# colors=['red','white','pink','green']
# a=[i for i in colors if i != 'pink']
# print(a)
#
#
# l = [3,7,3,8,9,3,4]
#
# a=[i if i>5 else 0 for i in l]
#
# print(a)
# b=set(a)
# print(b)
# l=[]
# a=[0 if i==5 else i for i in l]
# print(a)