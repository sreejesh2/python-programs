from MyModule import *
while True:
    op=int(input("1.create\n2.Search\n3.Remove\n4.Replace\nEnter your choice"))

    if op==1:
        create()
    elif op ==2:
        search()
    elif op==3:
        Remove()
    elif op==4:
        Replace()
    else:
        print("please enter the valid key\n\n")