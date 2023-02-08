arraysize = int(input("enter the size of the array"))
print("enter the values of array")
ar = []
for i in range(arraysize):
    arrayval = (input())
    ar.append(arrayval)
print("unsorted array :",ar)
ar.sort()
print("sorted :",ar)
