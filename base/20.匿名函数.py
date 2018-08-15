# 匿名函数
l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]


# 其中的 lambda x: x * x 就是匿名函数，直接使用lambda，不需要函数名，不用写返回值
# lambda x: x * x 分解如下:
def fun(x):
    return x * x


# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

fun = lambda x: x * x
print(fun)  # <function <lambda> at 0x10c1d82f0> - 返回的是一个函数

print(fun(10))  # 100


# 将匿名函数作为返回值
def bind(x, y):
    return lambda: x * x + y * y


print(bind(10, 3))  # <function bind.<locals>.<lambda> at 0x100d27378>
print(bind(10, 3)())  # 109

# 测试：
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))

print(L) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
