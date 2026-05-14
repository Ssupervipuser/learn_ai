def myfun(n=10):
    if n<1:
        return
    print(n)
    myfun(n-1)


myfun(10)


def func(n=5):
    if n==1 or n==0:
        return 1
    return n*func(n-1)

ret=func(5)
print(ret)
