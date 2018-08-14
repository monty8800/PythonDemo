# 返回函数

# 1.函数作为返回值
# 求和函数
def calc_sum(*args):
    ax = 0
    for x in args:
        ax = ax + x
    return ax


# 不直接返回结果，而是返回一个函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
fu = lazy_sum(1,2,3,4,5,6)

print(fu) # <function lazy_sum.<locals>.sum at 0x10392d378>

# 调用fu时才进行求和
print(fu()) # 21

# 2.闭包

