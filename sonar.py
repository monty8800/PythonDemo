__author__ = 'mwu'
import os
def printMenu():
    sonar_o = ['启动sonar', '停止sonar', '重启sonar']
    print('欢迎使用Sonar静态代码扫描服务')

    i = 1
    for s in sonar_o:
        print(i, s)
        i = i + 1

    menu = int(input("请输入操作:"))
    if menu in range(1, 4):
        execCmd(menu)
        return
    else:
        printMenu()

def execCmd(op):
    sonar_cmd = '/usr/local/sonarqube-6.7.4/bin/macosx-universal-64/./sonar.sh '

    if op == 1:
        os.system(sonar_cmd + 'start')
    elif op == 2:
        os.system(sonar_cmd + 'stop')
    elif op == 3:
        os.system(sonar_cmd + 'restart')

    re = input('是否需要继续操作？y(继续操作) n(任意键退出)')
    if re == 'y':
        printMenu()
    else:
        exit()


printMenu()