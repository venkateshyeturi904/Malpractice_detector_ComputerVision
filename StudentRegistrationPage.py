from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import Qt
from email_sender import send_email
import sys 
import pandas as pd
app = QApplication(sys.argv) 
screen = app.primaryScreen()
screen=screen.size()
w=screen.width()
h=screen.height()
print(w,h)

class Window2(QWidget):
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

        

        self.label = QLabel("Candidate Registraion Page",self)
        self.label.move(int(w*0.3796),int(h*0.055))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Pacifico",int(w*h*0.000010)))
        self.label.setStyleSheet("color : white")
        

        # self.label4 = QLabel("Welcome to Exam Proctoring System, IIT Guwahati",self)
        # self.label4.setStyleSheet("color : white")
        # self.label4.move(int(w*0.3109),int(h*0.1296))
        # self.label4.setFont(QFont("",int(w*h*0.000007716)))
        # # self.label4.setAlignment(Qt.AlignCenter)

        # self.label5 = QLabel("Please enter your credentials and click on relevant login button",self)
        # self.label5.setStyleSheet("color : white")
        # self.label5.move(int(w*0.27083),int(h*0.1620))
        # self.label5.setFont(QFont("",int(w*h*0.000007716)))
        
        
        # self.textbox2 = QLineEdit(self)
        # self.textbox2.setFont(QFont("",int(w*h*0.0000062692)))
        
        # self.textbox2.move(int(w*0.5208),int(h*0.4166))
        
        # self.textbox2.resize(int(w*0.2760),int(h*0.04166))

        self.label2 = QLabel("Enter your Email Id (Eg : abc@iitg.ac.in)",self)
        self.label2.move(int(w*0.5208),int(h*0.2685))
        self.label2.setFont(QFont("Times New Roman",int(w*h*0.00000819830)))
        self.label2.setStyleSheet("color:white")

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(int(w*0.5208),int(h*0.30))
        self.textbox1.resize(int(w*0.2760),int(h*0.04166))
        self.textbox1.setFont(QFont("",int(w*h*0.0000062692)))

        self.btn1 = QPushButton("Proceed",self)
        self.btn1.setGeometry(int(w*0.83),int(h*0.3240),int(w*0.08979),int(h*0.0416))
        self.btn1.clicked.connect(lambda : send_email(recipient= "<" + self.textbox1.text() + ">", email= "Hello" ))
        
        #recipient=self.textbox1.text()
        # self.label3 = QLabel("Password",self)
        # self.label3.move(int(w*0.5208),int(h*0.3768))
        # self.label3.setFont(QFont("Times New Roman",int(w*h*0.00000819830)))
        # self.label3.setStyleSheet("color:white")

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(int(w*0.5208),int(h*0.423240))
        self.textbox1.resize(int(w*0.2760),int(h*0.035166))
        self.textbox1.setFont(QFont("",int(w*h*0.0000062692)))

        self.label2 = QLabel("New Password",self)
        self.label2.move(int(w*0.5208),int(h*0.468842))
        self.label2.setFont(QFont("Times New Roman",int(w*h*0.00000819830)))
        self.label2.setStyleSheet("color:white")

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(int(w*0.5208),int(h*0.503240))
        self.textbox1.resize(int(w*0.2760),int(h*0.035166))
        self.textbox1.setFont(QFont("",int(w*h*0.0000062692)))

        self.label2 = QLabel("Confirm New Password",self)
        self.label2.move(int(w*0.5208),int(h*0.548842))
        self.label2.setFont(QFont("Times New Roman",int(w*h*0.00000819830)))
        self.label2.setStyleSheet("color:white")

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(int(w*0.5208),int(h*0.583240))
        self.textbox1.resize(int(w*0.2760),int(h*0.035166))
        self.textbox1.setFont(QFont("",int(w*h*0.0000062692)))

        btn1 = QPushButton("Proceed to Face registration",self)
        btn1.setGeometry(int(w*0.583),int(h*0.64),int(w*0.14979),int(h*0.0416))


class LinkLabel(QLabel):
    def __init__(self,parent=None):
        super().__init__()
        self.setOpenExternalLinks(True)
        self.setParent(parent)     
        color_effect = QGraphicsColorizeEffect()
        #color_effect.setColor(white)

# window = Window2()
# window.setGeometry(0,0,2000,1000)
# window.show()
# df = pd.read_csv('sampleDB.csv')
# print(df['Password'][1])
# sys.exit(app.exec())