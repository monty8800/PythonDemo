# 循环

# 1.for x in ... 遍历list
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 累加
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)  # 55

# range() - 可以生成一个整数序列，再通过list()函数可以转换为list
print(list(range(6)))  # [0, 1, 2, 3, 4, 5]

print(list(range(2, 6)))  # [2, 3, 4, 5] 包前不包后

sum = 0
for x in range(101):  # 0～101之间所有整数累加
    sum = sum + x
print(sum)  # 5050

sum = 0
for x in range(50, 101):  # 50～101之间所有整数累加
    sum = sum + x
print(sum)  # 3825

# 2.while - 只要满足条件，就一直循环

sum = 0
n = 99
while n > 0:
    sum = sum + n
    # 在循环内部变量n不断自减2，直到变为-1时，不再满足while条件，循环退出。
    n = n - 2
print(sum)  # 2500

# break 退出当前循环
n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue 退出当次循环，进入下一次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)  # 1,3,5,7,9
