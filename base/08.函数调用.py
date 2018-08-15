# 调用函数

# abs() - 绝对值
print(abs(100)) # 100
print(abs(-20)) # 20
print(abs(3.1415926)) # 3.1415926
print(abs(-3.1415926)) # 3.1415926

# max() - 最大值
print(max(1,2,3,-1,100,33)) # 100

# min() - 最小值
print(min(3,2,4,5,1)) # 1

# 数据类型转换
print(int('123')) # 123 - str -> int
print(int(3.1415925)) # 3 - float -> int
print(float('3.14')) # 3.14 - str -> float
print(str(3.1415)) # 3.1415 - float -> str
print(str(100)) # 100 - int -> str

print(bool(1)) # True - int -> bool
print(bool(0)) # False - int -> bool
print(bool(4)) # True - int -> bool
print(bool('')) # False - str -> bool
print(bool('a')) # True - str -> bool
print(bool()) # False

# 函数指向 - 函数名其实就是指向一个函数对象的引用，可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
print(a(-9.9)) # 9.9 - 等同于abs()

# 练习：利用hex()函数把一个整数转换成十六进制表示的字符串
n1 = 255
n2 = 1000
l = [n1,n2]
h = []
for n in l:
    h.append(hex(n))
print(h) # ['0xff', '0x3e8']


