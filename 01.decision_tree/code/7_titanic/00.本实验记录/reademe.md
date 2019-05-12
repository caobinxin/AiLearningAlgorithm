
运行： python -u 0_feature.py
错误：AttributeError: 'file' object has no attribute 'buffer'
解决方案：http://www.cnblogs.com/sundahua/p/10206801.html
    注销：sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
