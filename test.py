from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
import sys 
app = QApplication(sys.argv) 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setFixedWidth(1920)
        self.setFixedHeight(1080)
        size = self.size()
        pixmap = QPixmap('background_image.jpeg')
        pixmap4 = pixmap.scaled(size.width(), size.height())
        label = QLabel(self)
        label.resize(size.width(), size.height())
        label.setPixmap(pixmap4)

        label2 = QLabel(self)
        pixmap21 = QPixmap('side_image.jpg')
        print('Size: %d x %d' % (pixmap21.width(), pixmap21.height()))
        pixmap2 = pixmap21.scaled(579,460)
        label2.setPixmap(pixmap2)
        self.resize(pixmap2.width(),pixmap2.height())
        label2.setGeometry(300,290,pixmap2.width(),pixmap2.height())
        self.create_widgets()
        

    def create_widgets(self):

        btn1 = QPushButton("Student login",self)
        btn1.setGeometry(1300,700,230,45)
        btn2 = QPushButton("Admin Login",self)
        btn2.setGeometry(1000,700,230,45)

        self.label = QLabel("Exam proctoring system, IIT Guwahati",self)
        self.label.move(537,60)
        self.label.setFont(QFont("Algerian",25))
        self.label.setStyleSheet("color : white")
        

        self.label4 = QLabel("Welcome to Exam Proctoring System, IIT Guwahati",self)
        self.label4.setStyleSheet("color : white")
        self.label4.move(597,140)
        self.label4.setFont(QFont("",16))
        # self.label4.setAlignment(Qt.AlignCenter)

        self.label5 = QLabel("Please enter your credentials and click on relevant login button",self)
        self.label5.setStyleSheet("color : white")
        self.label5.move(520,175)
        self.label5.setFont(QFont("",16))
        
        self.textbox1 = QLineEdit(self)
        #self.textbox1.setTextMargins(1,1,1,30)
        self.textbox1.setFont(QFont("",13))
        self.textbox2 = QLineEdit(self)
        self.textbox2.setFont(QFont("",13))
        self.textbox1.move(1000,350)
        self.textbox2.move(1000,450)
        self.textbox1.resize(530,45)
        self.textbox2.resize(530,45)

        self.label2 = QLabel("UserName",self)
        self.label2.move(1000,307)
        self.label2.setFont(QFont("Times New Roman",17))
        self.label2.setStyleSheet("color:white")

        self.label3 = QLabel("Password",self)
        self.label3.move(1000,407)
        self.label3.setFont(QFont("Times New Roman",17))
        self.label3.setStyleSheet("color:white")

        
        label7 = LinkLabel(self)
        linkTemplate = '<a href={0}>{1}</a>'
        label7.setText(linkTemplate.format('https://Google.com','New User'))
        label7.setFont(QFont("",17))
        label7.setGeometry(1440,550,180,48)  
        label7.setStyleSheet("color:white")

        label8 = LinkLabel(self)
        label8.setText(linkTemplate.format('https://Google.com','Help'))
        label8.setFont(QFont("",17))
        label8.setGeometry(1485,600,180,48)  
        #label8.setStyleSheet("color:white")


class LinkLabel(QLabel):
    def __init__(self,parent=None):
        super().__init__()
        self.setOpenExternalLinks(True)
        self.setParent(parent)     
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(white)

window = Window()
# window.setGeometry(0,0,2000,1000)
window.show()
sys.exit(app.exec())