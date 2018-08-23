# import tkinter as tk
#
# root = tk.Tk()
# root.title('eleme')
# root.minsize(400,400)
# root.maxsize(400,400)
#
#
# root.text
#
# tk.Label()
# root.mainloop()

import sys
# from PyQt5.QtWidgets import QApplication,QWidget,QToolTip
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setToolTip('this is a <b>QWidget</b> widget') # 给整个窗体设置tip
        btn = QPushButton('Button',self)
        btn.setToolTip('This is a <b>QPushButton</b> widget') # 给button设置tip
        btn.resize(btn.sizeHint()) # 改变按钮大小，并使用推荐大小
        btn.move(50,50)

        qbtn = QPushButton('Quit',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit) # 设置qbtn按钮点击后关闭程序
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 80)

        l_cookie = QLabel('Cookie',self)
        l_cookie.move(20, 20)

        e_cookie = QTextEdit('cookie',self)
        e_cookie.move(50, 20)

        self.setGeometry(300, 300, 300,
                         200)  # setGeometry()做了两件事：将窗口在屏幕上显示，并设置了它的尺寸。setGeometry()方法的前两个参数定位了窗口的x轴和y轴位置。第三个参数是定义窗口的宽度，第四个参数是定义窗口的高度。
        self.setWindowIcon(QIcon('usr.png'))  # 设置窗口图标，在mac上貌似没什么用
        self.center()
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self,'Message','是否要退出？',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry() # 获得主窗口的一个矩形特定几何图形
        cp = QDesktopWidget().availableGeometry().center() # 桌面居中信息，算出相对于显示器的绝对值。并且从这个绝对值中，我们获得了屏幕中心点。
        qr.moveCenter(cp) # 矩形已经设置好了它的宽和高。现在我们把矩形的中心设置到屏幕的中间去。矩形的大小并不会改变。
        self.move(qr.topLeft()) # 移动了应用窗口的左上方的点到qr矩形的左上方的点，因此居中显示在我们的屏幕上。


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())


