class rectangle():
    def area(self,l,b):
        print("area of rectangle is :",l*b)

class square(rectangle):
    def area(self, l, b):
        print("area of square is :", l * b)
obj=square()
obj.area(2,5)