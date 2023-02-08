def outer(a):
    def inner(b):
        nonlocal a
        return a + b

    return inner


func = outer('haii')
print(func('\tsreejesh'))
