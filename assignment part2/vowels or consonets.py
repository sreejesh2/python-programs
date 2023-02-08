flag=0
letr = input("Enter the letter")
li= ['A','E','I','O','U','a','e','i','o','u']
for i in range(len(li)):
    if letr == li[i]:
        flag=1
        break
if flag==1:
    print("its a vowel number")
else:
    print("its a constant")