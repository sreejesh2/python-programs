#non parameterized constracter

# class A:
#     def __init__(self):
#         print("its a non parameterized constracter")
# obj=A()
class A:
    def __init__(self,name):
        self.na=name
        print("parameterized constracter")
    def display(self):
        print("name is ",self.na)




obj=A('sreejesh')
obj.display()