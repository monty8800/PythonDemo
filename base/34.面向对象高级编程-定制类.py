# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
#
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
#
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

# 1.__str__
class Student(object):
    def __init__(self, name):
        self.name = name


print(Student('Monty'))  # <__main__.Student object at 0x10dff6400>


# 打印出一堆<__main__.Student object at 0x109afb190>，不好看。
#
# 怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    # __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。通常__str__()和__repr__()代码都是一样的
    __repr__ = __str__


print(Student('Mwu'))  # Student object (name: Mwu)

# 2.__iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，
# Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# 裴波那契数列
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

# for n in Fib():
#     print(n)

# 3.__getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# print(Fib()[5]) # TypeError: 'Fib' object does not support indexing


# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

print(Fib()[5])


# 但是list有个神奇的切片方法：
print(list(range(100))[5:10]) # [5, 6, 7, 8, 9]

# print(Fib()[1:3]) # TypeError: 'slice' object cannot be interpreted as an integer

# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print(f[1:10]) # [1, 2, 3, 5, 8, 13, 21, 34, 55]

# 但是没有对step参数作处理：
print(f[:10:2]) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# 没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
#
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
#
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
#
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

# 4.__getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
# 动态返回一个属性
class Student(object):
    def __init__(self):
        self.name = 'mwu'
    def __getattr__(self, item):
        if item == 'score':
            return 100 # 直接返回score的值,调用 s.score
        if item == 'age':
            return lambda : 25 # 返回一个函数,调用 s.age()

s = Student()

print(s.score) # 100

print(s.age()) # 25

# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
print(s.abc) # None
# print(s.abc()) # TypeError: 'NoneType' object is not callable

# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：

class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25 # 返回一个函数，调用age()
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

# print(Student().adb) # AttributeError: 'Student' object has no attribute 'adb' - 抛出我们预期的异常

# 例子：REST API
# 利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list) # /status/user/timeline/list

# 无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
# 还有些REST API会把参数放到URL中，比如GitHub的API： GET /users/:user/repos
# 调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：Chain().users('michael').repos 就可以非常方便地调用API了

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().users('mwu').timeline.list) # /users/mwu/timeline/list


# 5.__call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name) # My name is mwu.

s = Student('mwu')
s()
Student('Monty')() # My name is Monty.

# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
#
# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
#
# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，
# 比如函数和我们上面定义的带有__call__()的类实例：

print(callable(Student)) # True
print(callable(max)) # True
print(callable([1,23,4])) # False
print(callable(None)) # False
print(callable('str')) # False

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。




