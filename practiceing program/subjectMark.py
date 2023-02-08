mark1 = int(input("Enter the physics mark:\n"))
mark2 = int(input("Enter the chemistry mark:\n"))
mark3 = int(input("Enter the biology mark:\n"))
mark4 = int(input("Enter the mathematics mark:\n"))
mark5 = int(input("Enter the computer mark:\n"))
per = ((mark1+mark2+mark3+mark4+mark5)*100/500)
print("Your percentage : ",per,"%")
if per>100:
    print("You have entered  invalid mark ")
elif per<=100 and per>=90:
    print("A Grade")
elif per>= 80:
    print("B Grade")
elif per>= 70:
    print("C Grade")
elif per>=60:
    print("D grade")
elif per >=50:
    print("E grade")
elif per>=40:
    print("F Grade")
else:
    print("FAIL !!!!!")
