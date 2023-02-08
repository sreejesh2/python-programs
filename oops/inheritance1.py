class A:
    def read(self):
        self.a=int(input("enter a number"))
        self.b = int(input("enter a number"))
class B(A):
    def sum(self):
        self.sum=self.a+self.b
        print(self.sum)
obj=B()
obj.read()
obj.sum()