from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import Qt
import StudentRegistrationPage
import sys 
app = QApplication(sys.argv) 
screen = app.primaryScreen()
screen=screen.size()
w=screen.width()
h=screen.height()
print(w,h)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        #self.setFixedWidth(w)
        #self.setFixedHeight(h)
        pixmap = QPixmap('background_image.jpeg')
        pixmap4 = pixmap.scaled(w,h)
        label = QLabel(self)
        label.resize(w, h)
        label.setPixmap(pixmap4)

        label2 = QLabel(self)
        pixmap21 = QPixmap('side_image.jpg')
        #print('Size: %d x %d' % (w*h*0.0001234569, h))
        pixmap2 = pixmap21.scaled(int(w*0.30),int(h*0.425))
        label2.setPixmap(pixmap2)
        self.resize(pixmap2.width(),pixmap2.height())
        label2.setGeometry(int(w*0.15625),int(h*0.2685),pixmap2.width(),pixmap2.height())
        self.create_widgets()
        

    def create_widgets(self):

        btn1 = QPushButton("Student login",self)
        btn1.setGeometry(int(w*0.677),int(h*0.6481),int(w*0.11979),int(h*0.0416))
        btn2 = QPushButton("Admin Login",self)
        btn2.setGeometry(1000,700,int(w*0.11979),int(h*0.0416))

        self.label = QLabel("Exam proctoring system, IIT Guwahati",self)
        self.label.move(int(w*0.2796),int(h*0.055))
        self.label.setFont(QFont("Algerian",int(w*h*0.0000120)))
        self.label.setStyleSheet("color : white")
        

        self.label4 = QLabel("Welcome to Exam Proctoring System, IIT Guwahati",self)
        self.label4.setStyleSheet("color : white")
        self.label4.move(int(w*0.3109),int(h*0.1296))
        self.label4.setFont(QFont("",int(w*h*0.000007716)))
        # self.label4.setAlignment(Qt.AlignCenter)

        self.label5 = QLabel("Please enter your credentials and click on relevant login button",self)
        self.label5.setStyleSheet("color : white")
        self.label5.move(int(w*0.27083),int(h*0.1620))
        self.label5.setFont(QFont("",int(w*h*0.000007716)))
        
        self.textbox1 = QLineEdit(self)
        #self.textbox1.setTextMargins(1,1,1,30)
        self.textbox1.setFont(QFont("",int(w*h*0.0000062692)))
        self.textbox2 = QLineEdit(self)
        self.textbox2.setFont(QFont("",int(w*h*0.0000062692)))
        self.textbox1.move(int(w*0.5208),int(h*0.3240))
        self.textbox2.move(int(w*0.5208),int(h*0.4166))
        self.textbox1.resize(int(w*0.2760),int(h*0.04166))
        self.textbox2.resize(int(w*0.2760),int(h*0.04166))

        self.label2 = QLabel("UserName",self)
        self.label2.move(int(w*0.5208),int(h*0.2842))
        self.label2.setFont(QFont("Times New Roman",int(w*h*0.00000819830)))
        self.label2.setStyleSheet("color:white")

        self.label3 = QLabel("Password",self)
        self.label3.move(int(w*0.5208),int(h*0.3768))
        self.label3.setFont(QFont("Times New Roman",int(w*h*0.00000819830)))
        self.label3.setStyleSheet("color:white")

        
        label7 = LinkLabel(self)
        linkTemplate = '<a href={0}>{1}</a>'

        btn3 = QPushButton("Proceed",self)
        btn3.setGeometry(int(w*0.75),int(h*0.50925),int(w*0.11979),int(h*0.0416))
        btn3.clicked.connect(self.callRPage)

        # label7.setText(linkTemplate.format('https://Google.com','New User'))
        # label7.setFont(QFont("",int(w*h*0.0000081983)))
        # label7.setGeometry(int(w*0.75),int(h*0.50925),int(w*0.09375),int(h*0.0444))  
        # label7.setStyleSheet("color:white")

        label8 = LinkLabel(self)
        label8.setText(linkTemplate.format('https://Google.com','Help'))
        label8.setFont(QFont("",int(w*h*0.0000081983)))
        label8.setGeometry(int(w*0.7734375),int(h*0.555555),int(w*0.09375),int(h*0.0444))  
        #label8.setStyleSheet("color:white")

    def callRPage(self):
        RPage = StudentRegistrationPage.Window2()
        # win = RPage.window2()
        RPage.show()
        window.close()



class LinkLabel(QLabel):
    def __init__(self,parent=None):
        super().__init__()
        self.setOpenExternalLinks(True)
        self.setParent(parent)     
        color_effect = QGraphicsColorizeEffect()
        #color_effect.setColor(white)

window = Window()
# window.setGeometry(0,0,2000,1000)
window.show()
sys.exit(app.exec())