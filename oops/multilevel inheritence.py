class A:
    def read(self):
        self.a=int(input("enter a number"))
        self.b = int(input("enter a number"))
class B(A):
    def sun(self):
       self.c= self.a+self.b
class C(B):
    def avg(self):
        self.avg= self.c/2
        print(self.avg)
ob=C()
ob.read()
ob.sun()
ob.avg()