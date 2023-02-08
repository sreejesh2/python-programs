num = int(input("enter the array size"))
print("enter the values")
ar=[]
ar1=[]
for i in range(num):
    arrv = int(input())
    ar.append(arrv)
cut=int(input("enter the position to rotate"))
for j in range(1,cut+1):
    ar1.append(j)
array = ar[cut:]+ar1
print("After rotation :")
print(array)