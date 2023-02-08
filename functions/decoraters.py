def oparations(func):
    def addition(a,b):
        result=func(a+b)
        return result
    return addition


@oparations
def mul(x):
    print('multiplication :',x*2)
mul(5,5)
