def students(a):
    l=[2,7,9,3,6,56,43,23,54]
    if a in l:
       print("student is present" )
    else:
        print("student is absent")


s=int(input("enter student rol number"))
students(s)