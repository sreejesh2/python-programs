class A:
    def display(self,name=None):
        if name is None:
            print("hello")
        else:
            print("hello"+name)

obj=A()
obj.display()
obj.display(" sreejesh")