from loguru import logger as log
# D:\ProgramData\anaconda3\python.exe -m pip install loguru -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 定义日志文件的名字
logfile_path_str = './loguru_test_{time}.log'
# log.add(logfile_path_str) # 把日志文件名字给到日志操作对象

log.add(
    sink=logfile_path_str, # 日志文件名
    # 以下为可选参数
    rotation='200KB', # 设定日志大小， 200k一个文件
    compression='zip', # 设置压缩格式为zip
    retention='72h', # 每隔72小时清理一次日志
    serialize=True, # 默认为False，普通日志；True 把日志改成json格式
    encoding='utf8', # 声明日志文件的编码格式
    level=10 # 日志文件只记录WARNING及更严重级别的日志
    # 10 20 30 40 50 60
)

# 自定义日志信息
log.debug('这是普通级别的日志记录信息') # 相当于 print
log.success('成功了！') # 相当于 print
log.info('正常信息') # 相当于 print
log.warning('警告！')
log.error('异常！错误')
log.critical('严重错误！')

import traceback
# 记录错误异常
try:
    print(5/0)
except:
    # print(traceback.format_exc())
    log.error('*错误记录如下：')
    log.exception('错误信息') # 代替traceback.format_exc()

# 关闭控制台输出，且不写入日志文件
log.remove(handler_id=None)
log.info('这个信息不回显示，111')