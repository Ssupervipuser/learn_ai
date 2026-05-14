

def outter(bar):
    def inner(a):
        ret = bar(a)
        return ret
    return inner
@outter
def bar(a):
    return a + 1
ret = bar(a=2)
print(ret)



def outter(bar):
    def inner(a):
        ret = bar(a)
        return ret
    return inner

def bar(a):
    return a + 1

inner = outter(bar)
ret = inner(a=2)
print(ret)


def outter2(outter_inner):
    print(2)
    def inner(a):
        ret = outter_inner(a)
        return ret
    return inner

def outter(bar):
    print(1)
    def inner(a):
        ret = bar(a)
        return ret
    return inner

@outter2
@outter
def bar(a):
    return a + 1

ret = bar(a=2)
print(ret)