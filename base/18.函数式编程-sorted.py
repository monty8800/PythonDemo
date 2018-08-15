# sorted
L = [1, 2, 5, -3, 3, 4]
l = sorted(L)
print(l)  # [-3, 1, 2, 3, 4, 5]

# sorted是一个高阶函数，可以接收一个key函数来实现自定义排序
l = sorted(L, key=abs)  # 按绝对值大小排序
print(l)  # [1, 2, -3, 3, 4, 5]

# 字符串排序 - 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
s = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(s)  # ['Credit', 'Zoo', 'about', 'bob']

s = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)  # 忽略大小写
print(s)  # ['about', 'bob', 'Credit', 'Zoo']

# 反向排序 加上 reverse=True
s = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(s)  # ['Zoo', 'Credit', 'bob', 'about']

# 测试：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# 请用sorted()对上述列表分别按名字排序：

# 根据名称排序
def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)


# 根据成绩从高到底排序
def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score, reverse=True)
print(L2)
