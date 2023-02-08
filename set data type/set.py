"""
immutable
unordered
un indexed
not allow duplicates
set items are unchangabale ,but you can remove items and add items.
"""
r={30,4,2,6,8}
s =  {1.0,2,4,"hello",(1,2,3,)}
a=['daw',9,3]

#print('union', s|r)
#print('intersection',s & r)
#print('difference',s-r)
#print('symmetic element',s^r)

#1
s.update(a)
print(s)
#2
print(s|r)
#3
if s & r:
    print(s & r)
else:
    print('not in commen')

#4
set1={10,20,30,40,50,}
set2= {30,40,50,60,70}
print(set1 & set2)


