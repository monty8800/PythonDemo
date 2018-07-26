# 1.序列化 - pickling ，使用pickle模块来实现
import pickle

d = dict(name='mwu', age=10, score=88)
print(pickle.dumps(d))  # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。

# 1.1序列化
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
# f = open('./demo/files/dump.txt','wb')
# pickle.dump(d,f)
# f.close()

# 1.2反序列化
f = open('./demo/files/dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)  # {'name': 'mwu', 'age': 10, 'score': 88}

# 2.Json
import json

# 2.1序列化
du = json.dumps(d)
print(du)  # {"name": "mwu", "age": 10, "score": 88}
# with open('./demo/files/jsondump.json','w') as f:
#     json.dump(d,f) # 将json写入文件

# 2.2反序列化
d = json.loads(du)
print(d)  # {'name': 'mwu', 'age': 10, 'score': 88}
# 从文件反序列化
with open('./demo/files/jsondump.json', 'r') as f:
    j = json.load(f)
print(j)  # {'name': 'mwu', 'age': 10, 'score': 88}


# 3.JSON进阶 类序列化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('mwu', 12, 100)


# print(json.dumps(s)) # TypeError: Object of type Student is not JSON serializable
# 错误的原因是Student对象不是一个可序列化为JSON的对象。
# 如果连class的实例对象都无法序列化为JSON，这肯定不合理！

# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


print(json.dumps(s, default=student2dict))  # {"name": "mwu", "age": 12, "score": 100}
# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：

# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s, default=lambda obj: obj.__dict__))  # {"name": "mwu", "age": 12, "score": 100}


# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。

# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))  # <__main__.Student object at 0x10e0a1978>
