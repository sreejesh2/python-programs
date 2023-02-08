number= int(input("enter the limit"))
d1={}
for i in range(number):

    key=input("enter the key")
    val=input("enter the value")
    d1.update({key:val})
print(d1)

