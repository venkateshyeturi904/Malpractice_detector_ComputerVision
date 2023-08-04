from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *
# import StudentRegistrationPage

import cv2
import time
import sys 
import os

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
                    latest_image = convertToQtFormat.scaled(640,360,Qt.KeepAspectRatio)
                    self.changePixmap.emit(latest_image)

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


        

        self.image_count_label = QLabel(self)
        self.image_count_label.move(int(w * 0.17), int(h * 0.46))
        self.image_count_label.setFont(QFont("", int(w * h * 0.0000062692)))
        self.image_count_label.setStyleSheet("color: white")

        self.latest_image = None
       
        self.create_widgets()

        self.show()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.latest_image = image
        self.label.setPixmap(QPixmap.fromImage(image))

    def create_widgets(self):
        

        self.name_label = QLabel("Name",self)
        self.name_label.setFont(QFont("Times New Roman",int(w*h*0.00000819830)))
        self.name_label.setStyleSheet("color:white")
        self.name_label.move(int(w*0.17),int(h*0.2842))

        self.rollnumber_label = QLabel("Roll Number",self)
        self.rollnumber_label.move(int(w*0.17),int(h*0.3768))
        self.rollnumber_label.setFont(QFont("Times New Roman",int(w*h*0.00000819830)))
        self.rollnumber_label.setStyleSheet("color:white")

        self.name_textbox = QLineEdit(self)
        self.name_textbox.setFont(QFont("",int(w*h*0.0000062692)))
        self.name_textbox.move(int(w*0.17),int(h*0.3240))
        self.name_textbox.resize(int(w*0.2760),int(h*0.04166))
        self.name_textbox.textChanged.connect(self.on_text_changed)

        self.rollnumber_textbox = QLineEdit(self)
        self.rollnumber_textbox.setFont(QFont("",int(w*h*0.0000062692)))
        self.rollnumber_textbox.move(int(w*0.17),int(h*0.4166))
        self.rollnumber_textbox.resize(int(w*0.2760),int(h*0.04166))
        self.rollnumber_textbox.textChanged.connect(self.on_text_changed)

        btn1 = QPushButton("Capture",self)
        btn1.setGeometry(int(w*0.677),int(h*0.6481),int(w*0.11979),int(h*0.0416))
        self.label = QLabel(self)
        self.label.resize(400,300)
        self.label.move(1200,200)
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()
        self.show()
        btn1.clicked.connect(self.saveImage)


    def on_text_changed(self,text):
        entered_text = self.name_textbox.text()

    def saveImage(self):
        if self.latest_image is None : 
            print("There is no image to save")
            return
        
        if not os.path.exists("saved_images"):
            os.makedirs("saved_images")
        
        # update the count label 

        self.rollnumber = self.rollnumber_textbox.text()
        self.name = self.name_textbox.text()
        
        student_folder_name = os.path.join("saved_images",str(self.name))



        if not os.path.exists(student_folder_name):
            os.makedirs(student_folder_name)

        count = len(os.listdir(student_folder_name))
        self.image_count_label.setText(f"Images saved: {count}")

        image_name = os.path.join(student_folder_name,"{}.jpg".format(count+1))

        self.latest_image.save(image_name)
        print("Current image saved as : ",image_name)


    # def show_captured_images(self):
    #     self.label5 = QLabel("printing random",self)
    #     self.label5.setStyleSheet("color : white")
    #     self.label5.move(700,100)
    #     self.label5.setFont(QFont("",22))
    #     self.show()
        # self.label5 = QLabel("printing random",self)
        # self.label5.resize(400,300)
        # self.label5.move(10,10)
        # self.label5.show()
        # print("before calling",p)
        # self.label5.setPixmap(QPixmap.fromImage(p))
        # self.show()
        # print("method called")
        # self.label5.move(500,800)
        # # self.label5.setPixmap()
        # print("entered show cap method",changePixmap)
        # self.label5.setPixmap(QPixmap(changePixmap))
        # print("changes pixmap",changePixmap)
        # self.show()

        



window3= Window3()
window3.setGeometry(0,30,w,h)
# window3.setWindowState(Qt.WindowFullScreen)
# window3.setWindowFlags(window3.windowFlags() | Qt.WindowCloseButtonHint)
# window3.move(0,100)
window3.show()
# cap.release()
# cv2.destoryAllWindows()
sys.exit(app.exec())

