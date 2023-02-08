def count(a):
    c=0
    d=0
    for i in range(len(a)):
        if a[i] in ['a','e','i','o','u','A','E','I','O','U']:
            c=c+1
        else:
            d=d+1


    print("vowels count is :",c)
    print("consonant is :",d)

count('sreejesh')