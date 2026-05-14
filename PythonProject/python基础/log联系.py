from loguru import logger as log

logfile_path_str='loguru_test_{time}.log'
log.add('logfile_path_str')
log.add(
    sink='logfile_path_str',
    rotation='200KB',
    compression='zip',
    retention='72h',
    serialize=True,
    encoding='utf-8',
)
# 自定义日志信息
log.debug('debug级别调试消息')
log.success('成功调用')
log.info('普通消息') # 常用
log.warning('警告消息')
log.error('错误消息')
log.critical('严重错误消息')

# try:
#     print(5/0)
# except:
#     log.exception('err')