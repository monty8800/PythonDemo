
# 现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

# 肉食动物
class CarnivorousMixIn(object):
    pass

# 植食动物
class HerbivoresMixIn(object):
    pass

# 多重继承
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal,RunnableMixIn,CarnivorousMixIn): # 多重继承
    pass

class Bat(Mammal,FlyableMixIn): # 多重继承
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# MixIn
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
#
# Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或
# 多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。




































