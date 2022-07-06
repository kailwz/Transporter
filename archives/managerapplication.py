from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from database import *
import sys

class managerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.windowTab()

        self.loadManagerWindow()

    def loadManagerWindow(self):
        # configurations #
        self.setWindowTitle('U n p a c k - L o c a t i o n')
        self.setWindowIcon(QtGui.QIcon('images/bluevioleticons/logo.png'))
        self.setStyleSheet('background: #111111;')
        self.setMaximumSize(500, 400)
        self.setMinimumSize(500, 400)

        # center the window #
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.show()

    def windowTab(self):
        self.myWindowTab = QTabWidget(self)
        self.myWindowTab.addTab(cadastreItems(), 'C A D A S T R E')
        self.myWindowTab.addTab(productsItems(), 'P R O D U C T S')
        self.myWindowTab.addTab(localItems(), 'L O C A L')
        self.myWindowTab.setGeometry(0, 0, 500, 400)

class cadastreItems(QWidget):
    def __init__(self):
        super().__init__()
        loadDatabase(self)

        self.cadastreFrame()

    def cadastreFrame(self):
        # frame for the cadastre #
        self.myCadastreFrame = QFrame(self)
        self.myCadastreFrame.setStyleSheet('background: #111111;')
        self.myCadastreFrame.setGeometry(0, 0, 500, 400)

        # cadastre frame label #
        self.cadastreFrameLabel()

        # cadastre frame entrys #
        self.cadastreFrameEntrys()

        # cadastre frame buttons #
        self.cadastreFrameButton()

        self.myCadastreFrame.show()

    def cadastreFrameLabel(self):

        # naming the page with a label #
        self.cadastreLabel = QLabel(self.myCadastreFrame)
        self.cadastreLabel.setText('C A D A S T R E')
        self.cadastreLabel.setGeometry(145, 10, 200, 50)
        self.cadastreLabel.setAlignment(Qt.AlignCenter)
        self.cadastreLabel.setStyleSheet(
            '''
                background: none;
                color: whitesmoke;
                font: bold 20px Dejavu, Sans, Mono;
            '''
        )
        self.cadastreLabel.show()

    def cadastreFrameEntrys(self):

        # name entry #
        self.cadastreNameEntry = QLineEdit(self.myCadastreFrame)
        self.cadastreNameEntry.setAlignment(Qt.AlignCenter)
        self.cadastreNameEntry.setPlaceholderText('Name')
        self.cadastreNameEntry.setMaxLength(50)
        self.cadastreNameEntry.setGeometry(135, 70, 220, 40)
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
        self.cadastreNameEntry.setMaxLength(50)
        self.cadastreEmailEntry.setGeometry(135, 140, 220, 40)
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
        self.cadastrePasswordEntry.setGeometry(135, 210, 220, 40)
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

    def cadastreFrameButton(self):
        # and the cadstre button #
        self.cadastreButton = QPushButton(self.myCadastreFrame)
        self.cadastreButton.setText('S I G N U P')
        self.cadastreButton.setGeometry(200, 285, 100, 50)
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
        self.cadastreButton.clicked.connect(lambda: (self.insertChangedUser()))
        self.cadastreButton.show()

    def insertChangedUser(self):
        
        # taking the text of the cadastre entrys #
        self.getname = self.cadastreNameEntry.text()
        self.getemail = self.cadastreEmailEntry.text()
        self.getpassword = self.cadastrePasswordEntry.text()

        # insert the cadastre data in the database #
        self.cursor.execute(
                '''
                    update userdata set name=?, email=?, password=? where email=?
                ''',
            (
                self.getname,
                self.getemail,
                self.getpassword,
                self.getemail
            )
        )
        self.connection.commit()

        # confirm that the login is working #
        print('Change Data OK!')

class productsItems(QWidget):
    def __init__(self):
        super().__init__()

        loadDatabase(self)

        self.productsFrame()

    def productsFrame(self):
        # frame for the products #
        self.myProductsFrame = QFrame(self)
        self.myProductsFrame.setStyleSheet('background: #111111;')
        self.myProductsFrame.setGeometry(0, 0, 500, 400)

        # products frame label #
        self.productsFrameLabel()

        # products frame entrys #
        self.productsFrameEntrys()

        # products frame buttons #
        self.productsFrameButton()

        self.myProductsFrame.show()

    def productsFrameLabel(self):

        # naming the page with a label #
        self.productsLabel = QLabel(self.myProductsFrame)
        self.productsLabel.setText('P R O D U C T S')
        self.productsLabel.setGeometry(145, 10, 200, 50)
        self.productsLabel.setAlignment(Qt.AlignCenter)
        self.productsLabel.setStyleSheet(
            '''
                background: none;
                color: whitesmoke;
                font: bold 20px Dejavu, Sans, Mono;
            '''
        )
        self.productsLabel.show()

    def productsFrameEntrys(self):

        # name entry #
        self.productsNameEntry = QLineEdit(self.myProductsFrame)
        self.productsNameEntry.setAlignment(Qt.AlignCenter)
        self.productsNameEntry.setPlaceholderText('Name')
        self.productsNameEntry.setMaxLength(50)
        self.productsNameEntry.setGeometry(135, 70, 220, 40)
        self.productsNameEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0, 0);
                color:whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.productsNameEntry.show()

        # price entry #
        self.productsPriceEntry = QLineEdit(self.myProductsFrame)
        self.productsPriceEntry.setAlignment(Qt.AlignCenter)
        self.productsPriceEntry.setPlaceholderText('Price')
        self.productsPriceEntry.setMaxLength(10)
        self.productsPriceEntry.setGeometry(135, 140, 220, 40)
        self.productsPriceEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0, 0);
                color:whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.productsPriceEntry.show()

        # Quantity entry #
        self.productsQuantityEntry = QLineEdit(self.myProductsFrame)
        self.productsQuantityEntry.setAlignment(Qt.AlignCenter)
        self.productsQuantityEntry.setPlaceholderText('Quantity')
        self.productsQuantityEntry.setMaxLength(100)
        self.productsQuantityEntry.setGeometry(135, 210, 220, 40)
        self.productsQuantityEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0, 0);
                color:whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.productsQuantityEntry.show()

    def productsFrameButton(self):
        # and the cadstre button #
        self.productsButton = QPushButton(self.myProductsFrame)
        self.productsButton.setText('A D D')
        self.productsButton.setGeometry(200, 285, 100, 50)
        self.productsButton.setStyleSheet(
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
        self.productsButton.clicked.connect(lambda: (self.insertProductInfo()))
        self.productsButton.show()

    def insertProductInfo(self):
        self.getname = self.productsNameEntry.text()
        self.getprice = self.productsPriceEntry.text()
        self.getquantity = self.productsQuantityEntry.text()

        self.cursor.execute(
            '''
                insert into productinfo (name, price, quantity) values (?, ?, ?);
            ''',
            (
                self.getname,
                self.getprice,
                self.getquantity
            )
        )
        self.connection.commit()
        print('Product OK!')

class localItems(QWidget):
    def __init__(self):
        super().__init__()
        loadDatabase(self)

        self.localFrame()

    def localFrame(self):
        # frame for the local #
        self.myLocalFrame = QFrame(self)
        self.myLocalFrame.setStyleSheet('background: #111111;')
        self.myLocalFrame.setGeometry(0, 0, 500, 400)

        # local frame label #
        self.localFrameLabel()

        # local frame entrys #
        self.localFrameEntrys()

        # local frame buttons #
        self.localFrameButton()

        self.myLocalFrame.show()

    def localFrameLabel(self):

        # naming the page with a label #
        self.localLabel = QLabel(self.myLocalFrame)
        self.localLabel.setText('L O C A L')
        self.localLabel.setGeometry(145, 10, 200, 50)
        self.localLabel.setAlignment(Qt.AlignCenter)
        self.localLabel.setStyleSheet(
            '''
                background: none;
                color: whitesmoke;
                font: bold 20px Dejavu, Sans, Mono;
            '''
        )
        self.localLabel.show()

    def localFrameEntrys(self):

        # name entry #
        self.localNameEntry = QLineEdit(self.myLocalFrame)
        self.localNameEntry.setAlignment(Qt.AlignCenter)
        self.localNameEntry.setPlaceholderText('Name')
        self.localNameEntry.setMaxLength(50)
        self.localNameEntry.setGeometry(135, 70, 220, 40)
        self.localNameEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0, 0);
                color:whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.localNameEntry.show()

        # Date entry #
        self.localDateEntry = QDateEdit(self.myLocalFrame)
        self.localDateEntry.setAlignment(Qt.AlignCenter)
        self.localDateEntry.setGeometry(135, 130, 220, 40)
        self.localDateEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0, 0);
                color:whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.localDateEntry.show()

        # Hour entry #
        self.localHourEntry = QTimeEdit(self.myLocalFrame)
        self.localHourEntry.setAlignment(Qt.AlignCenter)
        self.localHourEntry.setGeometry(135, 190, 220, 40)
        self.localHourEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0, 0);
                color:whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.localHourEntry.show()

        # email entry #
        self.climateEntry = QLineEdit(self.myLocalFrame)
        self.climateEntry.setPlaceholderText('Climate informations')
        self.climateEntry.setAlignment(Qt.AlignCenter)
        self.climateEntry.setMaxLength(50)
        self.climateEntry.setGeometry(135, 250, 220, 40)
        self.climateEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0 ,0);
                color: whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.climateEntry.show()

    def localFrameButton(self):
        # and the cadstre button #
        self.localButton = QPushButton(self.myLocalFrame)
        self.localButton.setText('U P D A T E')
        self.localButton.setGeometry(200, 300, 100, 50)
        self.localButton.setStyleSheet(
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
        self.localButton.clicked.connect(lambda: (self.localization()))
        self.localButton.show()

    def localization(self):
        self.getname = self.localNameEntry.text()
        self.getdate = self.localDateEntry.text()
        self.gethour = self.localHourEntry.text()
        self.getclimate = self.climateEntry.text()
        
        self.cursor.execute(
            '''
                insert into productlocation (local, date, hour, climate) values (?, ?, ?, ?)
            ''',
            (
                self.getname,
                self.getdate,
                self.gethour,
                self.getclimate
            )
        )
        self.connection.commit()
        print('Works')

app = QApplication(sys.argv)
load = managerWindow()
sys.exit(app.exec())
