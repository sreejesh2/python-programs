import re
# str= 'class will start at 10am'
# s=re.search(r'\d',str)
# print(s)

# str= 'class will start at 10am'
# s=re.search(r'python',str)
# print(s)

str= 'class will start at 10am'
s=re.search(r'^class.*10am$',str)
if s:
    print("find")
else:
    print("not find")
