num = int(input("enter the size of list"))
print("enter the values of list")
multi = 1
liast1 =[]
for i in range(num):
    my_list=int(input())
    liast1.append(my_list)
for i in liast1:
    multi = multi * i
print(multi)


