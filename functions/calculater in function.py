# definition
def add(a,b):
    print("answer is :", a + b)
def sub(a,b):
    print("answer is:",a-b)
def mul(a,b):
    print("answer is :",a*b)
def div(a,b):
    print("answer is :",a/b)
 #  calling
num1=int(input("enter fist number"))
num2=int(input("enter second number"))
op=int(input("1. for addition\n2. for substraction \n"
             "3. for multiplication\n4. for divition\n"
             "please select your option :"))
if op==1:
    add(num1,num2)
elif op==2:
    sub(num1,num2)
elif op==3:
    mul(num1,num2)
elif op ==4:
    div(num1,num2)
else:
    print("please enter a valid option")
