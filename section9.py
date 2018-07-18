# 定义函数 - 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def _my_abs(x):
    if x > 0:
        return x
    else:
        return -x

print(_my_abs(-3.14)) # 3.14

# 空函数 - 如果想定义一个什么事也不做的空函数，可以用pass语句.
def nop():
    pass # pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

def nop1(age):
    if age>18:
        pass #缺少了pass，代码运行就会有语法错误。

# 参数检查 - 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
# print(_my_abs(1,2)) # TypeError: _my_abs() takes 1 positional argument but 2 were given

# print(_my_abs('x')) # 参数类型错误 - TypeError: '>' not supported between instances of 'str' and 'int'

# print(abs('x')) # 参数类型错误，但是系统函数会校验数据类型 - TypeError: bad operand type for abs(): 'str'

# 加上类型检查 - 数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('类型错误，只允许接收int和float类型')
    if x > 0:
        return x
    else:
        return -x

# print(my_abs('a')) # TypeError: 类型错误，只允许接收int和float类型


# 返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x,y = (move(100,100,60,math.pi/6)) # 多个变量单独接收
print(x) # 151.96152422706632
print(y) # 70.0

xy = move(100,100,60,math.pi/6) # 一个变量接收

print(xy) # (151.96152422706632, 70.0) - 此处可以看出，实际上返回的并不是多个值，而是一个tuple，在语法上，返回一个tuple可以省略括号。所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。





