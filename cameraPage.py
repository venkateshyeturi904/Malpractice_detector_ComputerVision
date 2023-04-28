from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *
# import StudentRegistrationPage

import cv2
import sys 

app = QApplication(sys.argv) 
screen = app.primaryScreen()
screen=screen.size()
w=screen.width()
h=screen.height()
print(w,h)

# cam = cv2.VideoCapture(0)

class Thread(QThread):
     changePixmap = pyqtSignal(QImage)

     def run(self):
          cap = cv2.VideoCapture(0)
          while True:
               ret, frame = cap.read()
               if ret : 
                    rgbImage = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                    h,w,ch = rgbImage.shape
                    bytesPerLine = ch*w
                    convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                    p = convertToQtFormat.scaled(640,360,Qt.KeepAspectRatio)
                    self.changePixmap.emit(p)

class Window3(QWidget):
    def __init__(self):
        super().__init__()
        
        pixmap = QPixmap('background_image.jpeg')
        pixmap4 = pixmap.scaled(w,h)
        label = QLabel(self)
        label.resize(w, h)
        label.setPixmap(pixmap4)


        self.label4 = QLabel("Face Registration",self)
        self.label4.setStyleSheet("color : white")
        self.label4.move(700,100)
        self.label4.setFont(QFont("",22))

        label2 = QLabel(self)
        # pixmap21 = QPixmap('side_image.jpg')
        #print('Size: %d x %d' % (w*h*0.0001234569, h))
        # pixmap2 = pixmap21.scaled(int(w*0.30),int(h*0.425))
        # label2.setPixmap(pixmap2)
        # self.resize(pixmap2.width(),pixmap2.height())
        # label2.setGeometry(int(w*0.15625),int(h*0.2685),pixmap2.width(),pixmap2.height())
        self.create_widgets()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))

    def create_widgets(self):
        
        btn1 = QPushButton("Capture",self)
        btn1.setGeometry(int(w*0.677),int(h*0.6481),int(w*0.11979),int(h*0.0416))
        self.label = QLabel(self)
        self.label.resize(400,300)
        self.label.move(1200,200)
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()
        self.show()


        



window3= Window3()
window3.setGeometry(0,30,w,h)
# window3.setWindowState(Qt.WindowFullScreen)
# window3.setWindowFlags(window3.windowFlags() | Qt.WindowCloseButtonHint)
# window3.move(0,100)
window3.show()
# cap.release()
# cv2.destoryAllWindows()
sys.exit(app.exec())

