# 继承和多态

class Animal(object):
    def run(self):
        print('Animal is running...')


Animal().run() # Animal is running...

# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
class Dog(Animal): # Dog类继承Animal
    def run(self): # 子类重写父类方法
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running')


Dog().run() # Dog is running...

Cat().run() # Cat is running...

# 要理解什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

# 判断一个变量是否是某个类型
print(isinstance(a,list)) # True
print(isinstance(b,Animal)) # True
print(isinstance(c,Dog)) # True

print(isinstance(c,Animal)) # True - 因为Dog是继承Animal的，所有c既是Doc也是Animal


def run_twice(animal):
    animal.run()

run_twice(Animal()) # Animal is running...
run_twice(Dog()) # Dog is running...
run_twice(Cat()) # Cat is running...

# 新增一个Animal的子类
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise()) # Tortoise is running slowly...

# 新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。

# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，
# 然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的
# run()方法，这就是多态的意思：
#
# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在
# Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种
# Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
#
# 对扩展开放：允许新增Animal子类；
#
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。


# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
class Timer(object):
    def run(self):
        print('Start...')

run_twice(Timer()) # Start...


