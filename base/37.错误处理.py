# 1.try
# 1.1简单使用
def div(d):
    try:
        print('try...')
        r = 10/d
        print('result',r)
    except ZeroDivisionError as e:
        print('except',e)
    finally:
        print('finally...')

# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，
# 即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。

div(0) # division by zero

div(2) # result 5.0

# 1.2使用多个except捕获异常
def div(d):
    try:
        print('try...')
        r = 10/d
        print('result',r)
    except TypeError as e:
        print('TypeError',e)
    except ValueError as e:
        print('ValueError',e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError',e)
    finally:
        print('finally...')

div('3') # TypeError unsupported operand type(s) for /: 'int' and 'str'

# 1.3 使用else
def div(d):
    try:
        print('try...')
        r = 10/d
        print('result',r)
    except TypeError as e:
        print('TypeError',e)
    except ValueError as e:
        print('ValueError',e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError',e)
    else: # 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
        print('no error!')
    finally:
        print('finally...')

div(3) # no error!

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main() # Error: division by zero

# 2.调用栈
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看err.py：
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

# main() # 未捕获异常，逐级往上抛

# 3.记录错误
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

# main() # ERROR:root:division by zero

# 4.抛出错误
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

# foo('0') # __main__.FooError: invalid value: 0

# 5.常见的处理
# 在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？
# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，
# 最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，
# 最终会抛给CEO去处理。
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

# bar()

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型
# try:
#     10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error!')
# 只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。

# 测试：运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
from functools import reduce

def str2num(s):
    try:
        return int(s)
    except ValueError as e:
        logging.exception(e)
        return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()