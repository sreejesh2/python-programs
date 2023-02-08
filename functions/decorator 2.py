def decorate(func):
    def inner(a,b):
        result=func(a+b)
        return result
    return inner
@decorate
def double(x):
    return 2*x
print(double(2,4))
print("\U0001F618")