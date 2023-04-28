import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from email_sender import send_email
from internet_connectivity import connect_internet
import db

import pandas as pd
import ctypes   

app = QApplication(sys.argv) 
# screen = app.primaryScreen()
# screen=screen.size()
# w=screen.width()
# h=screen.height()
import ctypes
user32 = ctypes.windll.user32
w = user32.GetSystemMetrics(0)
h = user32.GetSystemMetrics(1)
print(w,h)
email_id = ""
#df = pd.read_csv("sampleDB.csv")
df = db.data

class Window_loginPage(QWidget):
    def __init__(self):
        super().__init__()
        

        self.setFixedWidth(w)
        self.setFixedHeight(h)
        self.setWindowTitle('IITG')
        
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
        self.check_connectivity()
        self.create_widgets()

    def check_connectivity(self):
        if(connect_internet()==False):
            self.label_net = QLabel("No Internet connection",self)
            self.label_net.move(0,0)
            self.label_net.setGeometry(0,0,w,int(h*0.0316))
            self.label_net.setFont(QFont("Times New Roman",int(w*h*0.00000819830)))
            self.label_net.setStyleSheet("background-color: red;color:white")
            self.label_net.setAlignment(Qt.AlignCenter)

    def change_StudentRegistrationPage(self):
         self.cams = Window_StudentRegistrationPage() 
         self.cams.show()
         self.close()

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

        btn3 = QPushButton("New User",self)
        btn3.setGeometry(int(w*0.75),int(h*0.50925),int(w*0.11979),int(h*0.0416))
        btn3.clicked.connect(lambda: self.change_StudentRegistrationPage())

        # label7.setText(linkTemplate.format('https://Google.com','New User'))
        # label7.setFont(QFont("",int(w*h*0.0000081983)))
        # label7.setGeometry(int(w*0.75),int(h*0.50925),int(w*0.09375),int(h*0.0444))  
        # label7.setStyleSheet("color:white")

        label8 = LinkLabel(self)
        label8.setText(linkTemplate.format('https://Google.com','Help'))
        label8.setFont(QFont("",int(w*h*0.0000081983)))
        label8.setGeometry(int(w*0.7734375),int(h*0.555555),int(w*0.09375),int(h*0.0444))  
        #label8.setStyleSheet("color:white")

class Window_StudentRegistrationPage(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setFixedWidth(w)
        self.setFixedHeight(h)
        self.setWindowTitle('IITG')



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
        self.check_connectivity()
        self.create_widgets()
    
    def check_connectivity(self):
        if(connect_internet()==False):
            self.label_net = QLabel("No Internet connection",self)
            self.label_net.move(0,0)
            self.label_net.setGeometry(0,0,w,int(h*0.0316))
            self.label_net.setFont(QFont("Times New Roman",int(w*h*0.00000819830)))
            self.label_net.setStyleSheet("background-color: red;color:white")
            self.label_net.setAlignment(Qt.AlignCenter)

    def sending_mail(self) :
          email_id = self.textbox1.text()
          password = ""
          for i in range(1,len(df)):
            x = df[i]
            print(x)
            if x['Outlook Id'] == email_id:
                password = x['Password']
                break    
          send_email(recipient= email_id, email= password )
          ctypes.windll.user32.MessageBoxW(0, "Mail sent on your email-id. Please check spam/junk folder too!", "Action completed", 1)
          self.textbox1.setText(email_id)


    def change_password(self):
        val1= self.textbox3.text()
        val2 = self.textbox4.text()
        val3 = self.textbox2.text()
        email_id = self.textbox1.text()
        for i in range(1,len(df)):
            x = df[i]
            if x['Outlook Id'] == email_id:
                if val1 == x['Password']:
                    if val2 == val3:
                        #df.loc[i,'Password'] = val2
                        #df.to_csv("sampleDB.csv", index=False)
                        db.sheet.update_cell(x['Candidate Id']+1,6,val2)
                        break
                    else:
                        #password doesn't match 
                        ctypes.windll.user32.MessageBoxW(0, "Confirm Password and New password is different", "Error", 1)
                        self.textbox4.setText("")
                        self.textbox2.setText("")
                        
                        break
                else:
                    #old password is incorrect
                    ctypes.windll.user32.MessageBoxW(0, "Old Password is Incorrect", "Error", 1)
                    self.textbox4.setText("")
                    self.textbox2.setText("")
                    self.textbox3.setText("")

                    break

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
        self.btn1.clicked.connect(lambda: self.sending_mail())
        #self.btn1.clicked.connect(lambda: print(self.textbox1.text()))
    
        self.label4 = QLabel("Old Password",self)
        self.label4.move(int(w*0.5208),int(h*0.3768))
        self.label4.setFont(QFont("Times New Roman",int(w*h*0.00000819830)))
        self.label4.setStyleSheet("color:white")
     
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(int(w*0.5208),int(h*0.423240))
        self.textbox3.resize(int(w*0.2760),int(h*0.035166))
        self.textbox3.setFont(QFont("",int(w*h*0.0000062692)))

        self.label2 = QLabel("New Password",self)
        self.label2.move(int(w*0.5208),int(h*0.468842))
        self.label2.setFont(QFont("Times New Roman",int(w*h*0.00000819830)))
        self.label2.setStyleSheet("color:white")

        self.textbox4 = QLineEdit(self)
        
        self.textbox4.move(int(w*0.5208),int(h*0.503240))
        self.textbox4.resize(int(w*0.2760),int(h*0.035166))
        self.textbox4.setFont(QFont("",int(w*h*0.0000062692)))

        self.label3 = QLabel("Confirm New Password",self)
        self.label3.move(int(w*0.5208),int(h*0.548842))
        self.label3.setFont(QFont("Times New Roman",int(w*h*0.00000819830)))
        self.label3.setStyleSheet("color:white")

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(int(w*0.5208),int(h*0.583240))
        self.textbox2.resize(int(w*0.2760),int(h*0.035166))
        self.textbox2.setFont(QFont("",int(w*h*0.0000062692)))
        
        self.btn2 = QPushButton("Proceed to Face registration",self)
        self.btn2.setGeometry(int(w*0.583),int(h*0.64),int(w*0.14979),int(h*0.0416))
        self.btn2.clicked.connect(lambda: self.change_password())


class LinkLabel(QLabel):
    def __init__(self,parent=None):
        super().__init__()
        self.setOpenExternalLinks(True)
        self.setParent(parent)     
        color_effect = QGraphicsColorizeEffect()
        #color_effect.setColor(white)

window = Window_loginPage()
# window.setGeometry(0,0,2000,1000)
window.show()
sys.exit(app.exec())