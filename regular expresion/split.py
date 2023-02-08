import re
str= 'class will start at 10am'
s=re.split(r'a',str)
print(s)


str= 'class will start at 10am'
s=re.split(r' ',str,2)
print(s)