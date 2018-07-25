# 获取对象信息
# 1.使用type()判断对象类型,基本类型都可以用type()来判断
print(type(123))  # <class 'int'>
print(type('sdf'))  # <class 'str'>
print(type(None))  # <class 'NoneType'>

print(type(abs))  # <class 'builtin_function_or_method'>


class Studnet(object):
    pass


print(type(Studnet()))  # <class '__main__.Studnet'>

# 比较两个变量类型是否相同
print(type(123) == type(456))  # True
print(type(123) == int)  # True
print(type(123) is not str)  # True
print(type('str') is not str)  # False
print(type('str') is type('sdf'))  # True
print(type('str') is str)  # True

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types


def fn():
    pass


print(type(fn) is types.BuiltinFunctionType)  # False

print(type(abs) == types.BuiltinFunctionType)  # True

print(type(lambda x: x) is types.LambdaType)  # True

print(type((x for x in range(10))) == types.GeneratorType)  # True


# 2.使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
class Animal(object):
    pass


class Dog(Animal):
    pass


class Husky(Dog):
    pass


# 以上3个类的继承关系：object->Animal->Dog->Husky
# 下面使用isinstance()来判断一个对象是否是某种类型
a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Animal))  # True
print(isinstance(d, Husky))  # False

# 3.判断一个对象是否是某些类型中的一种
print(isinstance(d, (Animal, Dog)))  # True
print(isinstance(d, (Animal, Husky)))  # True

# 4.使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir('abc'))  # ['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print(len('abc'))  # 3
print('abd'.__len__())  # 3


# 4.1 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class MyDog(Dog):
    def __len__(self):
        return 100


print(len(MyDog()))  # 100


# 4.2 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyClass(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyClass()

print(hasattr(obj,'x')) # True - 是否有'x'属性
print(obj.x) # 9
print(hasattr(obj,'y')) # False - 是否有'y'属性
setattr(obj,'y',100) # 设置一个'y'属性，并赋值100
print(hasattr(obj,'y')) # True - 是否有'y'属性
print(getattr(obj,'y')) # 100
print(getattr(obj,'z','no')) # no - 获取'z'属性，如果没有默认返回'no'

# 同样，可以用此方法获取对象中的方法是否存在
print(hasattr(obj,'power')) # True
print(getattr(obj,'power')) # <bound method MyClass.power of <__main__.MyClass object at 0x10de327b8>>
# 获取方法并赋值给变量
power = getattr(obj,'power')
print(power()) # 81