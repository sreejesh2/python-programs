class A:
    def read(self):
        self.name=input("Enter the name")
        self.age =int(input("Enter the age"))
        self.place = input("Enter the place")
class B:
    def write(self):
        self.salary=int(input("enter the salary"))
        self.anual_incom=int(input("enter income"))
class C(A,B):
    def display(self):
        print(self.name)
        print(self.age)
        print( self.place)
        print(self.salary)
        print( self.anual_incom)

obj=C()
obj.read()
obj.write()
obj.display()