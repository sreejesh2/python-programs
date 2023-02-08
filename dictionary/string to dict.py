from collections import Counter
str1='luminar'
dict1={}
for i in range(1,len(str1)+1):
    dict1.setdefault(i,str1[i-1])
print(dict1)




