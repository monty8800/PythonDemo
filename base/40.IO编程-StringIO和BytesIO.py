# 1.StringIO
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
# 1.1 写入StringIO
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue()) # hello world! - getvalue()方法用于获得写入后的str。

# 1.2 读取StringIO
f = StringIO('Hello world!\nMonty wu')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# 2.BytesIO
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
# 2.1 写入BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue()) # b'\xe4\xb8\xad\xe6\x96\x87'
f.close()

# 2.2 读取BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read()) # b'\xe4\xb8\xad\xe6\x96\x87'