from enum import Enum
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 打印枚举中的所有成员
for name,member in Month.__members__.items():
    print(name,'->',member,',',member.value) # value属性则是自动赋给成员的int常量，默认从1开始计数。


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import unique

@unique # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Sun) # Weekday.Sun
print(Weekday['Sun']) # Weekday.Sun
print(Weekday.Sun.value) # 0
print(Weekday(1)) # Weekday.Mon


# 测试：把Student的gender属性改造为枚举类型，可以避免使用字符串：
@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        if isinstance(gender,Gender):
            self.gender = gender
        else:
            raise ValueError('只允许接收Gender类型的参数')

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
