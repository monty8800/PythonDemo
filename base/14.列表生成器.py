# 列表生成器

# 1.生成list[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L = list(range(1,11))
print(L) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2.生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1,11):
    L.append(x*x)

print(L) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2.1 简化代码
L = [x * x for x in range(1, 11)] # 等同于上面的循环
print(L) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2.2 加上循环
L = [x * x for x in range(1, 11) if x % 2 == 0] # 筛选出需要的数据
print(L) # [4, 16, 36, 64, 100]


# 2.3 使用双层循环
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L) # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 3.列出当前目录下所有文件和目录名
import os
files = [d for d in os.listdir('.')]
print(files)

# 4.for循环中使用两个或多个变量
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
    print(k,'=',v)


# 4.1 列表生成使用两个变量
d = {'x': 'A', 'y': 'B', 'z': 'C' }
L = [k + '=' + v for k, v in d.items()]
print(L) # ['x=A', 'y=B', 'z=C']


# 4.2 把一个list中所有字符变成小写
L = ['Monty','WuMeng','Apple','Iphone']
L = [s.lower() for s in L] # ['monty', 'wumeng', 'apple', 'iphone']
print(L)

# 测试
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')