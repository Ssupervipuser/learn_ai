def describe_inputs(*args,**kwargs):
    print(args)
    print(f'位置参数个数：{len(args)}')

    print(f'关键字参数个数{len(kwargs.keys())}')

    for k in kwargs.keys():
        print(f'关键字参数的键:{k}')


describe_inputs(1, 'hello', 3.14, name='Alice', age=25, city='Beijing')