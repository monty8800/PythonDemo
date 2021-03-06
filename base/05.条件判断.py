# 条件判断

# if...else...
age = 15
if age >= 18:
    print('你成年了!!!')
    print('可以恋爱了!!!')
else:
    print('未成年!!!')
    print('滚回去读书!!!')

# if...elif...
# age = input('输入你的年龄:')
age = 5
if int(age) >= 18:
    print('你是成年人了')
elif int(age) >= 6:
    print('你是青少年了')
else:
    print('你还是个小屁孩')

# 简写,只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = 1
if x:
    print('True') # True

# 类型转换
# s = input('birth: ')
s = 2015
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后') # 00后

# 练习：小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = float(input('输入你的身高(cm):')) / 100
weight = float(input('输入你的体重(kg):'))

# round(x,y) x值保留位小数
bmi = round(weight / pow(height, 2),2)
print(bmi)
if bmi>32:
    print("严重肥胖")
elif bmi>=28:
    print('肥胖')
elif bmi>=25:
    print('过重')
elif bmi>=18.5:
    print('正常')
else:
    print('过轻')

