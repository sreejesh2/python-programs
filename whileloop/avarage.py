num = int(input("Howmany numbers u have"))
i=0
list1=[]
sum = 0
print("enter the values")
while(i<num):
    value =int(input())
    list1.append(value)
    sum=sum+list1[i]
    i=i+1
avarage=sum/num

print(avarage)