from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
<<<<<<< Updated upstream
from PyQt5 import QtCore
=======
from PyQt5.QtCore import *
>>>>>>> Stashed changes
import sys 
app = QApplication(sys.argv) 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        #self.setFixedWidth(1200)
        #self.setFixedHeight(1200)
        size = self.size()
        pixmap = QPixmap('background_image.jpeg')
<<<<<<< Updated upstream
        pixmap4 = pixmap.scaled(size.width(), size.height())
        label = QLabel(self)
        label.resize(size.width(), size.height())
        label.setPixmap(pixmap4)
=======
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        # self.setGeometry(0,0,8000,4000)

        label2 = QLabel(self)
        pixmap2 = QPixmap('side_image.jpg')
        label2.setPixmap(pixmap2)
        self.resize(pixmap2.width(),pixmap2.height())
        label2.setGeometry(160,200,pixmap2.width(),pixmap2.height())
        
        self.create_widgets()
>>>>>>> Stashed changes

        

    def create_widgets(self):

        btn1 = QPushButton("Student login",self)
        btn1.setGeometry(650,500,230,40)
        btn2 = QPushButton("Admin Login",self)
        btn2.setGeometry(900,500,230,40)

        self.label = QLabel("Exam proctoring system, IIT Guwahati",self)
        self.label.move(200,60)
        self.label.setFont(QFont("Algerian",25))
        self.label.setStyleSheet("color : white")
        

        self.label4 = QLabel("Welcome to Exam Proctoring System, IIT Guwahati",self)
        self.label4.setStyleSheet("color : white")
        self.label4.move(390,120)
        self.label4.setFont(QFont("",16))
        # self.label4.setAlignment(Qt.AlignCenter)

        self.label5 = QLabel("Please enter your credentials and click on relevant login button",self)
        self.label5.setStyleSheet("color : white")
        self.label5.move(360,145)
        self.label5.setFont(QFont("",16))
        
        self.textbox1 = QLineEdit(self)
        self.textbox1.setTextMargins(1,1,1,30)
        self.textbox2 = QLineEdit(self)
        self.textbox1.move(650,250)
        self.textbox2.move(650,350)
        self.textbox1.resize(480,40)
        self.textbox2.resize(480,40)

        self.label2 = QLabel("UserName",self)
        self.label2.move(650,217)
        self.label2.setFont(QFont("Times New Roman",17))
        self.label2.setStyleSheet("color:white")

        self.label3 = QLabel("Password",self)
        self.label3.move(650,317)
        self.label3.setFont(QFont("Times New Roman",17))
        self.label3.setStyleSheet("color:white")
        

window = Window()
# window.setGeometry(0,0,2000,1000)
window.show()
sys.exit(app.exec())