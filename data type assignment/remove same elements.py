str = "Let's google the pineaple"
str1 = str.split()
st2=[]
for i in str1:
    a=' '
    for j in i:
        if j in a:
            continue
        else:
            a=a+j
            st2.append(a)

    print(''.join(a),end=' ')