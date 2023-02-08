class A:
    def displaya(self):
        print("its a class")
class B(A):
    def displayB(self):
        print("its b class")
ob=B()
ob.displaya()
ob.displayB()