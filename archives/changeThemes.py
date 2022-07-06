def darkMode(self):

    welcomeFrameDarkTheme(self)

    productsFrameDarkTheme(self)

    infoFrameDarkTheme(self)

    searchFrameDarkTheme(self)

    locationFrameDarkTheme(self)

    mensageFrameDarkTheme(self)

    settingsFrameDarkTheme(self)

def whiteMode(self):

    welcomeFrameWhiteTheme(self)

    productsFrameWhiteTheme(self)

    infoFrameWhiteTheme(self)

    searchFrameWhiteTheme(self)

    locationFrameWhiteTheme(self)

    mensageFrameWhiteTheme(self)

    settingsFrameWhiteTheme(self)

def contrastMode(self):

    welcomeFrameContrastTheme(self)

    productsFrameContrastTheme(self)

    infoFrameContrastTheme(self)

    searchFrameContrastTheme(self)

    locationFrameContrastTheme(self)

    mensageFrameContrastTheme(self)

    settingsFrameContrastTheme(self)

def welcomeFrameContrastTheme(self):
    self.myWelcomeFrame.setStyleSheet(
        '''
            QFrame{
                background-color: black;
            }
        '''
    )

    self.enterpriseNameLabel.setStyleSheet(
        '''
            QLabel{
                color: yellow;
                font: bold 60px Dejavu, Sans, Mono;
            }
        '''
    )

    self.userLogoButton.setStyleSheet(
        '''
            QPushButton{
                background: rgba(0, 0, 0, 0);
                background-image: url(images/yellowicons/user.png);
                background-repeat: no-repeat;
                background-position: center;
            }
        '''
    )

    self.randomMensageLabel.setStyleSheet(
        '''
            QLabel{
                color: white;
                font: 15px Dejavu, Sans, Mono;
            }
        '''
    )

def productsFrameContrastTheme(self):
    self.myProductsFrame.setStyleSheet(
        '''
            QFrame{
                background-color: black;
            }
        '''
    )

    self.titleLabel.setStyleSheet(
        '''
            QLabel{
                border-left: none;
                background: none;
                color: white;
                font: bold 25px Dejavu, Sans, Mono;
                border-radius: none;
                border-bottom: 2px solid white;
            }
        '''
    )

    self.scrollArea.setStyleSheet(
            '''
                color: white;
                background-color: black;
                border: none;
            '''
        )

def infoFrameContrastTheme(self):
    self.myInfoFrame.setStyleSheet(
        '''
            QFrame{
                border: none;
                background-color: black;
            }
        '''
    )

    self.imageLabel.setStyleSheet(
        '''
            QLabel{
                background-image: url(images/productsimages/monalisa.png);
                background-position: center;
                background-repeat: no-repeat;
            }
        '''
    )
    
    self.infoLabel.setStyleSheet(
        '''
            QLabel{
                border-left: none;
                color: white;
                font: 15px Dejavu, Sans, Mono;
                background: none;
            }
        '''
    )
        
    self.unitLabel.setStyleSheet(
        '''
            QLabel{
                border-left: none;
                color: white;
                font: 15px Dejavu, Sans, Mono;
                background: none;
            }
        '''
    )

    self.closeInfoFrameButton.setStyleSheet(
        '''
            QPushButton{
                background-color: yellow;
                border-radius: 5px;
                font: 20px bold Dejavu, Sans, Mono;
                color: black;
            }

            QPushButton:hover{
                background-color: #f7d917;
            }
            
            QPushButton:pressed{
                background-color: rgba(0, 0, 0, 0);
                border: 2px solid yellow;
                color: white;
            }
        '''
    )

    self.buyProductButton.setStyleSheet(
        '''
            QPushButton{
                font: 12px bold Dejavu, Sans, Mono;
                background-color: yellow;
                border-radius: 5px;
                color: black;
            }

            QPushButton:hover{
                background-color: #f7d917;
            }
            
            QPushButton:pressed{
                background-color: rgba(0, 0, 0, 0);
                border: 2px solid yellow;
                color: white;
            }
        '''
    )

def searchFrameContrastTheme(self):
    self.mySearchFrame.setStyleSheet(
        '''
            QFrame{
                background-color: black;
            }
        '''
    )

    self.searchLabel.setStyleSheet(
        '''
            QLabel{
                border-left: none;
                background: none;
                color: white;
                font: bold 25px Dejavu, Sans, Mono;
                border-radius: none;
                border-bottom: 2px solid white;
            }
        '''
    )
    self.typeCepEntry.setStyleSheet(
            '''
                QLineEdit{
                    background: rgba(0, 0, 0 ,0);
                    color: white;
                    border: 2px solid yellow;
                    border-radius: 7px;
                    font: 14px Dejavu, Sans, Mono;
                }
            '''
    )
    self.searchState.setStyleSheet(
            '''
                QLineEdit{
                    background: rgba(0, 0, 0 ,0);
                    color: whitesmoke;
                    border-bottom: 2px solid yellow;
                    border-radius: 0px;
                    font: 14px Dejavu, Sans, Mono;
                }
            '''
        )
    self.searchCity.setStyleSheet(
        '''
            QLineEdit{
                background: rgba(0, 0, 0 ,0);
                color: white;
                border-bottom: 2px solid yellow;
                border-radius: 0px;
                font: 14px Dejavu, Sans, Mono;
            }
        '''
    )
    self.searchStreet.setStyleSheet(
        '''
            QLineEdit{
                background: rgba(0, 0, 0 ,0);
                color: white;
                border-bottom: 2px solid yellow;
                border-radius: 0px;
                font: 14px Dejavu, Sans, Mono;
            }
        '''
    )
    self.searchNeighborhood.setStyleSheet(
        '''
            QLineEdit{
                background: rgba(0, 0, 0 ,0);
                color: white;
                border-bottom: 2px solid yellow;
                border-radius: 0px;
                font: 14px Dejavu, Sans, Mono;
            }
        '''
    )
    self.searchCepButton.setStyleSheet(
        '''
            QPushButton{
                font: 12px bold Dejavu, Sans, Mono;
                background-color: yellow;
                border-radius: 5px;
                color: black;
            }

            QPushButton:hover{
                background-color: #f7d917;
            }
            
            QPushButton:pressed{
                background-color: rgba(0, 0, 0, 0);
                border: 2px solid yellow;
                color: white;
            }
        '''
    )

def locationFrameContrastTheme(self):
    self.myLocationFrame.setStyleSheet(
        '''
            QFrame{
                background-color: black;
            }
        '''
    )

    self.localizationLabel.setStyleSheet(
        '''
            QLabel{
                border-left: none;
                background: none;
                color: white;
                font: bold 25px Dejavu, Sans, Mono;
                border-radius: none;
                border-bottom: 2px solid white;
            }
        '''
    )

    self.codeEntry.setStyleSheet(
        '''
            QLineEdit{
                background: rgba(0, 0, 0 ,0);
                color: white;
                border: 2px solid yellow;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            }
        '''
    )

    self.searchCodeButton.setStyleSheet(
        '''
            QPushButton{
                font: 12px bold Dejavu, Sans, Mono;
                background-color: yellow;
                border-radius: 5px;
                color: black;
            }

            QPushButton:hover{
                background-color: #f7d917;
            }
            
            QPushButton:pressed{
                background-color: rgba(0, 0, 0, 0);
                border: 2px solid yellow;
                color: white;
            }
        '''
    )

    self.searchClimateButton.setStyleSheet(
        '''
            QPushButton{
                font: 12px bold Dejavu, Sans, Mono;
                background-color: yellow;
                border-radius: 25px;
                color: black;
            }

            QPushButton:hover{
                background-color: #f7d917;
            }
            
            QPushButton:pressed{
                background-color: rgba(0, 0, 0, 0);
                border: 2px solid yellow;
                color: white;
            }
        '''
    )

    self.deleteClimateButton.setStyleSheet(
        '''
            QPushButton{
                font: 12px bold Dejavu, Sans, Mono;
                background-color: yellow;
                border-radius: 10px;
                color: black;
            }

            QPushButton:hover{
                background-color: #f7d917;
            }
            
            QPushButton:pressed{
                background-color: rgba(0, 0, 0, 0);
                border: 2px solid yellow;
                color: white;
            }
        '''
    )

    self.climateLabel.setStyleSheet(
        '''
            QLabel{
                border-left: none;
                background: none;
                color: white;
                font: bold 14px Dejavu, Sans, Mono;
                border: 2px solid yellow;
                border-radius: 7px;
            }
        '''
    )

def mensageFrameContrastTheme(self):
    self.myMensageFrame.setStyleSheet(
        '''
            QFrame{
                background-color: black;
            }
        '''
    )

    self.mensageLabel.setStyleSheet(
        '''
            QLabel{
                border-left: none;
                background: none;
                color: white;
                font: bold 25px Dejavu, Sans, Mono;
                border-radius: none;
                border-bottom: 2px solid white;
            }
        '''
    )

    self.mensageBox.setStyleSheet(
        '''
            QPlainTextEdit{
                background: rgba(0, 0, 0 ,0);
                color: whitesmoke;
                border: 2px solid yellow;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            }
        '''
    )

    self.sendMensageButton.setStyleSheet(
        '''
            QPushButton{
                font: 12px bold Dejavu, Sans, Mono;
                background-color: yellow;
                border-radius: 5px;
                color: black;
            }

            QPushButton:hover{
                background-color: #f7d917;
            }
            
            QPushButton:pressed{
                background-color: rgba(0, 0, 0, 0);
                border: 2px solid yellow;
                color: white;
            }
        '''
    )

def settingsFrameContrastTheme(self):
    self.setStyleSheet(
        '''
            QMainWindow{
                background-color: black;
            }
        '''
    )

    self.mySettingsFrame.setStyleSheet(
        '''
            QFrame{
                background-color: black;
            }
        '''
    )

    self.settingsLabel.setStyleSheet(
        '''
            QLabel{
                border-left: none;
                background: none;
                color: white;
                font: bold 25px Dejavu, Sans, Mono;
                border-radius: none;
                border-bottom: 2px solid white;
            }
        '''
    )

    self.themesLabel.setStyleSheet(
        '''
            QLabel{
                border-left: none;
                background: none;
                color: white;
                font: 14px Dejavu, Sans, Mono;
                border-radius: none;
                border-bottom: 1px solid white;
            }
        '''
    )

    self.fontsLabel.setStyleSheet(
        '''
            QLabel{
                border-left: none;
                background: none;
                color: white;
                font: 14px Dejavu, Sans, Mono;
                border-radius: none;
                border-bottom: 1px solid white;
            }
        '''
    )

    self.arialFont.setStyleSheet(
        '''
            QRadioButton{
                background: rgba(0, 0, 0, 0);
                font: 14px Ubuntu Mono;
                color: white;
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

    self.helveticaFont.setStyleSheet(
        '''
            QRadioButton{
                background: rgba(0, 0, 0, 0);
                font: 14px Ubuntu Mono;
                color: white;
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

    self.ubuntuMonoFont.setStyleSheet(
        '''
            QRadioButton{
                background: rgba(0, 0, 0, 0);
                font: 14px Ubuntu Mono;
                color: white;
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

    self.logoButton.setStyleSheet(

        '''
            QPushButton{
                border: none;
                background-image: url(images/whiteicons/logo.png);
                background-repeat: no-repeat;
                background-position: center;
            }

            QPushButton:hover{
                border-left: 2px solid yellow;
                background-image: url(images/yellowicons/logo.png);
            }

            QPushButton:pressed{
                background-color: yellow;
                background-image: url(images/blackicons/logo.png);
            }
        '''
    )

    self.homeButton.setStyleSheet(

        '''
            QPushButton{
                border: none;
                background-image: url(images/whiteicons/home.png);
                background-repeat: no-repeat;
                background-position: center;
            }

            QPushButton:hover{
                border-left: 2px solid yellow;
                background-image: url(images/yellowicons/home.png);
            }

            QPushButton:pressed{
                background-color: yellow;
                background-image: url(images/blackicons/home.png);
            }
        '''
    )

    self.searchButton.setStyleSheet(

        '''
            QPushButton{
                border: none;
                background-image: url(images/whiteicons/search.png);
                background-repeat: no-repeat;
                background-position: center;
            }

            QPushButton:hover{
                border-left: 2px solid yellow;
                background-image: url(images/yellowicons/search.png);
            }

            QPushButton:pressed{
                background-color: yellow;
                background-image: url(images/blackicons/search.png);
            }
        '''
    )

    self.markerButton.setStyleSheet(

        '''
            QPushButton{
                border: none;
                background-image: url(images/whiteicons/marker.png);
                background-repeat: no-repeat;
                background-position: center;
            }

            QPushButton:hover{
                border-left: 2px solid yellow;
                background-image: url(images/yellowicons/marker.png);
            }

            QPushButton:pressed{
                background-color: yellow;
                background-image: url(images/blackicons/marker.png);
            }
        '''
    )

    self.mensageButton.setStyleSheet(

        '''
            QPushButton{
                border: none;
                background-image: url(images/whiteicons/mensage.png);
                background-repeat: no-repeat;
                background-position: center;
            }

            QPushButton:hover{
                border-left: 2px solid yellow;
                background-image: url(images/yellowicons/mensage.png);
            }

            QPushButton:pressed{
                background-color: yellow;
                background-image: url(images/blackicons/mensage.png);
            }
        '''
    )

    self.settingsButton.setStyleSheet(

        '''
            QPushButton{
                border: none;
                background-image: url(images/whiteicons/settings.png);
                background-repeat: no-repeat;
                background-position: center;
            }

            QPushButton:hover{
                border-left: 2px solid yellow;
                background-image: url(images/yellowicons/settings.png);
            }

            QPushButton:pressed{
                background-color: yellow;
                background-image: url(images/blackicons/settings.png);
            }
        '''
    )

def welcomeFrameDarkTheme(self):
    self.myWelcomeFrame.setStyleSheet(
        '''
            QFrame{
                background-color: #111111;
            }
        '''
    )

    self.enterpriseNameLabel.setStyleSheet(
        '''
            QLabel{
                color: blueviolet;
                font: bold 60px Dejavu, Sans, Mono;
            }
        '''
    )

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

    self.randomMensageLabel.setStyleSheet(
        '''
            QLabel{
                color: whitesmoke;
                font: 15px Dejavu, Sans, Mono;
            }
        '''
    )

def productsFrameDarkTheme(self):
    self.myProductsFrame.setStyleSheet(
        '''
            QFrame{
                background-color: #111111;
            }
        '''
    )

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
    
    self.scrollArea.setStyleSheet(
        '''
            color: whitesmoke;
            background-color: #111111;
            border: none;
        '''
    )

def infoFrameDarkTheme(self):
    self.myInfoFrame.setStyleSheet(
        '''
            QFrame{
                background-color: #111111;
            }
        '''
    )
    
    self.infoLabel.setStyleSheet(
        '''
            QLabel{
                color: whitesmoke;
                font: 15px Dejavu, Sans, Mono;
                background: none;
            }
        '''
    )
        
    self.unitLabel.setStyleSheet(
        '''
            QLabel{
                color: whitesmoke;
                font: 15px Dejavu, Sans, Mono;
                background: none;
            }
        '''
    )

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
                background-color: rgba(0, 0, 0, 0);
                border: 2px solid blueviolet;
            }
        '''
    )

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
                background-color: rgba(0, 0, 0, 0);
                border: 2px solid blueviolet;
            }
        '''
    )

def searchFrameDarkTheme(self):
    self.mySearchFrame.setStyleSheet(
        '''
            QFrame{
                background-color: #111111;
            }
        '''
    )

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

def locationFrameDarkTheme(self):
    self.myLocationFrame.setStyleSheet(
        '''
            QFrame{
                background-color: #111111;
            }
        '''
    )

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

def mensageFrameDarkTheme(self):
    self.myMensageFrame.setStyleSheet(
        '''
            QFrame{
                background-color: #111111;
            }
        '''
    )

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

def settingsFrameDarkTheme(self):
    self.setStyleSheet(
        '''
            QMainWindow{
                background-color: #151515;
            }
        '''
    )

    self.mySettingsFrame.setStyleSheet(
        '''
            QFrame{
                background-color: #111111;
            }
        '''
    )

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

    self.arialFont.setStyleSheet(
        '''
            QRadioButton{
                background: rgba(0, 0, 0, 0);
                font: 14px Ubuntu Mono;
                color: whitesmoke;
            }

            QRadioButton::indicator{
                border: 1px solid whitesmoke;
                border-radius: 2px;
            }

            QRadioButton::indicator::checked{
                background: blueviolet;
                background-position: center;
            }
        '''
    )

    self.helveticaFont.setStyleSheet(
        '''
            QRadioButton{
                background: rgba(0, 0, 0, 0);
                font: 14px Ubuntu Mono;
                color: whitesmoke;
            }

            QRadioButton::indicator{
                border: 1px solid whitesmoke;
                border-radius: 2px;
            }

            QRadioButton::indicator::checked{
                background: blueviolet;
                background-position: center;
            }
        '''
    )

    self.ubuntuMonoFont.setStyleSheet(
        '''
            QRadioButton{
                background: rgba(0, 0, 0, 0);
                font: 14px Ubuntu Mono;
                color: whitesmoke;
            }

            QRadioButton::indicator{
                border: 1px solid whitesmoke;
                border-radius: 2px;
            }

            QRadioButton::indicator::checked{
                background: blueviolet;
                background-position: center;
            }
        '''
    )

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
                background-color: whitesmoke;
            }
        '''
    )

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
                background-color: whitesmoke;
            }
        '''
    )

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
                background-color: whitesmoke;
            }
        '''
    )

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
                background-color: whitesmoke;
            }
        '''
    )

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
                background-color: whitesmoke;
            }
        '''
    )

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
                background-color: whitesmoke;
            }
        '''
    )

def welcomeFrameWhiteTheme(self):
    self.myWelcomeFrame.setStyleSheet(
        '''
            QFrame{
                background-color: rgb(245, 245, 245);
            }
        '''
    )

    self.enterpriseNameLabel.setStyleSheet(
        '''
            QLabel{
                color: blueviolet;
                font: bold 60px Dejavu, Sans, Mono;
            }
        '''
    )

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

    self.randomMensageLabel.setStyleSheet(
        '''
            QLabel{
                color: #111111;
                font: 15px Dejavu, Sans, Mono;
            }
        '''
    )

def productsFrameWhiteTheme(self):
    self.myProductsFrame.setStyleSheet(
        '''
            QFrame{
                background-color: rgb(245, 245, 245);
            }
        '''
    )

    self.titleLabel.setStyleSheet(
        '''
            QLabel{
                background: none;
                color: #111111;
                font: bold 25px Dejavu, Sans, Mono;
                border-radius: none;
                border-bottom: 2px solid #111111;
            }
        '''
    )

    self.scrollArea.setStyleSheet(
            '''
                color: #111111;
                background-color: whitesmoke;
                border: none;
            '''
        )

def infoFrameWhiteTheme(self):
    self.myInfoFrame.setStyleSheet(
        '''
            QFrame{
                background-color: rgb(230, 230, 230);
            }
        '''
    )
    
    self.infoLabel.setStyleSheet(
        '''
            QLabel{
                color: #111111;
                font: 15px Dejavu, Sans, Mono;
                background: none;
            }
        '''
    )
        
    self.unitLabel.setStyleSheet(
        '''
            QLabel{
                color: #111111;
                font: 15px Dejavu, Sans, Mono;
                background: none;
            }
        '''
    )

    self.closeInfoFrameButton.setStyleSheet(
        '''
            QPushButton{
                background-color: blueviolet;
                border-radius: 5px;
                font: 20px bold Dejavu, Sans, Mono;
                color: #111111;
            }

            QPushButton:hover{
                background-color: rgb(128, 33, 216);
            }
            
            QPushButton:pressed{
                background-color: rgba(0, 0, 0, 0);
                border: 2px solid blueviolet;
            }
        '''
    )

    self.buyProductButton.setStyleSheet(
        '''
            QPushButton{
                font: 12px bold Dejavu, Sans, Mono;
                background-color: blueviolet;
                border-radius: 5px;
                color: #111111;
            }

            QPushButton:hover{
                background-color: rgb(128, 33, 216);
            }
            
            QPushButton:pressed{
                background-color: rgba(0, 0, 0, 0);
                border: 2px solid blueviolet;
            }
        '''
    )

def searchFrameWhiteTheme(self):
    self.mySearchFrame.setStyleSheet(
        '''
            QFrame{
                background-color: rgb(245, 245, 245);
            }
        '''
    )

    self.searchLabel.setStyleSheet(
        '''
            QLabel{
                background: none;
                color: #111111;
                font: bold 25px Dejavu, Sans, Mono;
                border-radius: none;
                border-bottom: 2px solid #111111;
            }
        '''
    )
    self.typeCepEntry.setStyleSheet(
            '''
                QLineEdit{
                    background: rgba(0, 0, 0 ,0);
                    color: #111111;
                    border: 2px solid blueviolet;
                    border-radius: 7px;
                    font: 14px Dejavu, Sans, Mono;
                }
            '''
            )
    self.searchState.setStyleSheet(
            '''
                QLineEdit{
                    background: rgba(0, 0, 0 ,0);
                    color: #111111;
                    border-bottom: 2px solid #111111;
                    border-radius: 0px;
                    font: 14px Dejavu, Sans, Mono;
                }
            '''
        )
    self.searchCity.setStyleSheet(
        '''
            QLineEdit{
                background: rgba(0, 0, 0 ,0);
                color: #111111;
                border-bottom: 2px solid #111111;
                border-radius: 0px;
                font: 14px Dejavu, Sans, Mono;
            }
        '''
    )
    self.searchStreet.setStyleSheet(
        '''
            QLineEdit{
                background: rgba(0, 0, 0 ,0);
                color: #111111;
                border-bottom: 2px solid #111111;
                border-radius: 0px;
                font: 14px Dejavu, Sans, Mono;
            }
        '''
    )
    self.searchNeighborhood.setStyleSheet(
        '''
            QLineEdit{
                background: rgba(0, 0, 0 ,0);
                color: #111111;
                border-bottom: 2px solid #111111;
                border-radius: 0px;
                font: 14px Dejavu, Sans, Mono;
            }
        '''
    )
    self.searchCepButton.setStyleSheet(
        '''
            QPushButton{
                font: 12px Dejavu, Sans, Mono;
                background-color: blueviolet;
                border-radius: 7px;
                color: #111111;
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

def locationFrameWhiteTheme(self):
    self.myLocationFrame.setStyleSheet(
        '''
            QFrame{
                background-color: rgb(245, 245, 245);
            }
        '''
    )

    self.localizationLabel.setStyleSheet(
        '''
            QLabel{
                background: none;
                color: #111111;
                font: bold 25px Dejavu, Sans, Mono;
                border-radius: none;
                border-bottom: 2px solid #111111;
            }
        '''
    )

    self.codeEntry.setStyleSheet(
        '''
            QLineEdit{
                background: rgba(0, 0, 0 ,0);
                color: #111111;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            }
        '''
    )

    self.searchCodeButton.setStyleSheet(
        '''
            QPushButton{
                font: 20px Dejavu, Sans, Mono;
                background-color: blueviolet;
                border-radius: 7px;
                color: #111111;
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

    self.searchClimateButton.setStyleSheet(
        '''
            QPushButton{
                font: 20px Dejavu, Sans, Mono;
                background-color: blueviolet;
                border-radius: 25px;
                color: #111111;
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

    self.deleteClimateButton.setStyleSheet(
        '''
            QPushButton{
                font: 12px Dejavu, Sans, Mono;
                background-color: blueviolet;
                border-radius: 10px;
                color: #111111;
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

    self.climateLabel.setStyleSheet(
        '''
            QLabel{
                background: none;
                color: #111111;
                font: bold 14px Dejavu, Sans, Mono;
                border: 2px solid blueviolet;
                border-radius: 7px;
            }
        '''
    )

def mensageFrameWhiteTheme(self):
    self.myMensageFrame.setStyleSheet(
        '''
            QFrame{
                background-color: rgb(245, 245, 245);
            }
        '''
    )

    self.mensageLabel.setStyleSheet(
        '''
            QLabel{
                background: none;
                color: #111111;
                font: bold 25px Dejavu, Sans, Mono;
                border-radius: none;
                border-bottom: 2px solid #111111;
            }
        '''
    )

    self.mensageBox.setStyleSheet(
        '''
            QPlainTextEdit{
                background: rgba(0, 0, 0 ,0);
                color: #111111;
                border: 2px solid blueviolet;
                border-radius: 7px;
                font: 14px Dejavu, Sans, Mono;
            }
        '''
    )

    self.sendMensageButton.setStyleSheet(
        '''
            QPushButton{
                background: blueviolet;
                border: 2px solid blueviolet;
                color: #111111;
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

def settingsFrameWhiteTheme(self):
    self.setStyleSheet(
        '''
            QMainWindow{
                background-color: rgb(230, 230, 230);
            }
        '''
    )

    self.mySettingsFrame.setStyleSheet(
        '''
            QFrame{
                background-color: rgb(245, 245, 245);
            }
        '''
    )

    self.settingsLabel.setStyleSheet(
        '''
            QLabel{
                background: none;
                color: #111111;
                font: bold 25px Dejavu, Sans, Mono;
                border-radius: none;
                border-bottom: 2px solid #111111;
            }
        '''
    )

    self.themesLabel.setStyleSheet(
        '''
            QLabel{
                background: none;
                color: #111111;
                font: 14px Dejavu, Sans, Mono;
                border-radius: none;
                border-bottom: 1px solid #111111;
            }
        '''
    )

    self.fontsLabel.setStyleSheet(
        '''
            QLabel{
                background: none;
                color: #111111;
                font: 14px Dejavu, Sans, Mono;
                border-radius: none;
                border-bottom: 1px solid #111111;
            }
        '''
    )

    self.arialFont.setStyleSheet(
        '''
            QRadioButton{
                background: rgba(0, 0, 0, 0);
                font: 14px Ubuntu Mono;
                color: #111111;
            }

            QRadioButton::indicator{
                border: 1px solid #111111;
                border-radius: 2px;
            }

            QRadioButton::indicator::checked{
                background: blueviolet;
                background-position: center;
            }
        '''
    )

    self.helveticaFont.setStyleSheet(
        '''
            QRadioButton{
                background: rgba(0, 0, 0, 0);
                font: 14px Ubuntu Mono;
                color: #111111;
            }

            QRadioButton::indicator{
                border: 1px solid #111111;
                border-radius: 2px;
            }

            QRadioButton::indicator::checked{
                background: blueviolet;
                background-position: center;
            }
        '''
    )

    self.ubuntuMonoFont.setStyleSheet(
        '''
            QRadioButton{
                background: rgba(0, 0, 0, 0);
                font: 14px Ubuntu Mono;
                color: #111111;
            }

            QRadioButton::indicator{
                border: 1px solid #111111;
                border-radius: 2px;
            }

            QRadioButton::indicator::checked{
                background: blueviolet;
                background-position: center;
            }
        '''
    )

    self.logoButton.setStyleSheet(

        '''
            QPushButton{
                border: none;
                background-image: url(images/blackicons/logo.png);
                background-repeat: no-repeat;
                background-position: center;
            }

            QPushButton:hover{
                border-left: 2px solid blueviolet;
                background-image: url(images/bluevioleticons/logo.png);
            }

            QPushButton:pressed{
                background-color: rgb(204, 204, 204);
            }
        '''
    )

    self.homeButton.setStyleSheet(

        '''
            QPushButton{
                border: none;
                background-image: url(images/blackicons/home.png);
                background-repeat: no-repeat;
                background-position: center;
            }

            QPushButton:hover{
                border-left: 2px solid blueviolet;
                background-image: url(images/bluevioleticons/home.png);
            }

            QPushButton:pressed{
                background-color: rgb(204, 204, 204);
            }
        '''
    )

    self.searchButton.setStyleSheet(

        '''
            QPushButton{
                border: none;
                background-image: url(images/blackicons/search.png);
                background-repeat: no-repeat;
                background-position: center;
            }

            QPushButton:hover{
                border-left: 2px solid blueviolet;
                background-image: url(images/bluevioleticons/search.png);
            }

            QPushButton:pressed{
                background-color: rgb(204, 204, 204);
            }
        '''
    )

    self.markerButton.setStyleSheet(

        '''
            QPushButton{
                border: none;
                background-image: url(images/blackicons/marker.png);
                background-repeat: no-repeat;
                background-position: center;
            }

            QPushButton:hover{
                border-left: 2px solid blueviolet;
                background-image: url(images/bluevioleticons/marker.png);
            }

            QPushButton:pressed{
                background-color: rgb(204, 204, 204);
            }
        '''
    )

    self.mensageButton.setStyleSheet(

        '''
            QPushButton{
                border: none;
                background-image: url(images/blackicons/mensage.png);
                background-repeat: no-repeat;
                background-position: center;
            }

            QPushButton:hover{
                border-left: 2px solid blueviolet;
                background-image: url(images/bluevioleticons/mensage.png);
            }

            QPushButton:pressed{
                background-color: rgb(204, 204, 204);
            }
        '''
    )

    self.settingsButton.setStyleSheet(

        '''
            QPushButton{
                border: none;
                background-image: url(images/blackicons/settings.png);
                background-repeat: no-repeat;
                background-position: center;
            }

            QPushButton:hover{
                border-left: 2px solid blueviolet;
                background-image: url(images/bluevioleticons/settings.png);
            }

            QPushButton:pressed{
                background-color: rgb(204, 204, 204);
            }
        '''
    )
