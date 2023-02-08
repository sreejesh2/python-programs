
"""1.write a program to get a string from a given string where all the occurence of its first char have been changed to '$',
the first char itself .
sample o/p:'restart'
o/p:'resta$t'
2.Wap the python function that thakes a list of words and returns the length of the longest one.
"""
str= 'restart'
a=str[0]
str=str.replace(a,'$')
str=a+str[1:]
print(str)

l=['sreejesh','anand','anees',]
m=max(l)
f=len(m)
print(m,'in ',f,'characters')

