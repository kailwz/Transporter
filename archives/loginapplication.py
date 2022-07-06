from email.message import EmailMessage
from database import loadDatabase
from mainapplication import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from random import randint
from PyQt5.QtGui import *
import smtplib
import sys

class loginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # load the database #
        loadDatabase(self)

        # login frame #
        self.loginFrame()

        # loading the window #
        self.loadWindow()

    def loadWindow(self):

        # window configurations #
        self.setWindowIcon(QIcon('images/bluevioleticons/logo.png'))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet('background: #111111; border-radius: 15px;')
        self.setWindowTitle('U n p a c k - L o g i n')
        self.setMaximumSize(500, 500)
        self.setMinimumSize(350, 350)

        # centralizar a janela #
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.show()

    def loginFrame(self):

        # frame for the login #
        self.myLoginFrame = QFrame(self)
        self.myLoginFrame.setStyleSheet('background: #111111;')
        self.myLoginFrame.setGeometry(0, 0, 350, 350)

        # login frame label #
        self.loginFrameLabel()

        # login frame entrys #
        self.loginFrameEntrys()

        # login frame buttons #
        self.loginFrameButtons()
        
        self.myLoginFrame.show()

    def loginFrameLabel(self):

        # naming the page with a label #
        self.loginLabel = QLabel(self.myLoginFrame)
        self.loginLabel.setText('L O G I N')
        self.loginLabel.setAlignment(Qt.AlignCenter)
        self.loginLabel.setGeometry(70, 30, 200, 50)
        self.loginLabel.setStyleSheet(
            '''
                background: none;
                color: whitesmoke;
                font: bold 20px Dejavu, Sans, Mono;
            '''
        )
        self.loginLabel.show()

        # say to insert something in the email input #
        self.loginIsNullEmailLabel = QLabel(self.myLoginFrame)
        self.loginIsNullEmailLabel.setText('Fill in this field')
        self.loginIsNullEmailLabel.setGeometry(75, 80, 200, 15)
        self.loginIsNullEmailLabel.setAlignment(Qt.AlignCenter)
        self.loginIsNullEmailLabel.setStyleSheet(
            '''
                font: 12px Dejavu, Sans, Mono;
                color: #FF0800;
            '''
            )
        self.loginIsNullEmailLabel.hide()

        # say to inset something in the password input #
        self.loginIsNullPasswordLabel = QLabel(self.myLoginFrame)
        self.loginIsNullPasswordLabel.setText('Fill in this field')
        self.loginIsNullPasswordLabel.setGeometry(75, 150, 200, 15)
        self.loginIsNullPasswordLabel.setAlignment(Qt.AlignCenter)
        self.loginIsNullPasswordLabel.setStyleSheet(
            '''
                font: 12px Dejavu, Sans, Mono;
                color: #FF0800;
            '''
            )
        self.loginIsNullPasswordLabel.hide()

    def loginFrameEntrys(self):

        # email entry #
        self.loginEmailEntry = QLineEdit(self.myLoginFrame)
        self.loginEmailEntry.setPlaceholderText('E-mail')
        self.loginEmailEntry.setAlignment(Qt.AlignCenter)
        self.loginEmailEntry.setMaxLength(50)
        self.loginEmailEntry.setGeometry(65, 100, 220, 40)
        self.loginEmailEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0 ,0);
                color: whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.loginEmailEntry.show()

        # password entry #
        self.loginPasswordEntry = QLineEdit(self.myLoginFrame)
        self.loginPasswordEntry.setEchoMode(QLineEdit.Password)
        self.loginPasswordEntry.setPlaceholderText('Password')
        self.loginPasswordEntry.setAlignment(Qt.AlignCenter)
        self.loginPasswordEntry.setMaxLength(6)
        self.loginPasswordEntry.setGeometry(65, 170, 220, 40)
        self.loginPasswordEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0, 0);
                color:whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.loginPasswordEntry.show()

    def loginFrameButtons(self):

        # create a new account button #
        self.createButton = QPushButton(self.myLoginFrame)
        self.createButton.setText('Create a Acount!')
        self.createButton.setGeometry(30, 200, 155, 70)
        self.createButton.setStyleSheet(
            '''
                QPushButton{
                    background: none;
                    color: blueviolet;
                    font: 10px Dejavu, Sans, Mono;
                    border-radius: 7px;
                    }
                QPushButton:hover{
                    text-decoration: underline;
                }
            '''
        )
        self.createButton.clicked.connect(
            lambda: (
                self.myLoginFrame.hide(),
                self.loadCadastreFrame()
                )
            )
        self.createButton.show()

        # forgot your password button #
        self.forgotButton = QPushButton(self.myLoginFrame)
        self.forgotButton.setText('Forgot Password')
        self.forgotButton.setGeometry(165, 200, 155, 70)
        self.forgotButton.setStyleSheet(
            '''
                QPushButton{
                    background: none;
                    color: blueviolet;
                    font: 10px Dejavu, Sans, Mono;
                    border-radius: 7px;
                    }
                QPushButton:hover{
                    text-decoration: underline;
                }
            '''
        )
        self.forgotButton.clicked.connect(
            lambda: (
                self.myLoginFrame.hide(),
                self.loadForgotFrame()
                )
            )
        self.forgotButton.show()

        # and finally the login button #
        self.loginButton = QPushButton(self.myLoginFrame)
        self.loginButton.setText('S I G N I N')
        self.loginButton.setGeometry(125, 260, 100, 50)
        self.loginButton.setStyleSheet(
            '''
                QPushButton{
                    background: blueviolet;
                    border: 2px solid blueviolet;
                    color: whitesmoke;
                    font:  12px bold Dejavu, Sans, Mono;
                    border-radius: 10px;
                    }

                QPushButton:hover{
                    border: 2px solid rgb(128, 33, 216);
                    background: rgb(128, 33, 216);
                }

                QPushButton:pressed{
                    background: none;
                    border: 2px solid blueviolet;
                }
            '''
        )
        self.loginButton.clicked.connect(lambda: (self.loginInTheAccount()))
        self.loginButton.show()

    def cadastreFrame(self):

        # frame for the cadastre #
        self.myCadastreFrame = QFrame(self)
        self.myCadastreFrame.setStyleSheet('background: #111111;')
        self.myCadastreFrame.setGeometry(0, 0, 350, 350)

        # cadastre frame label #
        self.cadastreFrameLabel()

        # cadastre frame entrys #
        self.cadastreFrameEntrys()

        # cadastre frame buttons #
        self.cadastreFrameButtons()

        self.myCadastreFrame.show()

    def cadastreFrameLabel(self):

        # naming the page with a label #
        self.cadastreLabel = QLabel(self.myCadastreFrame)
        self.cadastreLabel.setText('C A D A S T R E')
        self.cadastreLabel.setGeometry(70, 10, 200, 50)
        self.cadastreLabel.setAlignment(Qt.AlignCenter)
        self.cadastreLabel.setStyleSheet(
            '''
                background: none;
                color: whitesmoke;
                font: bold 20px Dejavu, Sans, Mono;
            '''
        )
        self.cadastreLabel.show()

        # say to insert something in the name input #
        self.cadastreIsNullNameLabel = QLabel(self.myCadastreFrame)
        self.cadastreIsNullNameLabel.setText('Fill in this field')
        self.cadastreIsNullNameLabel.setGeometry(75, 50, 200, 15)
        self.cadastreIsNullNameLabel.setAlignment(Qt.AlignCenter)
        self.cadastreIsNullNameLabel.setStyleSheet(
            '''
                font: 12px Dejavu, Sans, Mono;
                color: #FF0800;
            '''
            )
        self.cadastreIsNullNameLabel.hide()

        # say to insert something in the email input #
        self.cadastreIsNullEmailLabel = QLabel(self.myCadastreFrame)
        self.cadastreIsNullEmailLabel.setText('Fill in this field')
        self.cadastreIsNullEmailLabel.setGeometry(75, 120, 200, 15)
        self.cadastreIsNullEmailLabel.setAlignment(Qt.AlignCenter)
        self.cadastreIsNullEmailLabel.setStyleSheet(
            '''
                font: 12px Dejavu, Sans, Mono;
                color: #FF0800;
            '''
            )
        self.cadastreIsNullEmailLabel.hide()

        # say to insert something in the password input #
        self.cadastreIsNullPasswordLabel = QLabel(self.myCadastreFrame)
        self.cadastreIsNullPasswordLabel.setText('Fill in this field')
        self.cadastreIsNullPasswordLabel.setGeometry(75, 190, 200, 15)
        self.cadastreIsNullPasswordLabel.setAlignment(Qt.AlignCenter)
        self.cadastreIsNullPasswordLabel.setStyleSheet(
            '''
                font: 12px Dejavu, Sans, Mono;
                color: #FF0800;
            '''
            )
        self.cadastreIsNullPasswordLabel.hide()

    def cadastreFrameEntrys(self):

        # name entry #
        self.cadastreNameEntry = QLineEdit(self.myCadastreFrame)
        self.cadastreNameEntry.setAlignment(Qt.AlignCenter)
        self.cadastreNameEntry.setPlaceholderText('Name')
        self.cadastreNameEntry.setMaxLength(50)
        self.cadastreNameEntry.setGeometry(65, 70, 220, 40)
        self.cadastreNameEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0, 0);
                color:whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.cadastreNameEntry.show()

        # email entry #
        self.cadastreEmailEntry = QLineEdit(self.myCadastreFrame)
        self.cadastreEmailEntry.setAlignment(Qt.AlignCenter)
        self.cadastreEmailEntry.setPlaceholderText('E-mail')
        self.cadastreEmailEntry.setMaxLength(50)
        self.cadastreEmailEntry.setGeometry(65, 140, 220, 40)
        self.cadastreEmailEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0, 0);
                color:whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.cadastreEmailEntry.show()

        # password entry #
        self.cadastrePasswordEntry = QLineEdit(self.myCadastreFrame)
        self.cadastrePasswordEntry.setEchoMode(QLineEdit.Password)
        self.cadastrePasswordEntry.setAlignment(Qt.AlignCenter)
        self.cadastrePasswordEntry.setPlaceholderText('Password')
        self.cadastrePasswordEntry.setMaxLength(6)
        self.cadastrePasswordEntry.setGeometry(65, 210, 220, 40)
        self.cadastrePasswordEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0, 0);
                color:whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.cadastrePasswordEntry.show()

    def cadastreFrameButtons(self):

        # return to the login page button #
        self.returnButton = QPushButton(self.myCadastreFrame)
        self.returnButton.setText('⇦ Return to Login')
        self.returnButton.setGeometry(95, 233, 155, 70)
        self.returnButton.setStyleSheet(
            '''
                QPushButton{
                    background: none;
                    color: blueviolet;
                    font: 10px Dejavu, Sans, Mono;
                    border-radius: 7px;
                    }
                QPushButton:hover{
                    text-decoration: underline;
                }
            '''
        )
        self.returnButton.clicked.connect(
            lambda: (
                self.myCadastreFrame.hide(),
                self.loadLoginFrame()
                )
            )
        self.returnButton.show()
        
        # and the cadstre button #
        self.cadastreButton = QPushButton(self.myCadastreFrame)
        self.cadastreButton.setText('S I G N U P')
        self.cadastreButton.setGeometry(125, 285, 100, 50)
        self.cadastreButton.setStyleSheet(
            '''
                QPushButton{
                    background: blueviolet;
                    border: 2px solid blueviolet;
                    color: whitesmoke;
                    font:  12px bold Dejavu, Sans, Mono;
                    border-radius: 10px;
                    }

                QPushButton:hover{
                    border: 2px solid rgb(128, 33, 216);
                    background: rgb(128, 33, 216);
                }

                QPushButton:pressed{
                    background: none;
                    border: 2px solid blueviolet;
                }
            '''
        )
        self.cadastreButton.clicked.connect(lambda: (self.createAccount()))
        self.cadastreButton.show()

    def forgotFrame(self):

        # frame for the forgot frame #
        self.myForgotFrame = QFrame(self)
        self.myForgotFrame.setStyleSheet('background: #111111;')
        self.myForgotFrame.setGeometry(0, 0, 350, 350)

        self.forgotFrameLabels()

        self.forgotFrameEntry()

        self.forgotFrameButtons()
        
        self.myForgotFrame.show()

    def forgotFrameLabels(self):

        # naming the page with a label #
        self.passwordLabel = QLabel(self.myForgotFrame)
        self.passwordLabel.setText('P A S S W O R D')
        self.passwordLabel.setAlignment(Qt.AlignCenter)
        self.passwordLabel.setGeometry(70, 50, 200, 50)
        self.passwordLabel.setStyleSheet(
            '''
                background: none;
                color: whitesmoke;
                font: bold 20px Dejavu, Sans, Mono;
            '''
        )
        self.passwordLabel.show()

        # advise about the email
        self.mensageLabel = QLabel(self.myForgotFrame)
        self.mensageLabel.setText(f'We send you a E-mail \n with your new password!')
        self.mensageLabel.setGeometry(75, 205, 200, 30)
        self.mensageLabel.setAlignment(Qt.AlignCenter)
        self.mensageLabel.setStyleSheet(
            '''
                font: 12px Dejavu, Sans, Mono;
                color: #54FF7F;
            '''
            )
        self.mensageLabel.hide()

        # say to insert something in the email input #
        self.passwordIsNullEmailLabel = QLabel(self.myForgotFrame)
        self.passwordIsNullEmailLabel.setText('Fill in this field')
        self.passwordIsNullEmailLabel.setGeometry(75, 100, 200, 15)
        self.passwordIsNullEmailLabel.setAlignment(Qt.AlignCenter)
        self.passwordIsNullEmailLabel.setStyleSheet(
            '''
                font: 12px Dejavu, Sans, Mono;
                color: #FF0800;
            '''
            )
        self.passwordIsNullEmailLabel.hide()

    def forgotFrameEntry(self):

        # email entry #
        self.passwordEmailEntry = QLineEdit(self.myForgotFrame)
        self.passwordEmailEntry.setPlaceholderText('E-mail')
        self.passwordEmailEntry.setAlignment(Qt.AlignCenter)
        self.passwordEmailEntry.setMaxLength(50)
        self.passwordEmailEntry.setGeometry(65, 120, 220, 40)
        self.passwordEmailEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0 ,0);
                color: whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.passwordEmailEntry.show()

    def forgotFrameButtons(self):

        # return to the login page button #
        self.returnButton = QPushButton(self.myForgotFrame)
        self.returnButton.setText('⇦ Return to Login')
        self.returnButton.setGeometry(95, 150, 155, 70)
        self.returnButton.setStyleSheet(
            '''
                QPushButton{
                    background: none;
                    color: blueviolet;
                    font: 10px Dejavu, Sans, Mono;
                    border-radius: 7px;
                    }
                QPushButton:hover{
                    text-decoration: underline;
            }
            '''
        )
        self.returnButton.clicked.connect(
            lambda: (
                self.myForgotFrame.hide(),
                self.loadLoginFrame()
                )
            )
        self.returnButton.show()

        # this butto will send a mensage in the email you put on the input #
        self.sendMensageButton = QPushButton(self.myForgotFrame)
        self.sendMensageButton.setText('S E N D')
        self.sendMensageButton.setGeometry(125, 250, 100, 50)
        self.sendMensageButton.setStyleSheet(
            '''
                QPushButton{
                    background: blueviolet;
                    border: 2px solid blueviolet;
                    color: whitesmoke;
                    font:  12px bold Dejavu, Sans, Mono;
                    border-radius: 10px;
                    }

                QPushButton:hover{
                    border: 2px solid rgb(128, 33, 216);
                    background: rgb(128, 33, 216);
                }

                QPushButton:pressed{
                    background: none;
                    border: 2px solid blueviolet;
                }
            '''
        )
        self.sendMensageButton.clicked.connect(lambda: (self.newPassword()))
        self.sendMensageButton.show()

    def loadLoginFrame(self):

        self.loginFrame()
        self.loginFrameButtons()
        self.loginFrameEntrys()
        self.loginFrameLabel()

    def loadCadastreFrame(self):

        self.cadastreFrame()
        self.cadastreFrameButtons()
        self.cadastreFrameEntrys()
        self.cadastreFrameLabel()

    def loadForgotFrame(self):

        self.forgotFrame()
        self.forgotFrameButtons()
        self.forgotFrameEntry()
        self.forgotFrameLabels()

    def loginInTheAccount(self):

        # get the text in the inputs #
        self.getemail = self.loginEmailEntry.text()
        self.getpassword = self.loginPasswordEntry.text()

        #make the  advise to insert something in the login input work#
        if self.getemail == '':
            self.loginIsNullEmailLabel.show()
        else:
            self.loginIsNullEmailLabel.hide()

        if self.getpassword == '':
            self.loginIsNullPasswordLabel.show()

        else:

            self.loginIsNullPasswordLabel.hide()

            # change the password and send a email to the user #
            self.cursor.execute(
                    f'''
                        select password from userdata where email = '{self.getemail}'
                    '''
                )
            self.showpassword = self.cursor.fetchall()

            # help to choose a item in a list because is not working #
            for i in self.showpassword:

                if self.getpassword == self.showpassword[0][0]:
                    self.close()
                    mainWindow()
                else:
                    self.loginIsNullPasswordLabel.setText('Your Password is Wrong!')
                    self.loginIsNullPasswordLabel.show()

        # confirm that the login is working #
        print('Login OK!')

    def createAccount(self):
        
        # taking the text of the cadastre entrys #
        self.getname = self.cadastreNameEntry.text()
        self.getemail = self.cadastreEmailEntry.text()
        self.getpassword = self.cadastrePasswordEntry.text()
        
        #make the  advise to insert something in the create account input work#
        if self.getname == '':
            self.cadastreIsNullNameLabel.show()
        else:
            self.cadastreIsNullNameLabel.hide()

        if self.getemail == '':
            self.cadastreIsNullEmailLabel.show()
        else:
            self.cadastreIsNullEmailLabel.hide()

        if self.getpassword == '':
            self.cadastreIsNullPasswordLabel.show()
        else:
            self.cadastreIsNullPasswordLabel.hide()

            # insert the cadastre data in the database #
            self.cursor.execute(
                    '''
                        insert into userdata (name, email, password) values (?, ?, ?);
                    ''',
                (
                    self.getname,
                    self.getemail,
                    self.getpassword
                )
            )
            self.connection.commit()

            # confirm that the login is working #
            print('Cadastre OK!')

    def newPassword(self):
        
        # get the email text, and load random
        self.getemail = self.passwordEmailEntry.text()
        random = randint(100000, 999999)

        self.passwordIsNullEmailLabel.hide()

        try:

            # send the email with the password for the user #
            self.recoverPassLabel = QLineEdit(self)
            self.recoverPassLabel.setText(f'{random}')
            self.getrandom = self.recoverPassLabel.text()

            self.getemail = self.passwordEmailEntry.text()
            EMAIL_ADRESS = ''
            EMAIL_PASSWORD = ''

            self.mensage = EmailMessage()
            self.mensage ['Subject'] = f'Reculperação de Senha.'
            self.mensage ['From'] = 'OpenBox'
            self.mensage ['To'] = self.getemail
            self.mensage.set_content(f'Sua nova senha é *{random}*')

            with smtplib.SMTP_SSL('smtp.gmail.com', 465)  as smtp:
                smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                smtp.send_message(self.mensage)

            # insert the new password in the database #
            self.cursor.execute(
                    f'''
                        update userdata set password = '{self.getrandom}' where email = '{self.getemail}'
                    '''
                )
            self.connection.commit()
            
            # show a mensage to confirm the sending of the password #
            self.mensageLabel.show()

            # confirm that the password recover is working #
            print('Password OK!')
        
        except:
            # hide the mesage to confirm the sending #
            self.mensageLabel.hide()

            # make the label advising to insert something in the email input work #
            if self.getemail == '':
                self.passwordIsNullEmailLabel.show()
            else:
                self.passwordIsNullEmailLabel.setText('Invalid E-mail!')
                self.passwordIsNullEmailLabel.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    load = loginWindow()
    sys.exit = QMainWindow(app.exec())
