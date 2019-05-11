错误：Non-ASCII character '\xe5'
原因：Python的默认编码文件是用的ASCII码，而你的python文件中使用了中文等非英语字符。
url:https://blog.csdn.net/idlehand/article/details/77253294
解决方法：
 在Python源文件的最开始一行，加入一句：

# coding=UTF-8（等号换为”:“也可以）

或者

# -*- coding:UTF-8 -*-