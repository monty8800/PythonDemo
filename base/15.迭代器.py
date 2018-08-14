# 迭代器
from collections.abc import Iterable, Iterator

print(isinstance([],Iterable)) # True
print(isinstance({},Iterable)) # True
print(isinstance('',Iterable)) # True
print(isinstance((x for x in range(1,11)),Iterable)) # True
print(isinstance(100,Iterable)) # False

# 迭代对象(Iterable)和迭代器(Iterator)
# 以上几种为True的都是迭代对象，但它们不是迭代器
print(isinstance([],Iterator)) # False
print(isinstance({},Iterator)) # False
print(isinstance('',Iterator)) # False
print(isinstance((x for x in range(1,11)),Iterator)) # True
print(isinstance(100,Iterator)) # False

# 将迭代对象变成迭代器
print(isinstance(iter([]),Iterator)) # True
print(isinstance(iter('abc'), Iterator)) # True

# Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是
# 惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# 小结：
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。


# Python的for循环本质上就是通过不断调用next()函数实现的，如下
for x in [1, 2, 3, 4, 5]:
    pass
# 完全等同于下面的代码：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
