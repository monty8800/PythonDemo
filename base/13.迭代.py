# 迭代

# 1.字典迭代
d = {'a': 1, 'b': 2, 'c': 3}

# 迭代key
for k in d:
    print(k)  # a,b,c

# 迭代value
for v in d.values():
    print(v)  # 1,2,3

# 同时迭代key和value
for m in d.items():
    print(m)  # ('a', 1),('b', 2),('c', 3)

# 2.字符串迭代
for s in 'Monty':
    print(s)

# 3.判断一个对象是否可迭代 Iterable
from collections.abc import Iterable

print(isinstance('abcsdf', Iterable))  # True 可迭代

print(isinstance([1, 2, 3], Iterable))  # True 可迭代

print(isinstance(123, Iterable))  # False 不可迭代

# 4.list实现下标 - enumerate
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)

# 结果:
# 0 a
# 1 b
# 2 c


for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


# public class Max {
#     public static void main(String[] args) {
#         double[] myList = {1.9, 2.9, 3.4, 3.5,10,11,15,100,-1,-4.5};  //定义一维数组
#         double num = myList[0]; //0为第一个数组下标
#           for (int i = 0; i < myList.length; i++) {   //开始循环一维数组
#              if (myList[i] > num) {  //循环判断数组元素
#                  num = myList[i]; }  //赋值给num，然后再次循环
#           }
#           System.out.println("最大值为" + num); //跳出循环，输出结果
#       }
# }

# 测试：使用迭代查找一个list中最小和最大值，返回一个tuple
def findMinAndMax(l=None):
    if l is None:
        l = []
    m = l[0]
    n = l[0]
    for i in l:
        if i > m:
            m = i
        if i < n:
            n = i
    return m, n


L = [10, 3, 22, 55, -99, 101]

print(findMinAndMax(L))
