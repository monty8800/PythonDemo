# 1.map - map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f(x):
    return x * x


# 1.1 计算平方
r = map(f, [1, 2, 3, 4, 5])  # 将list中的元素依次放入f()方法中执行，并依次返回，组合成一个迭代器
print(list(r))  # [1, 4, 9, 16, 25]

# 1.2 将list中的数字转换成字符串
r = map(str, [1, 2, 3, 4, 5])
print(list(r))  # ['1', '2', '3', '4', '5']

L = [1, 2, 3, 4, 5]

# 2.序列求和 使用 reduce 实现
from functools import reduce


def add(a, b):
    return a + b


print(reduce(add, L))  # 15

# 2.1 使用sum求和
# sum(iterable[, start])
# iterable - 可迭代对象，如：列表、元组、集合。
# start - 指定相加的参数，如果没有设置这个值，默认为0。
print(sum(L, 3))


# 2.2 将[1, 3, 5, 7, 9]变成13579
def fn(a, b):
    return a * 10 + b


print(reduce(fn, L))  # 12345


# 2.3 将str转换成int

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


n = reduce(fn, map(char2num, '123443'))

print(n)  # 123443

# 2.4 整理成一个函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(a, b):
        return a * 10 + b

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


print(str2int('10086'))  # 10086


# 2.5 使用lambda简化
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# 测试1：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    if len(name) == 0:
        return name
    return name[0].upper() + reduce(add, iter(x.lower() for x in name[1:]))


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 测试2：Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(l=None):
    def p(x, y):
        return x * y
    return reduce(p, l)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
