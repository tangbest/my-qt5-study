'''
应用图标
'''
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

class AppIcon(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		# 窗口在屏幕上显示，并设置了它的尺寸。resize()和remove()合而为一的方法
		# 前两个参数定位了窗口的x轴和y轴位置。第三个参数是定义窗口的宽度，
		# 第四个参数是定义窗口的高度
		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle("Icon")
		# 创建一个QIcon对象并接收一个我们要显示的图片路径作为参数
		self.setWindowIcon(QIcon("Resource/icon.PNG"))
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	pWindow = AppIcon()
	sys.exit(app.exec_())

