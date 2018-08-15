#使用list和tuple

# 1.list
classmates = ['Monty','Wu','Boy']
print(classmates) # ['Monty', 'Wu', 'Boy']

print(len(classmates)) # 3

# 使用索引访问数组中的元素
print(classmates[0]) # Monty
print(classmates[1]) # Wu
print(classmates[2]) # Boy

# 获取最后一个元素
print(classmates[-1]) # Boy
# 获取倒数第二个元素
print(classmates[-2]) # Wu
# 获取倒数第三个元素
print(classmates[-3]) # Wu

# append()追加元素
classmates.append('MC')
print(classmates) # ['Monty', 'Wu', 'Boy', 'MC']

# append()插入元素到指定位置
classmates.insert(1,'HaHa')
print(classmates) # ['Monty', 'HaHa', 'Wu', 'Boy', 'MC']

# pop()删除末尾元素,返回被删除的元素
print(classmates.pop()) # MC
print(classmates) # ['Monty', 'HaHa', 'Wu', 'Boy']

# pop(i)删除指定位置元素
print(classmates.pop(1)) # HAHA
print(classmates) # ['Monty', 'Wu', 'Boy']

# 替换某个元素的值
classmates[1] = 'M' # 直接赋值
print(classmates) # ['Monty', 'M', 'Boy']

# 不同类型的元素
L = ['Monty',123,True]
print(L) # ['Monty', 123, True]

# 包含另一个list
P = ['Monty',['M',1],'Wu']
print(P) # ['Monty', ['M', 1], 'Wu']
print(len(P)) # 3
print(P[1]) # ['M', 1]
print(len(P[1])) # 2


# 2.tuple - tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy') # classmates这个tuple不能变了，它也没有append()，insert()这样的方法
print(classmates.index('Bob')) # 1 - 取'Bob'的下标
print(classmates[0]) # Michael

# 定义的歧义
# 如果定义一个tuple，只包含一个元素，必须使用,结尾
P = (1,)
print(P) # (1,)

P = ("Mwu",1)
print(P) # ('Mwu', 1)

# 可变的tuple，tuple中包含list
t = ('a', 'b', ['A', 'B'])
print(t) # ('a', 'b', ['A', 'B'])

t[2][0] = 'Monty' # 改变tuple下标为2的list中下标为0的元素
print(t) # ('a', 'b', ['Monty', 'B']) - 表面上看tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple的每个元素，指向永远不变。

# 练习：请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])











