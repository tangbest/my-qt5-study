import sys
from PyQt5.QtWidgets import QApplication, QWidget

def showWindow():
	# 所有的PyQt5应用必须创建一个应用（Application）对象
	# sys.argv参数是一个来自命令行的参数列表
	app = QApplication(sys.argv)

	# Qwidget组件是PyQt5中所有用户界面类的基础类。我们给QWidget提供了默认的构造方法
	# 默认构造方法没有父类。没有父类的widget组件将被作为窗口使用
	pWidget = QWidget()

	# resize()方法调整了widget组件的大小。它现在是500px宽，500px高
	pWidget.resize(500, 500)

	# move()方法移动widget组件到一个位置，这个位置是屏幕上x=500,y=200的坐标
	pWidget.move(500, 100)

	# 设置了窗口的标题。这个标题显示在标题栏中
	pWidget.setWindowTitle("Title")

	# show()方法在屏幕上显示出widget。一个widget对象在这里第一次被在内存中创建，并且之后在屏幕上显示
	pWidget.show()

	# 应用进入主循环。在这个地方，事件处理开始执行。主循环用于接收来自窗口触发的事件，
	# 并且转发他们到widget应用上处理。如果我们调用exit()方法或主widget组件被销毁，主循环将退出
	sys.exit(app.exec())
	# sys.exit() 方法确保一个不留垃圾的退出。系统环境将会被通知应用是怎样被结束的


if __name__ == "__main__":
	showWindow()


