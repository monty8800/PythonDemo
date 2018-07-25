# 1.类的定义和使用
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
# 定义类
class Student(object):
    pass


# 创建对象 - 创建实例通过类名+()实现
bart = Student()
print(bart)  # <__main__.Student object at 0x1089a33c8> - bart 指向一个Student的实例

print(Student)  # <class '__main__.Student'>

# 给实例比变量绑定属性
bart.name = 'Monty'

print(bart.name)


# 增加必需的属性
class Student(object):
    def __init__(self, name, score):  # 相当于java中的构造方法
        self.name = name
        self.score = score


# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
bart = Student('Monty', 90)

print('name:%s,score:%d' % (bart.name, bart.score))  # name:Monty,score:90


# 2.数据封装
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_info(self):
        print('name:%s,score:%d' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'



bart = Student('Mwu', 99)
bart.print_info()  # name:Mwu,score:99

print(bart.name,bart.get_grade()) # Mwu A
