# 递归函数

# 1.阶乘 n! = 1 x 2 x 3 x ... x n
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

# 递归函数如果调用次数过多会导致栈溢出，比如fact(1000)，会出现RecursionError: maximum recursion depth exceeded in comparison，
# 要解决递归调用栈溢出，需要使用尾递归优化，


print(fact(1000))
