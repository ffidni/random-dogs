from PyQt5.QtWidgets import QPushButton, QLabel, QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from sys import exit, argv
from requests import get
from urllib.request import urlopen

class RandomDog(QWidget):

	def __init__(self):
		super().__init__()
		self.images = []
		self.index = 0
		self.init_ui()

	def init_ui(self):
		self.setWindowTitle("Random Dog Images")
		self.resize(937, 684)
		self.get_image()
		self.widget_manage()
		self.setup_stylesheet()
		self.layout_manage()

	def widget_manage(self):
		self.image = QPixmap()
		self.label = QLabel()
		self.prev_btn = QPushButton("Previous", clicked=self.prev)
		self.next_btn = QPushButton("Next", clicked=self.next)

		self.apply_image()
		self.label.setPixmap(self.image)
		self.prev_btn.setFixedSize(115, 38)
		self.prev_btn.setFont(QFont("MS Shell Dlg", 12))
		self.next_btn.setFixedSize(115, 38)
		self.next_btn.setFont(QFont("MS Shell Dlg", 12))

	def setup_stylesheet(self):
		self.setObjectName("Main")
		self.setStyleSheet("""#Main{
								background: #f7f1e3;
							  }
							  QPushButton{
							  	background: #f7f5ee;
							  	border: 1px solid gray;
							  }
							  QPushButton:hover{
							  	background: #e5e4e0;
							  	border: 1px solid gray;
							  }""")

	def layout_manage(self):
		ver_layout = QVBoxLayout()
		hor_layout = QHBoxLayout()

		ver_layout.addSpacing(45)
		ver_layout.addWidget(self.label, alignment=Qt.AlignCenter)
		hor_layout.addWidget(self.prev_btn, alignment=Qt.AlignRight)
		hor_layout.addSpacing(40)
		hor_layout.addWidget(self.next_btn, alignment=Qt.AlignLeft)
		ver_layout.addLayout(hor_layout)
		ver_layout.addSpacing(30)
		self.setLayout(ver_layout)

	def next(self):
		self.index += 1
		self.get_image()
		self.apply_image()

	def apply_image(self):
		self.image.loadFromData(urlopen(self.images[self.index]).read())
		self.image = self.image.scaled(500, 500, transformMode=Qt.SmoothTransformation)
		self.label.setPixmap(self.image)

	def prev(self):
		if self.index-1 >= 0:
			self.index -= 1
			self.apply_image()

	def get_image(self):
		response = get("https://dog.ceo/api/breeds/image/random")
		image_data = response.json()["message"]
		self.images.append(image_data)

if __name__ == '__main__':
	app = QApplication(argv)
	win = RandomDog()
	win.show()
	exit(app.exec_())
