# -*- coding: utf-8 -*-

# 字符串和编码

# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
print('包含中文的str')

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
# 获取字符的整数表示
a = ord('a')
b = ord('中')
print(a,b)

# 编码转换为对应的字符
a = chr(66)
b = chr(20013)
print(a,b)

print('\u4e2d\u6587') # 字符的整数编码,用16进制写

# bytes,bytes类型的数据用带b前缀的单引号或双引号表示。在bytes中，无法显示为ASCII字符的字节，用\x##显示。
x = b'ABC' # 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

# encode() 编码
print('ABC'.encode('ascii')) # b'ABC'

print('中文'.encode('utf-8')) # b'\xe4\xb8\xad\xe6\x96\x87'

# print('中文'.encode('ascii')) # 报错，含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围

# decode() 解码
print(b'ABC'.decode('ascii')) # ABC

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')) # 中文

# print(b'\xe4\xb8\xad\xff'.decode('utf-8')) # 报错，无法解码

# errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')) # 中

# len() 计算字符长度
print(len('aaa')) # 3
print(len('中文')) # 2

# 如果类型是bytes，len()函数计算的就是字节数
print(len(b'aaa')) # 3
print(len(b'\xe4\xb8\xad\xe6\x96\x87')) # 6
print(len('中文'.encode('utf-8'))) # 6,可见一个中文字符占了3个字节，而一个英文字符只占1个字节


# 格式化，在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：
print('Hello, %s' % 'world') # Hello, world
print('Hi, %s, you have $%d.' % ('Michael', 1000000)) # Hi, Michael, you have $1000000.
# %s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('name:%s,age:%d'%('Monty',25)) # name:monty,age:25

# 如果字符串中%是一个普通字符，通过%%进行转义
print('name:%s %% age:%d'%('Monty',25)) # name:Monty % age:25

# format() 使用传入的参数依次替换字符串内的占位符
print('Hello, {0}, 成绩提升了 {1}%'.format('小明', 17.125))

# 练习：小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位
s1 = 72
s2 = 85
t = (s2-s1)/100*100

print('小明的成绩提升了%s%%' % t)
