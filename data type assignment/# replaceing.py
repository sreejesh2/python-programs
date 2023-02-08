str1 = '/*Jon is @developer & musician!!'
m=''
for i in range(len(str1)):
    if str1[i]=='/' or str1[i]=='@' or str1[i]=='*' or str1[i]=='&' or str1[i]=='!':
        m=m+'#'
    else:
        m=m+str1[i]
print(m)
