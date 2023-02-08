year = int(input("enter the number"))
if year % 400 == 0 or year % 100 !=0  and year % 4== 0 :

    print("its a leap year")
else:
    print("not a leap year")
