# 访问限制

# 私有变量 -  以__开头
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s : %d'%(self.__name,self.__score))

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self,score): # 在方法中处理业务逻辑
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')



bart = Student('Mwu',90)

# print(bart.__name) # 访问私有变量报错 - AttributeError: 'Student' object has no attribute '__name'

bart.print_score() # Mwu : 90

print(bart.get_name()) # Mwu - 通过类中提供的方法访问name属性

bart.set_name('Monty') # 通过类中提供的方法修改name

bart.print_score() # Monty : 90

# bart.set_score(-1) # set_score()中校验了score的值必须在0-100之间，否则报错 - ValueError: bad score
bart.set_score(100)
bart.print_score() # Monty : 100

# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，
# 不是private变量，所以，不能用__name__、__score__这样的变量名。
#
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样
# 的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
#
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了
# _Student__name，所以，仍然可以通过_Student__name来访问__name变量：
print(bart._Student__name) # Monty

# 测试
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('receive only male or female')

bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')