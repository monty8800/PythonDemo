# filter
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

L = [1,2,3,4,5,6,7,8,9]
# 1.在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1

l = list(filter(is_odd,L)) # 过滤偶数
print(l) # [1, 3, 5, 7, 9]

# 2.删掉一个序列中的空字符串
S = ['s','',' ',1,'   ']

def not_empty(s):
    return s and str(s).strip()

l = list(filter(not_empty,S)) # 剔除空字符串
print(l) # ['s', 1]