class A:
    def read(self):
        self.a=int(input("enter a number"))

        self.b = int(input("enter a number"))

class B(A):
    def sum(self):
        self.c=self.a+self.b
        print("sum :",self.c)
class C(A):
    def avg(self):
        print("avg :",self.a+self.b/2)
class D(A):
    def mul(self):
        print("mul :",self.a*self.b)
ob1=B()
ob2=C()
ob3=D()
ob1.read()
ob1.sum()
ob2.read()
ob2.avg()
ob3.read()
ob3.mul()