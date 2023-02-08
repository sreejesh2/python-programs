str1 = input("Enter a string")
str2 = input("Enter a another string")
str1.lower()
str2.lower()
if (len(str1)==(len(str2))):
    s1=sorted(str1)
    s2=sorted(str2)
    if s1 == s2:
        print(str1+"\t and \t"+str2+ "\tis anagram ")
    else:print(str1+"\tand\t"+str2+ "\tis not anagram")
else:
    print("not anagram")
