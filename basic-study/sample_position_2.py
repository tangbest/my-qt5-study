'''
网格布局
'''
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QToolTip
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class AppMainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.initSize()
		self.initIcon()
		self.initGridLayout()
		self.show()

	def initSize(self):
		# 窗口在屏幕上显示，并设置了它的尺寸。resize()和remove()合而为一的方法
		# 前两个参数定位了窗口的x轴和y轴位置。第三个参数是定义窗口的宽度,第四个参数是定义窗口的高度
		#self.setGeometry(200, 100, 800, 600)
		self.resize(800, 600)
		# center
		# 获得主窗口的一个矩形特定几何图形。这包含了窗口的框架。
		qr = self.frameGeometry()
		# 算出相对于显示器的绝对值
		cp = QDesktopWidget().availableGeometry().center()
		# 矩形已经设置好了它的宽和高。现在我们把矩形的中心设置到屏幕的中间去。
		qr.moveCenter(cp)
		# 移动应用窗口的左上方的点到qr矩形的左上方的点，因此居中显示在我们的屏幕上
		self.move(qr.topLeft())

	def initIcon(self):
		# 图标
		self.setWindowTitle("Icon")
		# 创建一个QIcon对象并接收一个我们要显示的图片路径作为参数
		self.setWindowIcon(QIcon("F:\pythonproject\my-qt5-study\Resource\icon.PNG"))

	def initGridLayout(self):
		pGridLayout = QGridLayout()
		self.setLayout(pGridLayout) # 把QGridLayout类设为应用窗口的布局
		names = ['Cls', 'Bck', '', 'Close',
		         '7', '8', '9', '/',
		         '4', '5', '6', '*',
		         '1', '2', '3', '-',
		         '0', '.', '=', '+']
		lstPosition = [(i, j) for i in range(5) for j in range(4)]
		for position, name in zip(lstPosition, names):
			if name == '':
				continue
			button = QPushButton(name)
			pGridLayout.addWidget(button, *position)


	def closeEvent(self, QCloseEvent):
		reply = QMessageBox.question(self, 'Message', 'Sure to quit?',
		                             QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			QCloseEvent.accept()
		else:
			QCloseEvent.ignore()



if __name__ == "__main__":
	app = QApplication(sys.argv)
	pWindow = AppMainWindow()
	sys.exit(app.exec_())

