from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys 
app = QApplication(sys.argv) 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        label = QLabel(self)
        pixmap = QPixmap('background_image.jpeg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())

        label2 = QLabel(self)
        pixmap2 = QPixmap()
        label2.setPixmap()
        self.resize(pixmap2.width(),pixmap.height())

window = Window()

window.show()
sys.exit(app.exec())