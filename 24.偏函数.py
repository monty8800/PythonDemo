# 偏函数
# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。
# 在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。

# 进制转换 - base 默认值为10,如果传入base参数，就可以做N进制的转换
s = '1223321'
print(int(s, base=8))
print(int(s, base=16))


# 进制转换封装 - 默认使用二进制
def int2(n, base=2):
    return int(n, base)


print(int2('1010001111'))  # 655

# functools.partial
import functools

int2 = functools.partial(int, base=2)
print(int2('00111111')) # 63
print(int2('01010101')) # 85

# 接收函数对象、*args和**kw这3个参数

max2 = functools.partial(max, 13)
#实际上会把10作为*args的一部分自动加到左边，也就是：
max2(5, 6, 7)
#相当于
args = (10, 5, 6, 7)
m = max(*args)

print(m)
print(max2(5, 6, 7))