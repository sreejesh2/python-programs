# class fact():
#     def factorial(self,num):
#         self.a=num
#         f=1
#         for i in range(1,self.a+1):
#             f=f*i
#         return f
#
#
# obj=fact()
# print(obj.factorial(5))

class fact:

    def fac(self,num):
        self.c=num
        if self.c==1:
            return 1
        else:
            return self.c*self.fac(self.c-1)

obj=fact()
d=obj.fac(5)
print(d)