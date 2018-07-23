# 切片

# 1.list切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前3个元素
print(L[0:3]) # ['Michael', 'Sarah', 'Tracy'] - 索引从0开始，到索引3结束，但不包含索引3，即0，1，2，三个元素

print(L[:3]) # ['Michael', 'Sarah', 'Tracy'] - 如果第一个索引是0，可以省略

print(L[3:]) # ['Bob', 'Jack'] - 从索引3开始，到最后一个，即3，4，两个元素


print(L[1:3]) # ['Sarah', 'Tracy'] - 从索引1开始，到索引3结束，即1，2，两个元素

# 从后往前取，倒数切片，如果使用倒数切片，那么倒数第一个元素的索引是-1，从-1开始数
print(L[-1:]) # ['Jack'] - 倒数第一个
print(L[-2:-1]) # ['Bob'] - 从索引-2开始，到索引-1结束，包含索引-2，但不包含索引-1，即-2，一个元素
print(L[-3:-1]) # ['Tracy', 'Bob'] - 从索引-3开始，到索引-1结束，包含索引-3，但不包含索引-1，即-3，-2，两个元素
print(L[-3:]) # ['Tracy', 'Bob', 'Jack'] - 从索引-3开始到集合最后，即-3，-2，-1，一共三个元素


# 2.切片的实际使用
L = list(range(100)) # 创建一个从0到99一个100个元素的list
print(L)

# 取前10个数
print(L[:10]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[0:10]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 取后10个数
print(L[-10:])  # [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

# 前11-20个数：
print(L[10:20]) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# 后11-20个数:
print(L[-20:-10]) # [80, 81, 82, 83, 84, 85, 86, 87, 88, 89]

# 前10个数，每两个取一个：
print(L[:10:2]) # [0, 2, 4, 6, 8]

# 所有数，每5个取一个：
print(L[::5]) # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# 什么都不写，相当于复制一个list
print(L[:]) # [0,1,2.....100]


# 2.tuple 切片
T = (tuple(range(10)))
print(T)

print(T[:3]) # (0, 1, 2) - 取前三个数

print(T[-3:]) # (7, 8, 9) - 取后三个数

# 3.str 切片
S = 'ABCDEFG'
print(S[3:]) # DEFG - 从索引3(包含索引3)开始，向右到最后(包含最后一个元素)
print(S[:3]) # ABC - 从索引3(不包含索引3)开始，向左到最后

print(S[:5:2]) # ACE - 前5个数，每两个取一个

print(S[-3:]) # EFG - 从索引-3开始(包含-3)，向右到最后一位，即-3，-2，-1，三个元素

print(S[:-3]) # ABCD - 从索引-3开始(不包含-3)，向左到最后一位，即-4，-5，-6，-7，四个元素

# 测试，实现trim()函数，去除字符串首尾空格
def trim(s):
    if len(s) == 0:
        print(s)
        return s
    elif s[0] == ' ':
        print('>>>>>',s)
        return trim(s[1:]) # 从左往右去空格，如果索引0的元素是空格，则截取从索引1(包含索引1)开始到最后的字符串再次截取
    elif s[-1] == ' ':
        print('<<<<<',s)
        return trim(s[:-1]) # 从右往左去空格，如果索引为-1的元素是空格，则截取从索引-1(不包含索引-1，所以是从索引-2开始的)开始到最后的字符串再次截取
    else:
        return s

print(trim('    中文  我是     ')) # sdf

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')