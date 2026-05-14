# import a

# 这样的导包、导模块的方式，可以突破__all__白名单的限制
# from a import sum, foo, bar

# todo 使用*导入所有时，白名单__all__生效
from a import *
# 相当于 form a import a的__all__中的对象
# from a import sum, foo


print(sum)

ret = foo(1,2)
print(ret)

ret = bar(1, 2)
print(ret)