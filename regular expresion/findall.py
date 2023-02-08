import re
# str= "i am a very lazy and very bad"
# s=re.findall('ry',str)
# print(s)


# s='cat vat saw met sat'
# r=re.findall('[sv]',s)
# print(r)

#
# s='cat vat saw met sat'
# r=re.findall('[^sv]',s)
# print(r)


# s='cat999 vat9584 saw677 met992 999sat 999 999'
# r=re.findall('\d{3}',s)
# print(r)

# s='cat999 vat9584 saw677 met992 999sat 999 999'
# r=re.findall('\d{1,3}',s)
# print(r)

s='cat999 vat9584 saw677 met992 999sat 999 999'
r=re.findall(r'\b\d{3}\b',s)
print(r)