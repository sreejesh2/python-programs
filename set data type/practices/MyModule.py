l1=[]
def create():
    lit=int(input("Enter the limit"))
    print("Enter the values")
    for i in range(lit):
        val=int(input( ))
        l1.append(val)

    print(l1)



def search():
    c=int(input("enter a num"))

    if c in l1:
        print("item found")
    else:
        print("not found")
def Remove():
    c=int(input("enter the num"))
    if c in l1:
      l1.remove(c)
    else:
        print("item not in list")
    print(l1)
def Replace():
    num= int(input("Enter the array value"))
    c=int(input("Enter the replace value"))
    for i in range(len(l1)):
        if l1[i]==num:
            l1[i]=c

    else:
        print("not in the value in the list")
    print(l1)

