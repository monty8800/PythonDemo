import os

# 使用name获取操作系统类型
print(os.name) # posix - 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

# 使用uname()获取系统详细信息 - 注意uname()函数在Windows上不提供
print(os.uname()) # posix.uname_result(sysname='Darwin', nodename='wumengdeMacBook-Pro.local', release='17.6.0', version='Darwin Kernel Version 17.6.0: Tue May  8 15:22:16 PDT 2018; root:xnu-4570.61.1~1/RELEASE_X86_64', machine='x86_64')

# 1.环境变量
print(os.environ) # 获取系统环境变量
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('GRADLE_HOME')) # /Users/monty/gradle-4.1 - 获取gradle环境变量的值

# 2.操作文件和目录
# 2.1 使用path
print(os.path.abspath('.')) # /Users/monty/PycharmProjects/PythonDemo - 查看当前目录的绝对路径
path = os.path.join('./demo/','monty') # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(path)
# os.mkdir(path) # 创建一个目录

# os.rmdir(path) # 删除一个目录

# 2.2 拆分路径
print(os.path.split('./demo/files/test.txt')) # ('./demo/files', 'test.txt')
print(os.path.splitext('./demo/files/test.txt')) # ('./demo/files/test', '.txt') - os.path.splitext()可以直接让你得到文件扩展名

# 3.文件重命名与删除

# os.rename('./demo/files/test.txt','./demo/files/demo.txt') # 重命名文件
# os.remove('./demo/files/demo.txt') # 删除文件

# 4.shutil模块
import shutil
# shutil.copyfile('./demo/user.png','./demo/files/usr.png') # 复制文件
print([x for x in os.listdir('.') if os.path.isdir(x)]) # ['demo', '.git', '.idea'] - 列出当前目录下所有目录
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']) # 列出当前目录下所有'.py'文件




