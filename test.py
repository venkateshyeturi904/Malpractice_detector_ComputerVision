from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys 
app = QApplication(sys.argv) 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        #self.setFixedWidth(1200)
        #self.setFixedHeight(1200)
        size = self.size()
        pixmap = QPixmap('background_image.jpeg')
        pixmap4 = pixmap.scaled(size.width(), size.height())
        label = QLabel(self)
        label.resize(size.width(), size.height())
        label.setPixmap(pixmap4)

window = Window()

window.show()
sys.exit(app.exec())