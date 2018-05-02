'''
应用图标
'''
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QToolTip

class AppMainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.initSize()
		self.initIcon()
		self.initTip()
		self.initStatusBar()
		self.initMenuBar()
		self.initToolBar()
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

	def initTip(self):
		# 提示
		QToolTip.setFont(QFont('SansSerif', 10))  # 这个静态方法设置了用于提示框的字体
		self.setToolTip('This is a <b> QWidget</b> widget')
		pBtn = QPushButton('Quit', self)
		pBtn.setToolTip('This is a button')
		pBtn.resize(pBtn.sizeHint())
		pBtn.move(200,200)
		'''
		在PyQt5中，事件处理系统由信号&槽机制建立。如果我们点击了按钮，信号clicked被发送。
		槽可以是Qt内置的槽或Python 的一个方法调用。QCoreApplication类包含了主事件循环；
		它处理和转发所有事件。instance()方法给我们返回一个实例化对象。
		注意QCoreAppli类由QApplication创建。点击信号连接到quit()方法，将结束应用。
		事件通信在两个对象之间进行：发送者和接受者。发送者是按钮，接受者是应用对象
		'''
		pBtn.clicked.connect(QCoreApplication.instance().quit)

	def initStatusBar(self):
		# 状态栏
		self.statusBar().showMessage('Ready')

	def initMenuBar(self):
		# 菜单栏
		pActionExit = QAction(QIcon('F:\pythonproject\my-qt5-study\Resource\icon.PNG'), '&Exit', self)
		pActionExit.setShortcut('Ctrl+Q')
		pActionExit.setStatusTip('Exit!')
		pActionExit.triggered.connect(qApp.quit)

		menuBar = self.menuBar()
		fileMenu = menuBar.addMenu('&File')
		fileMenu.addAction(pActionExit)

	def initToolBar(self):
		pActionExit = QAction(QIcon('F:\pythonproject\my-qt5-study\Resource\icon.PNG'), '&Exit', self)
		pActionExit.setShortcut('Ctrl+Q')
		pActionExit.setStatusTip('Exit!')
		pActionExit.triggered.connect(qApp.quit)

		self.toolBar = self.addToolBar('Exit')
		self.toolBar.addAction(pActionExit)

		self.toolBar2 = self.addToolBar('Exit')
		self.toolBar2.addAction(pActionExit)

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

