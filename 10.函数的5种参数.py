# 函数的参数
def power(x):
    if not isinstance(x, (int, float)):  # 类型校验 如果x不是int或者float就抛出异常
        raise TypeError('只允许传入int和float类型')
    return x * x


# print(power('3')) # TypeError: 只允许传入int和float类型
print(power(3.14))  # 9.8596


# 1.多个参数
def power(x, n):  # x代表基数，n代表n次方
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(2, 3))  # 8


# 2.默认参数 - 必选参数在前，默认参数在后
# 由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(2))  # 4 - 当我们调用power(2)时，相当于调用power(2, 2)：


def enroll(name, gender, age=6, city='BeiJing'):
    student = {'name': name, 'gender': gender, 'age': age, 'city': city}
    print(student)


enroll('Monty', '男')  # {'name': 'Monty', 'gender': '男', 'age': 6, 'city': 'BeiJing'}
enroll('Monty', '男', 60, 'ShenZhen')  # {'name': 'Monty', 'gender': '男', 'age': 60, 'city': 'ShenZhen'}
enroll('Monty', '男', city='MaCheng')  # {'name': 'Monty', 'gender': '男', 'age': 6, 'city': 'MaCheng'}


# 传入list类型的数据
def add_end(l=[]):
    l.append('End')
    return l


print(add_end([]))  # ['End']

l = [1, 2]
print(add_end(l))  # [1, 2, 'End']

print(add_end(['x', 'y', 'z']))  # ['x', 'y', 'z', 'End']

print(add_end())  # ['End']
print(add_end())  # ['End', 'End'] - 再次调用add_end()时，结果就不对了.默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list


# 要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('End')
    return L


print(add_end())  # ['End']
print(add_end())  # ['End'] - 无论调用多少次，都不会有问题,结果一直是['End']


# 3.可变参数 - 可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
# 使用list或tuple
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))  # 14 - 调用时先组装一个list
print(calc((1, 3, 5, 7)))  # 84 - 调用时先组装一个tuple


# 使用可变参数 - 在参数前面加一个*，参数numbers接收到的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))  # 14 - 不需要组装list或tuple，直接传入多个参数
print(calc(1, 3, 5, 7))  # 84
print(calc())  # 0

# 如果已经有一个list或tuple要调用一个可变参数的函数
nums = [1, 2, 3]
# print(calc(nums)) # TypeError: can't multiply sequence by non-int of type 'list'
print(calc(*nums))  # 14 - 在lsit或tuple前加一个*，*nums表示把nums这个list的所有元素作为可变参数传进去。


# 4.关键字参数 - 使用**作为关键字参数的前缀
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):  # 函数person除了必选参数name和age外，还接受关键字参数kw.
    print('name:', name, 'age:', age, 'kw:', kw)


# 可以只传入必填参数
person('Monty', 1)  # name: Monty age: 1 kw: {}
# 任意个关键字参数
person('Monty', 1, city='ShenZhen')  # name: Monty age: 1 kw: {'city': 'ShenZhen'}
person('Monty', 1, city='ShenZhen', job='dev')  # name: Monty age: 1 kw: {'city': 'ShenZhen', 'job': 'dev'}
# 将dict作为关键字参数 - 使用**作为前缀
d = {'city': 'ShenZhen', 'job': 'dev', 'key': 100}
person('Monty', 2, **d)  # name: Monty age: 2 kw: {'city': 'ShenZhen', 'job': 'dev', 'key': 100}


# 5.命名关键字参数
# 检查需要的关键字参数是否存在
def person(name, age, **kw):
    if 'city' in kw:  # 关键字参数字典中是否有'city'这个字段
        pass
    if 'job' in kw:  #
        pass
    print('name:', name, 'age:', age, 'kw:', kw)


# 限制关键字的参数名字
def person(name, age, *, city, job):  # 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)


# person('Monty',12,'ShenZhen','dev') # TypeError: person() takes 2 positional arguments but 4 were given - 这种调用是错的，*右边两个参数必须使用参数名

person('Monty', 100, city='ShenZhen', job='dev')  # name: Monty age: 100 city: ShenZhen job: dev


# 使用已定义的可变参数
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


# person('Jack', 24, 'Beijing', 'Engineer') # TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job' - 由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。

person('Monty', 100, city='ShenZhen', job='dev')  # Monty 100 () ShenZhen dev
person('Monty', 100, 1, 2, 3, 4, city='ShenZhen', job='dev')  # Monty 100 (1, 2, 3, 4) ShenZhen dev
# person('Monty',100,1,2,3,4) # TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'
person(1, 2, 3, 4, city='ShenZhen', job='dev')  # 1 2 (3, 4) ShenZhen dev


# 可变参数规则，必填参数和关键字参数中间可以是任意个参数(tuple)

# 命名关键字参数可以有缺省值，从而简化调用：
def person(name, age, *, city='BeiJing', job):
    print(name, age, city, job)


# 由于命名关键字参数city具有默认值，调用时，可不传入city参数
person('Monty', 1, job='dev')  # Monty 1 BeiJing dev
person('Monty', 1, city='Sz', job='dev')  # Monty 1 Sz dev


# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass


# 6.参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def m(a, b, c=3, *d, **kw):  # 带有可变参数d,命名关键字参数前不需要加*分隔
    #  ，参数类型依次是:必选参数'a' - 必选参数'b' - 默认参数'c' - 可变参数'd' - 民命关键字参数'kw'
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 只传入必选参数
m('monty', 1)  # a = monty b = 1 c = 3 d = () kw = {}

# 传必选参数和重置默认参数
m(1, 2, c=5)  # a = 1 b = 2 c = 5 d = () kw = {}

# 传入必选参数，重置默认参数，和可变参数
m(1, 2, 3, 'a', 'b', 'sdf')  # a = 1 b = 2 c = 3 d = ('a', 'b', 'sdf') kw = {}

# 传入必选参数，重置默认参数，可变参数,和命名关键字参数
m(1, 2, 3, 'a', 'b', 'sdf', city='sz')  # a = 1 b = 2 c = 3 d = ('a', 'b', 'sdf') kw = {'city': 'sz'}

# 传入必选参数，和命名关键字参数
m(1, 2, d=99, ext=None)  # a = 1 b = 2 c = 3 d = () kw = {'d': 99, 'ext': None}

# 传入必选参数，可变参数为lsit，和命名关键字参数
l = [1, 2, 3]
m('monty', 11, 'dev', *l, other='other')  # a = monty b = 11 c = dev d = (1, 2, 3) kw = {'other': 'other'} - 可变参数为list

# 传入必选参数，可变参数为tuple,其中的()括号可以省略，和命名关键字参数
m('monty', 11, 6, 1, 2, 3,
  other='other')  # a = monty b = 11 c = 6 d = (1, 2, 3) kw = {'other': 'other'} - 可变参数为tuple

# 传入一个tuple和dict
t = (1, 2, 3, 4, 5, 6)
d = {'d': 100, 'x': '###'}
m(*t, **d)  # a = 1 b = 2 c = 3 d = (4, 5, 6) kw = {'d': 100, 'x': '###'}


def n(a, b, c, **kw):  # 不带可变参数
    print('a =', a, 'b =', b, 'c =', c, 'kw =', kw)


n('monty', 1, 32, age=10)  # a = monty b = 1 c = 32 kw = {'age': 10}


# 依次打印num集合中的值的n次方
def product(n=2, *num):
    for i in num:
        print('%s的%s次方是:%s' % (i, n, pow(i, n)))


lis = list(range(1, 10))
product(3, * lis)
