'''
信号槽
'''
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QObject
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QToolTip
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

class Communicate(QObject):
	closeApp = pyqtSignal() # 信号使用了pyqtSignal()方法创建，并且成为外部类Communicate类的属性。

class AppMainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.initSize()
		self.initIcon()
		self.initContent()
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

	def initContent(self):
		pLcd = QLCDNumber()  # 显示一个LCD数字
		pSld = QSlider(Qt.Horizontal, self)  # 提供了一个水平滑动条

		pBtn1 = QPushButton("Button1")
		pBtn2 = QPushButton("Button2")

		pVbox = QVBoxLayout()
		pVbox.addWidget(pLcd)
		pVbox.addWidget(pSld)
		pVbox.addWidget(pBtn1)
		pVbox.addWidget(pBtn2)

		self.setLayout(pVbox)

		pSld.valueChanged.connect(pLcd.display)
		pBtn1.clicked.connect(self.buttonClicked)
		pBtn2.clicked.connect(self.buttonClicked)

		# 自定义信号
		self.mySignal = Communicate()
		self.mySignal.closeApp.connect(self.mySignalFunc) # 把自定义的closeApp信号连接到QMainWindow的close()槽上

	def mySignalFunc(self):
		print("触发了自定义信号")

	def buttonClicked(self):
		pSender = self.sender()
		print(pSender.text() + " was pressed!")

	def keyPressEvent(self, QKeyEvent):
		if QKeyEvent.key() == Qt.Key_Escape:
			self.close()

	def mousePressEvent(self, QMouseEvent):
		self.mySignal.closeApp.emit()  # 当我们在窗口上点击一下鼠标，closeApp信号会被发射。应用中断

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

