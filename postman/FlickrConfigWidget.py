from PySide import QtGui
from PySide import QtCore

from FlickrWorker import *

from postman_lib import Ui_FlickrConfigWidget


class FlickrConfigWidget(QtGui.QWidget):
    
    STATE_AUTH = 0
    STATE_CONFIRM = 1
    STATE_DONE = 2
    
    def __init__(self, parent = None):
        super(FlickrConfigWidget, self).__init__(parent)
        
        self.ui = Ui_FlickrConfigWidget.Ui_FlickrConfigWidget()
        self.ui.setupUi(self)
        
        self.ui.authButton.clicked.connect(self.authButtonClicked)
        
        self.enablerTimer = QtCore.QTimer(self)
        self.enablerTimer.setInterval(1000)
        self.enablerTimer.timeout.connect(self.reEnableButton)
        
    def setServiceModel(self, model):
        self.serviceModel = model
    
    def setService(self, service):
        
        # add and initialize non existing parameters
        if not 'auth' in service:
            service['auth'] = False

        if not 'flickrInst' in service:
            service['flickrInst'] = flickrapi.FlickrAPI(FlickrWorker.key, FlickrWorker.secret, store_token=False)

        self.ui.authButton.setText('Authorize...')
        if service['auth'] == True:
            self.state = self.STATE_DONE
            self.ui.authButton.setVisible(False)
            self.ui.successLabel.setVisible(True)
        else:
            self.state = self.STATE_AUTH
            self.ui.authButton.setVisible(True)
            self.ui.successLabel.setVisible(False)

        # save the reference to the service
        self.service = service
    
    def authButtonClicked(self):
        if self.state == self.STATE_AUTH:
            try:
                (token, frob) = self.service['flickrInst'].get_token_part_one(perms='write')
            except:
                QtGui.QMessageBox.information(self, QtCore.QCoreApplication.applicationName(), 'Cannot start the authorization process.\n\nPlease make sure that you are connected to the internet.')
                return

            self.service['flickrToken'] = token
            self.service['flickrFrob'] = frob

            self.ui.authButton.setEnabled(False)
            self.state = self.STATE_CONFIRM
            
            self.enablerTimer.start()
            self.count = 5

        elif self.state == self.STATE_CONFIRM:
            # check if authenticated correctly
            try:
                self.service['flickrInst'].get_token_part_two((self.service['flickrToken'], self.service['flickrFrob']))
            except flickrapi.exceptions.FlickrError:
                QtGui.QMessageBox.information(self, QtGui.QApplication.applicationName(), '<p>The Flickr website did not authorize ' + QtGui.QApplication.applicationName() + ' correctly.</p><p>Please make sure that you finish the authorization process before clicking the <span style="font-style: italic">Confirm</span> button.</p>')

                self.state = self.STATE_AUTH
                self.ui.authButton.setText('Authorize')
                return

            self.ui.authButton.setVisible(False)
            self.ui.successLabel.setVisible(True)
            self.state = self.STATE_DONE
            self.service['auth'] = True
            self.serviceModel.notifyAuthChanged()

    def reEnableButton(self):
        if self.count > 0:
            self.ui.authButton.setText('Confirm (' + str(self.count) + ')')
        else:
            self.enablerTimer.stop()
            self.ui.authButton.setText('Confirm')
            self.ui.authButton.setEnabled(True)
    
        self.count = self.count - 1

