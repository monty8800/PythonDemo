# 使用dict和set

# 1.dict 字典，类似java中的map
d = {'name':'monty','sex':'男'}

# 取值
print('名称:',d['name']) # 名称: monty
print('性别:',d['sex']) # 性别: 男

# 赋值
d['name'] = 'mwu'
print('名称:',d['name']) # 名称: mwu

# 避免key不存在的情况(1)
if 'name' in d:
    print('名称:', d['name']) # 名称: mwu

if 'age' in d:
    print('年龄:', d['age'])
else:
    print('没有找到age') # 没有找到age

# 避免key不存在的情况(2),通过get获取
name = d.get('name') # 存在
print('名称:',name) # 名称: mwu

age = d.get('age') # 不存在，返回None
print('年龄:',age) # 年龄: None

# 指定默认值
age = d.get('age',15) # 获取key为age的值，如果找不到此key，则返回默认值 15
print('年龄:',age) # 年龄: 15

# 删除元素
print(d.pop('name')) # mwu - 删除key为name的元素
print(d) # {'sex': '男'}



# 2.set - 和dict类似，也是一组key的集合，但不存储value

s = set([1,2,3])
print(s) # {1, 2, 3} - 传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。

s = set([1, 1, 2, 2, 3, 3]) # {1, 2, 3} - 重复元素在set中自动被过滤

# add() - 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s) # {1, 2, 3, 4}
s.add(4)
print(s) # {1, 2, 3, 4}

# remove()
s.remove(4)
print(s) # {1, 2, 3}

# 交集&并集
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1&s2) # {2, 3} - 交集
print(s1|s2) # {1, 2, 3, 4} - 并集

# 不可变对象
# 可变对象list,对list进行操作，list内部的内容是会变化的
a = ['c','b','a']
a.sort() # 排序
print(a) # ['a', 'b', 'c']
# 不可变对象string
a = 'abc'
a.replace('a','z')
print(a) # abc - 虽然字符串有个replace()方法，也确实变出了'Abc'，但变量a最后仍是'abc'

# 如何改变
a = 'abc'
b = a.replace('a','z')
print(a) # abc
print(b) # zba - replace方法创建了一个新字符串'zbc'并返回，使用一个新的变量b来接收改变后的值


print(tuple(range(1,4)))





