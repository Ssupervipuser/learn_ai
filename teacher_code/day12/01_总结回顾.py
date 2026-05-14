
def outter2(outter1_inner):
    def inner(a, b):
        ret = outter1_inner(a, b)
        return ret
    return inner

def outter1(func):
    def inner(a, b):
        ret = func(a, b)
        return ret
    return inner


@outter2
@outter1
def func(a, b):
    return 123