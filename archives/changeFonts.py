def ubuntuFont(self):
    loginFrameUbuntoFont(self)

def helveticaFont(self):
    loginFrameHelveticaFont(self)

def arialFont(self):
    loginFrameArialFont(self)

def loginFrameUbuntoFont(self):
    if self.ubuntuMonoFont.isChecked():
        self.settingsLabel.setStyleSheet(
            '''
                QLabel{
                    border: none;
                    background: none;
                    color: whitesmoke;
                    font: bold 25px Ubuntu Mono;
                    border-bottom: 2px solid whitesmoke;
                }
            '''
        )
    else:
        pass

def loginFrameHelveticaFont(self):
    if self.helveticaFont.isChecked():
        self.settingsLabel.setStyleSheet(
            '''
                QLabel{
                    border: none;
                    background: none;
                    color: whitesmoke;
                    font: bold 25px Helvetica;
                    border-bottom: 2px solid whitesmoke;
                }
            '''
        )
    else:
        pass

def loginFrameArialFont(self):
    if self.arialFont.isChecked():
        self.settingsLabel.setStyleSheet(
            '''
                QLabel{
                    border: none;
                    background: none;
                    color: whitesmoke;
                    font: bold 25px Arial;
                    border-bottom: 2px solid whitesmoke;
                }
            '''
        )
    else:
        pass
