# 装饰器
import datetime


def now():
    print(datetime.datetime.now())


f = now  # 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
print(now.__name__)  # now
print(f.__name__)  # now


# 在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args,**kwargs)
    return wrapper

# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。

@log
def now():
    print(datetime.datetime.now())

now() # call now(): 2018-07-25 10:54:11.131810

now = log(now)
now()