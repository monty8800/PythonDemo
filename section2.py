# 数据类型和变量

# 1.字符串
# 字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。请注意，''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。如果'本身也是一个字符，那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符。
print('a')  # 单引号
print("b")  # 双引号
print("'c'")  # 字符串中本身包含单引号
print('I\'m \"OK\"!')  # 字符串中本身包含单引号和双引号 使用\转义
print('I\'m learning\nPython.')  # \n 换行
print('\\\n\\')  # \\转义为\

print('\\\t\\')

print(r'\\\t\\')  # r''表示''内部的字符串默认不转义

# '''...'''的格式表示多行内容
print('''line1
... line2
... line3''')

# \n不转义，并换行(...可省略)
print(r'''hello,\n
world''')
print('\n\n\n')

# 2.布尔
print(True)  # True

print(3 == 2)  # False

# and
print(True and True)  # True
print(True and False)  # False
print(False and False)  # False
print(5 > 2 and 3 < 4)  # True

# or
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
print(5 < 2 or 3 < 4)  # True

# not
print(not True)  # False
print(not False)  # True
print(not 1 < 2)  # False
print(not 1 == 2)  # True

# if...else
# age = input('请输入年龄:')
#
# if int(age) >= 18:
#     print('你是成年人了!')
# else:
#     print('你是未成年，请远离游戏!')


# 3.变量
a = 1  # 整形
b = '123'  # 字符串
c = True  # boolean

c = b  # 不同类型可以赋值

print('c =', c)

x = 10
x = x + 2  # 赋值语句先计算右侧的表达式x + 2，得到结果12，再赋给变量x。由于x之前的值是10，重新赋值后，x的值变成12。
print('x =',x)

a = 'ABC'
b = a
a = 'XYZ'
print(b) # ABC

# 4.常量
PI = 3.14159265359 # 通常用全部大写的变量名表示常量,但事实上PI仍然是一个变量,Python根本没有任何机制保证PI不会被改变,所以,用全部大写的变量名表示常量只是一个习惯上的用法,如果你一定要改变变量PI的值,也没人能拦住你。

# 除法
print(10 / 3) # 3.3333333333333335

print(9 / 3) # 3.0

# 地板除，两个整数的除法仍然是整数,只取结果的整数部分
print(10 // 3) # 3

# 余数
print(10 % 3) # 1



