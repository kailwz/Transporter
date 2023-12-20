import sys
from changeThemes import contrastMode, whiteMode, darkMode
from email.message import EmailMessage
from changeFonts import ubuntuFont
from database import loadDatabase
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import requests
import smtplib

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadDatabase(self)

        self.menuBarButtons()

        self.welcomeFrame()

        self.productsFrame()

        self.blockFrame()

        self.infoFrame()

        self.searchFrame()
        
        self.locationFrame()

        self.mensageFrame()

        self.settingsFrame()

        self.welcomeFrame()

        self.loadWindow()
    
    def loadWindow(self):
        # window configurations #
        self.setWindowTitle('U n p a c k')
        self.setWindowIcon(QtGui.QIcon('images/bluevioleticons/logo.png'))
        self.setStyleSheet('background-color: #151515;')
        self.setMaximumSize(900, 600)
        self.setMinimumSize(900, 600)

        # center the window #
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.show()

    def menuBarButtons(self):
        self.logoButton = QPushButton(self)
        self.logoButton.setGeometry(0, 10, 70, 50)
        self.logoButton.setStyleSheet(
            '''
                QPushButton{
                    border: none;
                    background-image: url(images/whiteicons/logo.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton:hover{
                    border-left: 2px solid blueviolet;
                    background-image: url(images/bluevioleticons/logo.png);
                }

                QPushButton:pressed{
                    background-color: #111111;
                }
            '''
        )
        self.logoButton.clicked.connect(lambda: (self.deleteAllFrames(), self.myWelcomeFrame.show()))
        self.logoButton.show()

        self.homeButton = QPushButton(self)
        self.homeButton.setGeometry(0, 60, 70, 50)
        self.homeButton.setStyleSheet(
            '''
                QPushButton{
                    border: none;
                    background-image: url(images/whiteicons/home.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton:hover{
                    border-left: 2px solid blueviolet;
                    background-image: url(images/bluevioleticons/home.png);
                }

                QPushButton:pressed{
                    background-color: #111111;
                }
            '''
        )
        self.homeButton.clicked.connect(lambda: (self.deleteAllFrames(), self.myProductsFrame.show()))
        self.homeButton.show()

        self.searchButton = QPushButton(self)
        self.searchButton.setGeometry(0, 110, 70, 50)
        self.searchButton.setStyleSheet(
            '''
                QPushButton{
                    border: none;
                    background-image: url(images/whiteicons/search.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton:hover{
                    border-left: 2px solid blueviolet;
                    background-image: url(images/bluevioleticons/search.png);
                }

                QPushButton:pressed{
                    background-color: #111111;
                }
            '''
        )
        self.searchButton.clicked.connect(lambda: (self.deleteAllFrames(), self.mySearchFrame.show()))
        self.searchButton.show()

        self.markerButton = QPushButton(self)
        self.markerButton.setGeometry(0, 160, 70, 50)
        self.markerButton.setStyleSheet(
            '''
                QPushButton{
                    border: none;
                    background-image: url(images/whiteicons/marker.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton:hover{
                    border-left: 2px solid blueviolet;
                    background-image: url(images/bluevioleticons/marker.png);
                }

                QPushButton:pressed{
                    background-color: #111111;
                }
            '''
        )
        self.markerButton.clicked.connect(lambda: (self.deleteAllFrames(), self.myLocationFrame.show()))
        self.markerButton.show()

        self.mensageButton = QPushButton(self)
        self.mensageButton.setGeometry(0, 210, 70, 50)
        self.mensageButton.setStyleSheet(
            '''
                QPushButton{
                    border: none;
                    background-image: url(images/whiteicons/mensage.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton:hover{
                    border-left: 2px solid blueviolet;
                    background-image: url(images/bluevioleticons/mensage.png);
                }

                QPushButton:pressed{
                    background-color: #111111;
                }
            '''
        )
        self.mensageButton.clicked.connect(lambda: (self.deleteAllFrames(), self.myMensageFrame.show()))
        self.mensageButton.show()

        self.settingsButton = QPushButton(self)
        self.settingsButton.setGeometry(0, 260, 70, 50)
        self.settingsButton.setStyleSheet(
            '''
                QPushButton{
                    border: none;
                    background-image: url(images/whiteicons/settings.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton:hover{
                    border-left: 2px solid blueviolet;
                    background-image: url(images/bluevioleticons/settings.png);
                }

                QPushButton:pressed{
                    background-color: #111111;
                }
            '''
        )
        self.settingsButton.clicked.connect(lambda: (self.deleteAllFrames(), self.mySettingsFrame.show()))
        self.settingsButton.show()

    def welcomeFrame(self):
        self.myWelcomeFrame = QFrame(self)
        self.myWelcomeFrame.setGeometry(70, 0, 830, 600)
        self.myWelcomeFrame.setStyleSheet(
            '''
                QFrame{
                    background-color: #111111;
                }
            '''
        )

        self.welcomeFrameLabels()
        self.myWelcomeFrame.show()

    def welcomeFrameLabels(self):
        self.enterpriseNameLabel = QLabel(self.myWelcomeFrame)
        self.enterpriseNameLabel.setGeometry(0, 200, 830, 80)
        self.enterpriseNameLabel.setAlignment(Qt.AlignCenter)
        self.enterpriseNameLabel.setText('Unpack')
        self.enterpriseNameLabel.setStyleSheet(
            '''
                QLabel{
                    color: blueviolet;
                    font: bold 60px Dejavu, Sans, Mono;
                }
            '''
        )
        self.enterpriseNameLabel.show()
        
        self.userLogoButton = QPushButton(self.myWelcomeFrame)
        self.userLogoButton.setGeometry(370, 290, 80, 80)
        self.userLogoButton.setStyleSheet(
            '''
                QPushButton{
                    background: rgba(0, 0, 0, 0);
                    background-image: url(images/bluevioleticons/user.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }
            '''
        )
        self.userLogoButton.clicked.connect(lambda: (changeUserWindow()))
        self.userLogoButton.show()
        
        self.randomMensageLabel = QLabel(self.myWelcomeFrame)
        self.randomMensageLabel.setGeometry(0, 370, 830, 50)
        self.randomMensageLabel.setAlignment(Qt.AlignCenter)
        self.randomMensageLabel.setText('Configure your <b>User<b>.')
        self.randomMensageLabel.setStyleSheet(
            '''
                QLabel{
                    color: whitesmoke;
                    font: 15px Dejavu, Sans, Mono;
                }
            '''
        )
        self.randomMensageLabel.show()

    def productsFrame(self):
        self.myProductsFrame = QFrame(self)
        self.myProductsFrame.setGeometry(70, 0, 830, 600)
        self.myProductsFrame.setStyleSheet(
            '''
                QFrame{
                    background-color: #111111;
                }
            '''
        )

        self.myProductsFrame.show()

        self.productsFrameLabels()

        self.productsFrameScrollArea()

    def productsFrameScrollArea(self):       
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        object = QPushButton()
        object.setFixedSize(180, 250)
        object.setStyleSheet(
            '''
                QPushButton{
                    background-image: url(images/productsimages/monalisa.png);
                    border-radius: 10px;
                }
            '''
        )
        object.clicked.connect(lambda: (self.myBlockFrame.show(), self.myInfoFrame.show()))

        product = object
        self.vbox.addWidget(product)

        self.widget.setLayout(self.vbox)

        self.scrollArea = QScrollArea(self.myProductsFrame)
        self.scrollArea.setGeometry(30, 70, 760, 500)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)
        self.scrollArea.setStyleSheet(
            '''
                color: whitesmoke;
                background-color: #111111;
                border: none;
            '''
        )
        self.scrollArea.show()

    def productsFrameLabels(self):
        self.titleLabel = QLabel(self.myProductsFrame)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setGeometry(30, 10, 760, 50)
        self.titleLabel.setText('P R O D U C T S')
        self.titleLabel.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: whitesmoke;
                    font: bold 25px Dejavu, Sans, Mono;
                    border-radius: none;
                    border-bottom: 2px solid whitesmoke;
                }
            '''
        )
        
        self.titleLabel.show()

    def infoFrame(self):
        self.myInfoFrame = QFrame(self)
        self.myInfoFrame.setGeometry(610, 0, 300, 600)
        self.myInfoFrame.setStyleSheet(
            '''
                QFrame{
                    background-color: #151515;
                }
            '''
        )

        self.infoFrameLabels()

        self.infoFrameButtons()

        self.myInfoFrame.hide()

    def infoFrameLabels(self):
        self.imageLabel = QLabel(self.myInfoFrame)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setGeometry(0, 65, 300, 275)
        self.imageLabel.setStyleSheet(
            '''
                QLabel{
                    background-image: url(images/productsimages/monalisa.png);
                    background-position: center;
                    background-repeat: no-repeat;
                    border-radius: 10px;
                }
            '''
        )

        self.imageLabel.show()

        self.cursor.execute('select name from productinfo where id="1"')
        name = self.cursor.fetchall()
        productname = str(name)[3:-4]

        self.infoLabel = QLabel(self.myInfoFrame)
        self.infoLabel.setAlignment(Qt.AlignCenter)
        self.infoLabel.setText(f'{productname}')
        self.infoLabel.setGeometry(0, 340, 300, 50)
        self.infoLabel.setStyleSheet(
            '''
                QLabel{
                    color: whitesmoke;
                    font: 15px Dejavu, Sans, Mono;
                    background: none;
                }
            '''
        )

        self.infoLabel.show()

        self.cursor.execute('select price from productinfo where id="1"')
        price = self.cursor.fetchall()
        productprice = str(price)[2:-3]

        self.priceLabel = QLabel(self.myInfoFrame)
        self.priceLabel.setAlignment(Qt.AlignCenter)
        self.priceLabel.setText(f'R$ {productprice}')
        self.priceLabel.setGeometry(0, 370, 300, 50)
        self.priceLabel.setStyleSheet(
            '''
                QLabel{
                    color: #2ecc71;
                    font: 15px Dejavu, Sans, Mono;
                    background: none;
                }
            '''
        )

        self.priceLabel.show()

        self.cursor.execute('select quantity from productinfo where id="1"')
        quantity = self.cursor.fetchall()
        productquantity = str(quantity)[2:-3]

        self.unitLabel = QLabel(self.myInfoFrame)
        self.unitLabel.setAlignment(Qt.AlignCenter)
        self.unitLabel.setText(f'Avaliable Unit: {productquantity}')
        self.unitLabel.setGeometry(0, 400, 300, 50)
        self.unitLabel.setStyleSheet(
            '''
                QLabel{
                    color: whitesmoke;
                    font: 15px Dejavu, Sans, Mono;
                    background: none;
                }
            '''
        )

        self.unitLabel.show()

    def infoFrameButtons(self):
        self.closeInfoFrameButton = QPushButton(self.myInfoFrame)
        self.closeInfoFrameButton.setGeometry(5, 5, 30, 30)
        self.closeInfoFrameButton.setText('⇠')
        self.closeInfoFrameButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: blueviolet;
                    border-radius: 5px;
                    font: 20px bold Dejavu, Sans, Mono;
                    color: whitesmoke;
                }

                QPushButton:hover{
                    background-color: rgb(128, 33, 216);
                }
                
                QPushButton:pressed{
                    background-color: #111111;
                    border: 2px solid blueviolet;
                }
            '''
        )

        self.closeInfoFrameButton.clicked.connect(self.deleteInfoFrameAndBlockFrame)

        self.closeInfoFrameButton.show()

        self.buyProductButton = QPushButton(self.myInfoFrame)
        self.buyProductButton.setGeometry(50, 450, 200, 50)
        self.buyProductButton.setText('B U Y')
        self.buyProductButton.setStyleSheet(
            '''
                QPushButton{
                    font: 12px bold Dejavu, Sans, Mono;
                    background-color: blueviolet;
                    border-radius: 5px;
                    color: whitesmoke;
                }

                QPushButton:hover{
                    background-color: rgb(128, 33, 216);
                }
                
                QPushButton:pressed{
                    background-color: #111111;
                    border: 2px solid blueviolet;
                }
            '''
        )

        self.buyProductButton.clicked.connect(lambda: (purchaseWindow()))
        self.buyProductButton.show()

    def blockFrame(self):
        self.myBlockFrame = QFrame(self)
        self.myBlockFrame.setGeometry(0, 0, 900, 600)
        self.myBlockFrame.setStyleSheet(
            '''
                QFrame{
                    background-color: rgba(10, 10, 10, 200);
                }
            '''
        )
        self.myBlockFrame.hide()

    def searchFrame(self):
        self.mySearchFrame = QFrame(self)
        self.mySearchFrame.setGeometry(70, 0, 830, 600)
        self.mySearchFrame.setStyleSheet(
            '''
                QFrame{
                    background-color: #111111;
                }
            '''
        )

        self.searchFrameLabels()

        self.searchFrameEntrys()

        self.searchFrameButtons()

        self.mySearchFrame.show()

    def searchFrameLabels(self):
        self.searchLabel = QLabel(self.mySearchFrame)
        self.searchLabel.setAlignment(Qt.AlignCenter)
        self.searchLabel.setGeometry(30, 10, 760, 50)
        self.searchLabel.setText('S E A R C H E R')
        self.searchLabel.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: whitesmoke;
                    font: bold 25px Dejavu, Sans, Mono;
                    border-radius: none;
                    border-bottom: 2px solid whitesmoke;
                }
            '''
        )
        self.searchLabel.show()

    def searchFrameEntrys(self):
        self.typeCepEntry = QLineEdit(self.mySearchFrame)
        self.typeCepEntry.setAlignment(Qt.AlignCenter)
        self.typeCepEntry.setGeometry(265, 90, 300, 40)
        self.typeCepEntry.setMaxLength(8)
        self.typeCepEntry.setPlaceholderText('Type Your CEP:')
        self.typeCepEntry.setStyleSheet(
            '''
                QLineEdit{
                    background: rgba(0, 0, 0 ,0);
                    color: whitesmoke;
                    border: 2px solid blueviolet;
                    border-radius: 7px;
                    font: 14px Dejavu, Sans, Mono;
                }
            '''
        )
        self.typeCepEntry.show()

        self.searchState = QLineEdit(self.mySearchFrame)
        self.searchState.setGeometry(265, 160, 300, 40)
        self.searchState.setPlaceholderText('State')
        self.searchState.setAlignment(Qt.AlignCenter)
        self.searchState.setStyleSheet(
            '''
                QLineEdit{
                    background: rgba(0, 0, 0 ,0);
                    color: whitesmoke;
                    border-bottom: 2px solid whitesmoke;
                    border-radius: 0px;
                    font: 14px Dejavu, Sans, Mono;
                }
            '''
        )
        self.searchState.setDisabled(True)
        self.searchState.show()

        self.searchCity = QLineEdit(self.mySearchFrame)
        self.searchCity.setGeometry(265, 230, 300, 40)
        self.searchCity.setPlaceholderText('City')
        self.searchCity.setAlignment(Qt.AlignCenter)
        self.searchCity.setStyleSheet(
            '''
                QLineEdit{
                    background: rgba(0, 0, 0 ,0);
                    color: whitesmoke;
                    border-bottom: 2px solid whitesmoke;
                    border-radius: 0px;
                    font: 14px Dejavu, Sans, Mono;
                }
            '''
        )
        self.searchCity.setDisabled(True)
        self.searchCity.show()

        self.searchStreet = QLineEdit(self.mySearchFrame)
        self.searchStreet.setGeometry(265, 300, 300, 40)
        self.searchStreet.setPlaceholderText('Street')
        self.searchStreet.setAlignment(Qt.AlignCenter)
        self.searchStreet.setStyleSheet(
            '''
                QLineEdit{
                    background: rgba(0, 0, 0 ,0);
                    color: whitesmoke;
                    border-bottom: 2px solid whitesmoke;
                    border-radius: 0px;
                    font: 14px Dejavu, Sans, Mono;
                }
            '''
        )
        self.searchStreet.setDisabled(True)
        self.searchStreet.show()

        self.searchNeighborhood = QLineEdit(self.mySearchFrame)
        self.searchNeighborhood.setGeometry(265, 370, 300, 40)
        self.searchNeighborhood.setPlaceholderText('Neighborhood')
        self.searchNeighborhood.setAlignment(Qt.AlignCenter)
        self.searchNeighborhood.setStyleSheet(
            '''
                QLineEdit{
                    background: rgba(0, 0, 0 ,0);
                    color: whitesmoke;
                    border-bottom: 2px solid whitesmoke;
                    border-radius: 0px;
                    font: 14px Dejavu, Sans, Mono;
                }
            '''
        )
        self.searchNeighborhood.setDisabled(True)
        self.searchNeighborhood.show()

    def searchFrameButtons(self):
        self.searchCepButton = QPushButton(self.mySearchFrame)
        self.searchCepButton.setText('S E A R C H')
        self.searchCepButton.setGeometry(265, 440, 300, 50)
        self.searchCepButton.setStyleSheet(
            '''
                QPushButton{
                    font: 12px Dejavu, Sans, Mono;
                    background-color: blueviolet;
                    border-radius: 7px;
                    color: whitesmoke;
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
        self.searchCepButton.clicked.connect(lambda: (self.insertCepInfo()))
        self.searchCepButton.show()

    def locationFrame(self):
        self.myLocationFrame = QFrame(self)
        self.myLocationFrame.setGeometry(70, 0, 830, 600)
        self.myLocationFrame.setStyleSheet(
            '''
                QFrame{
                    background-color: #111111;
                }
            '''
        )
        self.createClimateLabel()

        self.locationFrameLabel()

        self.locationFrameEntry()

        self.locationFrameButtons()

        self.myLocationFrame.show()

    def locationFrameLabel(self):
        self.localizationLabel = QLabel(self.myLocationFrame)
        self.localizationLabel.setAlignment(Qt.AlignCenter)
        self.localizationLabel.setGeometry(30, 10, 760, 50)
        self.localizationLabel.setText('L O C A L I Z A T I O N')
        self.localizationLabel.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: whitesmoke;
                    font: bold 25px Dejavu, Sans, Mono;
                    border-radius: none;
                    border-bottom: 2px solid whitesmoke;
                }
            '''
        )
        self.localizationLabel.show()

    def createClimateLabel(self):

        self.cursor.execute('select climate from productlocation where id="1"')
        climate = self.cursor.fetchall()
        localclimate = str(climate)[3:-4]

        self.climateLabel = QLabel(self.myLocationFrame)
        self.climateLabel.setGeometry(30, 150, 760, 400)
        self.climateLabel.setAlignment(Qt.AlignCenter)
        self.climateLabel.setText(f'{localclimate}')
        self.climateLabel.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: whitesmoke;
                    font: bold 14px Dejavu, Sans, Mono;
                    border: 2px solid blueviolet;
                    border-radius: 7px;
                }
            '''
        )
        self.climateLabel.hide()

    def locationFrameEntry(self):
        self.codeEntry = QLineEdit(self.myLocationFrame)
        self.codeEntry.setPlaceholderText('Search Code')
        self.codeEntry.setMaxLength(6)
        self.codeEntry.setGeometry(30, 80, 700, 50)
        self.codeEntry.setStyleSheet(
            '''
                QLineEdit{
                    background: rgba(0, 0, 0 ,0);
                    color: whitesmoke;
                    border: 2px solid blueviolet;
                    border-radius: 7px;
                    font: 14px Dejavu, Sans, Mono;
                }
            '''
        )
        self.codeEntry.show()

    def locationFrameButtons(self):
        self.searchCodeButton = QPushButton(self.myLocationFrame)
        self.searchCodeButton.setText('🔍')
        self.searchCodeButton.setGeometry(740, 80, 50, 50)
        self.searchCodeButton.setStyleSheet(
            '''
                QPushButton{
                    font: 20px Dejavu, Sans, Mono;
                    background-color: blueviolet;
                    border-radius: 7px;
                    color: whitesmoke;
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

        self.searchCodeButton.clicked.connect(lambda: (locationWindow()))
        self.searchCodeButton.show()

        self.searchClimateButton = QPushButton(self.myLocationFrame)
        self.searchClimateButton.setText('+')
        self.searchClimateButton.setGeometry(381, 180, 50, 50)
        self.searchClimateButton.setStyleSheet(
            '''
                QPushButton{
                    font: 20px Dejavu, Sans, Mono;
                    background-color: blueviolet;
                    border-radius: 25px;
                    color: whitesmoke;
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

        self.searchClimateButton.clicked.connect(lambda: (self.climateLabel.show(), self.deleteClimateButton.show(), self.searchClimateButton.hide()))
        self.searchClimateButton.show()

        self.deleteClimateButton = QPushButton(self.myLocationFrame)
        self.deleteClimateButton.setText('x')
        self.deleteClimateButton.setGeometry(760, 160, 20, 20)
        self.deleteClimateButton.setStyleSheet(
            '''
                QPushButton{
                    font: 12px Dejavu, Sans, Mono;
                    background-color: blueviolet;
                    border-radius: 10px;
                    color: whitesmoke;
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
        self.deleteClimateButton.clicked.connect(lambda: (self.deleteClimateButton.hide(), self.climateLabel.hide(), self.searchClimateButton.show()))
        self.deleteClimateButton.hide()

    def mensageFrame(self):
        self.myMensageFrame = QFrame(self)
        self.myMensageFrame.setGeometry(70, 0, 830, 600)
        self.myMensageFrame.setStyleSheet(
            '''
                QFrame{
                    background-color: #111111;
                }
            '''
        )

        self.mensageFrameLabels()

        self.mensageFrameEntrys()

        self.mensageFrameButtons()

        self.myMensageFrame.show()

    def mensageFrameLabels(self):
        self.mensageLabel = QLabel(self.myMensageFrame)
        self.mensageLabel.setAlignment(Qt.AlignCenter)
        self.mensageLabel.setGeometry(30, 10, 760, 50)
        self.mensageLabel.setText('M E N S A G E')
        self.mensageLabel.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: whitesmoke;
                    font: bold 25px Dejavu, Sans, Mono;
                    border-radius: none;
                    border-bottom: 2px solid whitesmoke;
                }
            '''
        )
        self.mensageLabel.show()

    def mensageFrameEntrys(self):
        self.mensageBox = QPlainTextEdit(self.myMensageFrame)
        self.mensageBox.setPlaceholderText('Type here your mensage...')
        self.mensageBox.setGeometry(30, 80, 760, 400)
        self.mensageBox.setStyleSheet(
            '''
                QPlainTextEdit{
                    background: rgba(0, 0, 0 ,0);
                    color: whitesmoke;
                    border: 2px solid blueviolet;
                    border-radius: 7px;
                    font: 14px Dejavu, Sans, Mono;
                }
            '''
        )
        self.mensageBox.show()

    def mensageFrameButtons(self):
        self.sendMensageButton = QPushButton(self.myMensageFrame)
        self.sendMensageButton.setText('S E N D')
        #self.sendMensageButton.setGeometry(315, 500, 200, 50)
        self.sendMensageButton.setGeometry(30, 500, 760, 50)
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
        self.sendMensageButton.clicked.connect(self.sendEmail)
        self.sendMensageButton.show()

    def settingsFrame(self):
        self.mySettingsFrame = QFrame(self)
        self.mySettingsFrame.setGeometry(70, 0, 830, 600)
        self.mySettingsFrame.setStyleSheet(
            '''
                QFrame{
                    background: #111111;
                }
            '''
        )

        self.settingsFrameLabels()

        self.settingsFrameButtons()

        self.mySettingsFrame.show()

    def settingsFrameLabels(self):
        self.settingsLabel = QLabel(self.mySettingsFrame)
        self.settingsLabel.setAlignment(Qt.AlignCenter)
        self.settingsLabel.setGeometry(30, 10, 760, 50)
        self.settingsLabel.setText('S E T T I N G S')
        self.settingsLabel.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: whitesmoke;
                    font: bold 25px Dejavu, Sans, Mono;
                    border-radius: none;
                    border-bottom: 2px solid whitesmoke;
                }
            '''
        )
        self.settingsLabel.show()

        self.themesLabel = QLabel(self.mySettingsFrame)
        self.themesLabel.setAlignment(Qt.AlignLeft)
        self.themesLabel.setGeometry(30, 80, 100, 30)
        self.themesLabel.setText('T h e m e s')
        self.themesLabel.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: whitesmoke;
                    font: 14px Dejavu, Sans, Mono;
                    border-radius: none;
                    border-bottom: 1px solid whitesmoke;
                }
            '''
        )
        self.themesLabel.show()

        self.fontsLabel = QLabel(self.mySettingsFrame)
        self.fontsLabel.setAlignment(Qt.AlignLeft)
        self.fontsLabel.setGeometry(30, 320, 100, 30)
        self.fontsLabel.setText('F o n t s')
        self.fontsLabel.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: whitesmoke;
                    font: 14px Dejavu, Sans, Mono;
                    border-radius: none;
                    border-bottom: 1px solid whitesmoke;
                }
            '''
        )
        self.fontsLabel.show()

    def settingsFrameButtons(self):
        self.darkThemeButton = QPushButton(self.mySettingsFrame)
        self.darkThemeButton.setGeometry(30, 140, 160, 160)
        self.darkThemeButton.setStyleSheet(
            '''
                QPushButton{
                    background: rgba(0, 0, 0, 0);
                    background-image: url(images/themeIcons/dark.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }
            '''
        )
        self.darkThemeButton.clicked.connect(lambda: (darkMode(self)))
        self.darkThemeButton.show()

        self.whiteThemeButton = QPushButton(self.mySettingsFrame)
        self.whiteThemeButton.setGeometry(230, 140, 160, 160)
        self.whiteThemeButton.setStyleSheet(
            '''
                QPushButton{
                    background: rgba(0, 0, 0, 0);
                    background-image: url(images/themeIcons/white.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }
            '''
        )
        self.whiteThemeButton.clicked.connect(lambda: (whiteMode(self)))
        self.whiteThemeButton.show()

        self.highContrastThemeButton = QPushButton(self.mySettingsFrame)
        self.highContrastThemeButton.setGeometry(430, 140, 160, 160)
        self.highContrastThemeButton.setStyleSheet(
            '''
                QPushButton{
                    background: rgba(0, 0, 0, 0);
                    background-image: url(images/themeIcons/highcontrast.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }
            '''
        )
        self.highContrastThemeButton.clicked.connect(lambda: (contrastMode(self)))
        self.highContrastThemeButton.show()

        self.arialFont = QRadioButton('Arial', self.mySettingsFrame)
        self.arialFont.setGeometry(30, 370, 55, 14)
        self.arialFont.setStyleSheet(
            '''
                QRadioButton{
                    background: rgba(0, 0, 0, 0);
                    font: 14px Arial;
                    color: whitesmoke;
                }

                QRadioButton::indicator{
                    border: 1px solid white;
                    border-radius: 2px;
                }

                QRadioButton::indicator::checked{
                    background: blueviolet;
                    background-position: center;
                }
            '''
        )
        self.arialFont.show()

        self.helveticaFont = QRadioButton('Helvetica', self.mySettingsFrame)
        self.helveticaFont.setGeometry(100, 370, 85, 14)
        self.helveticaFont.setStyleSheet(
            '''
                QRadioButton{
                    background: rgba(0, 0, 0, 0);
                    font: 14px Helvetica;
                    color: whitesmoke;
                }

                QRadioButton::indicator{
                    border: 1px solid white;
                    border-radius: 2px;
                }

                QRadioButton::indicator::checked{
                    background: blueviolet;
                    background-position: center;
                }
            '''
        )
        self.helveticaFont.show()

        self.ubuntuMonoFont = QRadioButton('Ubuntu Mono', self.mySettingsFrame)
        self.ubuntuMonoFont.setGeometry(190, 370, 120, 14)
        self.ubuntuMonoFont.setStyleSheet(
            '''
                QRadioButton{
                    background: rgba(0, 0, 0, 0);
                    font: 14px Ubuntu Mono;
                    color: whitesmoke;
                }

                QRadioButton::indicator{
                    border: 1px solid white;
                    border-radius: 2px;
                }

                QRadioButton::indicator::checked{
                    background: blueviolet;
                    background-position: center;
                }
            '''
        )
        self.ubuntuMonoFont.toggled.connect(lambda: (ubuntuFont(self)))
        self.ubuntuMonoFont.show()

    def deleteInfoFrameAndBlockFrame(self):

        try:
            self.myInfoFrame.hide()
        except:
            pass
        try:
            self.myBlockFrame.hide()
        except:
            pass

    def deleteAllFrames(self):

        try:
            self.mySearchFrame.hide()
        except:
            pass

        try:
            self.myWelcomeFrame.hide()
        except:
            pass

        try:
            self.myProductsFrame.hide()
        except:
            pass

        try:
            self.myLocationFrame.hide()
        except:
            pass

        try:
            self.myMensageFrame.hide()
        except:
            pass

        try:
            self.mySettingsFrame.hide()
        except:
            pass

    def sendEmail(self):

        self.getmensage = self.mensageBox.toPlainText()
        self.interpriseEmail = ''

        EMAIL_ADRESS = ''
        EMAIL_PASSWORD = ''

        self.mensage = EmailMessage()
        self.mensage ['Subject'] = f'Personal User Mensage.'
        self.mensage ['From'] = 'User'
        self.mensage ['To'] = self.interpriseEmail
        self.mensage.set_content(f'{self.getmensage}')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465)  as smtp:
            smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
            smtp.send_message(self.mensage)

        print('Mensage OK!')

    def localizeCep(self, cep):
        getcep = self.typeCepEntry.text()
        url = 'https://viacep.com.br/ws/%s/json/' % getcep
        response = requests.get(url)
        response_json = response.json()
        return response_json

    def insertCepInfo(self):
        try:
            uf = self.localizeCep(['cep'])['uf']
            logradouro = self.localizeCep('cep')['logradouro']
            bairro = self.localizeCep('cep')['bairro']
            localidade = self.localizeCep('cep')['localidade']

            self.searchState.setText(uf)
            self.searchCity.setText(localidade)
            self.searchStreet.setText(logradouro)
            self.searchNeighborhood.setText(bairro)
        
        except:
            self.searchState.setText('')
            self.searchCity.setText('')
            self.searchStreet.setText('')
            self.searchNeighborhood.setText('')

class changeUserWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadDatabase(self)

        self.changeUserWindowLabel()

        self.changeUserWindowEntrys()

        self.changeUserWindowButton()

        self.loadChangeUserWindow()

    def loadChangeUserWindow(self):
        # configurations #
        self.setWindowTitle('U n p a c k - A c c o u n t')
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

    def changeUserWindowLabel(self):
        # naming the page with a label #
        self.accountLabel = QLabel(self)
        self.accountLabel.setText('A c c o u n t')
        self.accountLabel.setAlignment(Qt.AlignCenter)
        self.accountLabel.setGeometry(150, 20, 200, 50)
        self.accountLabel.setStyleSheet(
            '''
                background: none;
                color: whitesmoke;
                font: bold 20px Dejavu, Sans, Mono;
            '''
        )
        self.accountLabel.show()

    def changeUserWindowEntrys(self):

        self.changeNameEntry = QLineEdit(self)
        self.changeNameEntry.setAlignment(Qt.AlignCenter)
        self.changeNameEntry.setPlaceholderText('Name')
        self.changeNameEntry.setMaxLength(50)
        self.changeNameEntry.setGeometry(150, 90, 200, 40)
        self.changeNameEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0 ,0);
                color: whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.changeNameEntry.show()

        self.changeEmailEntry = QLineEdit(self)
        self.changeEmailEntry.setAlignment(Qt.AlignCenter)
        self.changeEmailEntry.setPlaceholderText('E-mail')
        self.changeEmailEntry.setMaxLength(50)
        self.changeEmailEntry.setGeometry(150, 155, 200, 40)
        self.changeEmailEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0 ,0);
                color: whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.changeEmailEntry.show()

        self.changePasswordEntry = QLineEdit(self)
        self.changePasswordEntry.setAlignment(Qt.AlignCenter)
        self.changePasswordEntry.setPlaceholderText('Password')
        self.changePasswordEntry.setMaxLength(6)
        self.changePasswordEntry.setGeometry(150, 220, 200, 40)
        self.changePasswordEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0 ,0);
                color: whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )

    def changeUserWindowButton(self):
        self.changeButton = QPushButton(self)
        self.changeButton.setText('C H A N G E')
        self.changeButton.setGeometry(150, 285, 200, 50)
        self.changeButton.setStyleSheet(
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
        self.changeButton.clicked.connect(lambda: (self.insertChangedUser(), self.close()))
        self.changeButton.show()

    def insertChangedUser(self):
        
        # taking the text of the cadastre entrys #
        self.getname = self.changeNameEntry.text()
        self.getemail = self.changeEmailEntry.text()
        self.getpassword = self.changePasswordEntry.text()

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
        print('Cadastre OK!')

class purchaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadDatabase(self)

        self.purchaseWindowLabel()

        self.purchaseWindowEntrys()

        self.purchaseWindowButton()

        self.loadPurchaseWindow()

    def loadPurchaseWindow(self):
        # configurations #
        self.setWindowTitle('U n p a c k - P u r c h a s e')
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

    def purchaseWindowLabel(self):
        # naming the page with a label #
        self.purchaseLabel = QLabel(self)
        self.purchaseLabel.setText('B U Y')
        self.purchaseLabel.setAlignment(Qt.AlignCenter)
        self.purchaseLabel.setGeometry(150, 20, 200, 50)
        self.purchaseLabel.setStyleSheet(
            '''
                background: none;
                color: whitesmoke;
                font: bold 20px Dejavu, Sans, Mono;
            '''
        )
        self.purchaseLabel.show()

    def purchaseWindowEntrys(self):

        self.purchaseNameEntry = QLineEdit(self)
        self.purchaseNameEntry.setAlignment(Qt.AlignCenter)
        self.purchaseNameEntry.setPlaceholderText('Name')
        self.purchaseNameEntry.setMaxLength(50)
        self.purchaseNameEntry.setGeometry(40, 90, 200, 40)
        self.purchaseNameEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0 ,0);
                color: whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.purchaseNameEntry.show()

        self.purchaseEmailEntry = QLineEdit(self)
        self.purchaseEmailEntry.setAlignment(Qt.AlignCenter)
        self.purchaseEmailEntry.setPlaceholderText('E-mail')
        self.purchaseEmailEntry.setMaxLength(50)
        self.purchaseEmailEntry.setGeometry(260, 90, 200, 40)
        self.purchaseEmailEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0 ,0);
                color: whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.purchaseEmailEntry.show()

        self.purchaseCpfEntry = QLineEdit(self)
        self.purchaseCpfEntry.setAlignment(Qt.AlignCenter)
        self.purchaseCpfEntry.setPlaceholderText('CPF')
        self.purchaseCpfEntry.setMaxLength(13)
        self.purchaseCpfEntry.setGeometry(40, 155, 200, 40)
        self.purchaseCpfEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0 ,0);
                color: whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.purchaseCpfEntry.show()

        self.purchaseCepEntry = QLineEdit(self)
        self.purchaseCepEntry.setAlignment(Qt.AlignCenter)
        self.purchaseCepEntry.setPlaceholderText('CEP')
        self.purchaseCepEntry.setMaxLength(8)
        self.purchaseCepEntry.setGeometry(260, 155, 200, 40)
        self.purchaseCepEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0 ,0);
                color: whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.purchaseCepEntry.show()

        self.purchasePasswordEntry = QLineEdit(self)
        self.purchasePasswordEntry.setAlignment(Qt.AlignCenter)
        self.purchasePasswordEntry.setPlaceholderText('Password')
        self.purchasePasswordEntry.setMaxLength(6)
        self.purchasePasswordEntry.setGeometry(40, 220, 200, 40)
        self.purchasePasswordEntry.setStyleSheet(
            '''
                background: rgba(0, 0, 0 ,0);
                color: whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.purchasePasswordEntry.show()

        self.purchaseCardNumberEntry = QLineEdit(self)
        self.purchaseCardNumberEntry.setAlignment(Qt.AlignCenter)
        self.purchaseCardNumberEntry.setPlaceholderText('Card Number')
        self.purchaseCardNumberEntry.setMaxLength(10)
        self.purchaseCardNumberEntry.setGeometry(260, 220, 200, 40)
        self.purchaseCardNumberEntry.setStyleSheet(
            '''
                background: #111111;
                color: whitesmoke;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            '''
        )
        self.purchaseCardNumberEntry.show()

    def purchaseWindowButton(self):
        self.purchaseButton = QPushButton(self)
        self.purchaseButton.setText('F I N I S H')
        self.purchaseButton.setGeometry(150, 300, 200, 50)
        self.purchaseButton.setStyleSheet(
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
        self.purchaseButton.clicked.connect(lambda: (self.insertPurchaseData(), productPurchaseInfo()))
        self.purchaseButton.show()

    def insertPurchaseData(self):
        self.getname = self.purchaseNameEntry.text()
        self.getemail = self.purchaseEmailEntry.text()
        self.getpassword = self.purchasePasswordEntry.text()
        self.getcpf = self.purchaseCpfEntry.text()
        self.getcep = self.purchaseCepEntry.text()
        self.getcard = self.purchaseCardNumberEntry.text()

        self.cursor.execute(
                '''
                    insert into userpurchase (name, email, password, cpf, cep, card) values (?, ?, ?, ?, ?, ?);
                ''',
            (
                self.getname,
                self.getemail,
                self.getpassword,
                self.getcpf,
                self.getcep,
                self.getcard
            )
        )
        self.connection.commit()
        print('works')

class locationWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadDatabase(self)

        self.locationWindowLabels()

        self.purchaseWindowButton()

        self.loadLocationWindow()

    def loadLocationWindow(self):
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

    def locationWindowLabels(self):
        for row in self.cursor.fetchall():
            print(row)

        self.cursor.execute('select local from productlocation where id="1"')
        local = self.cursor.fetchall()

        self.cursor.execute('select date from productlocation where id="1"')
        date = self.cursor.fetchall()

        self.cursor.execute('select hour from productlocation where id="1"')
        hour = self.cursor.fetchall()

        daylocal = str(local)[3:-4]
        daydate = str(date)[3:-4]
        dayhour = str(hour)[3:-4]

        # naming the page with a label #
        self.locationLabel = QLabel(self)
        self.locationLabel.setText('L O C A L')
        self.locationLabel.setAlignment(Qt.AlignCenter)
        self.locationLabel.setGeometry(150, 20, 200, 50)
        self.locationLabel.setStyleSheet(
            '''
                background: none;
                color: whitesmoke;
                font: bold 20px Dejavu, Sans, Mono;
            '''
        )
        self.locationLabel.show()

        self.systemLocationLabel = QLabel(self)
        self.systemLocationLabel.setGeometry(10, 80, 480, 310)
        self.systemLocationLabel.setAlignment(Qt.AlignCenter)
        self.systemLocationLabel.setText(
            f'''
                The product arrived in: <u>{daylocal}</u>
                <br><br>
                In the date: <u>{daydate}</u>
                <br><br>
                On the hour: <u>{dayhour}</u>
                <br><br>
            '''
        )
        self.systemLocationLabel.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: whitesmoke;
                    font: bold 14px Dejavu, Sans, Mono;
                    border: 2px solid blueviolet;
                    border-radius: 7px;
                }
            '''
        )
        self.systemLocationLabel.show()

    def purchaseWindowButton(self):
        self.purchaseButton = QPushButton()
        self.purchaseButton.clicked.connect(lambda: (self.close()))

class productPurchaseInfo(QWidget):
    def __init__(self):
        super().__init__()
        loadDatabase(self)

        self.cursor.execute('update productinfo set quantity=quantity-1')

        self.loadProductPurchaseWindow()

        self.productPurchaseInfoLabels()

        self.purchaseWindowButton()
        
    def loadProductPurchaseWindow(self):
        # configurations #
        self.setWindowTitle('U n p a c k - P u r c h a s e  I n f o')
        self.setWindowIcon(QtGui.QIcon('images/bluevioleticons/logo.png'))
        self.setStyleSheet('background: #111111;')
        self.setMaximumSize(300, 400)
        self.setMinimumSize(300, 400)

        # center the window #
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.show()

    def productPurchaseInfoLabels(self):
        # naming the page with a label #
        self.productInfoLabel = QLabel(self)
        self.productInfoLabel.setText('I N F O')
        self.productInfoLabel.setAlignment(Qt.AlignCenter)
        self.productInfoLabel.setGeometry(0, 0, 300, 50)
        self.productInfoLabel.setStyleSheet(
            '''
                background: none;
                color: whitesmoke;
                font: bold 20px Dejavu, Sans, Mono;
            '''
        )
        self.productInfoLabel.show()
        #self.getclimate = self.climateEntry.text()
        
        self.cursor.execute('select quantity from productinfo where id="1"')
        quantity = self.cursor.fetchall()
        
        self.cursor.execute('select price from productinfo where id="1"')
        price = self.cursor.fetchall()

        self.cursor.execute('select name from userdata where id="1"')
        oname = self.cursor.fetchall()
        
        self.cursor.execute('select email from userdata where id="1"')
        omail = self.cursor.fetchall()
        
        self.cursor.execute('select cep from userpurchase where id="1"')
        ocep = self.cursor.fetchall()
        
        self.cursor.execute('select cpf from userpurchase where id="1"')
        ocpf = self.cursor.fetchall()

        productname = str(oname)[3:-4] 
        productquantity = str(quantity)[3:-4]
        productprice = str(price)[3:-4]
        ownername = str(oname)[3:-4]
        owneremail = str(omail)[3:-4]
        ownercep = str(ocep)[3:-4]
        ownercpf = str(ocpf)[3:-4]

        self.productInfoLabel = QLabel(self)
        self.productInfoLabel.setGeometry(10, 80, 480, 310)
        self.productInfoLabel.setAlignment(Qt.AlignLeft)
        self.productInfoLabel.setText(
            f'''
                Product Name: <u>{productname}</u>
                <br><br>
                Product Quantity: <u>{productquantity}</u>
                <br><br>
                Product Price: <u>{productprice}</u>
                <br><br>
                Owner Name: <u>{ownername}</u>
                <br><br>
                Owner E-mail: <u>{owneremail}</u>
                <br><br>
                Owner CEP: <u>{ownercep}</u>
                <br><br>
                Owner CPF: <u>{ownercpf}</u>
                <br><br>
            '''
        )
        self.productInfoLabel.setStyleSheet(
            '''
                background: none;
                color: whitesmoke;
                font: bold 12px Dejavu, Sans, Mono;
            '''
        )
        self.productInfoLabel.show()

    def purchaseWindowButton(self):
        self.purchaseButton = QPushButton()
        self.purchaseButton.clicked.connect(lambda: (self.close()))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    load = mainWindow()
    sys.exit(app.exec())
