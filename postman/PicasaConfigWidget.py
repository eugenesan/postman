from PySide import QtGui

from GooglePlusConfigWidget import *

from postman_lib import Ui_PicasaConfigWidget


class PicasaConfigWidget(QtGui.QWidget):

    def __init__(self, parent = None):
        super(PicasaConfigWidget, self).__init__(parent)

        self.ui = Ui_PicasaConfigWidget.Ui_PicasaConfigWidget()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self.loginButtonClicked)
        self.ui.albumEdit.textEdited.connect(self.albumTextEdited)

        self.ui.usernameEdit.returnPressed.connect(self.ui.loginButton.clicked)
        self.ui.passwordEdit.returnPressed.connect(self.ui.loginButton.clicked)

    def setServiceModel(self, model):
        self.serviceModel = model

    def setService(self, service):

        # add and initialize non existing parameters
        if not 'auth' in service:
            service['auth'] = False

        isAuth = service['auth']
        if isAuth:
            self.ui.usernameEdit.setText(service['googlePlusUsername'])
            self.ui.passwordEdit.setText(service['googlePlusPassword'])
        else:
            self.ui.usernameEdit.clear()
            self.ui.passwordEdit.clear()

        if 'googlePlusAlbum' in service:
            self.ui.albumEdit.setText(service['googlePlusAlbum'])
        else:
            self.ui.albumEdit.clear()

        self.ui.loginContainer.setVisible(not isAuth)
        self.ui.messageLabel.setVisible(False)
        self.ui.successLabel.setVisible(isAuth)
        self.ui.albumSettings.setVisible(isAuth)

        # save the reference to the service
        self.service = service

    def loginButtonClicked(self):

        import gdata.photos, gdata.photos.service

        client = gdata.photos.service.PhotosService()
        isAuth = False

        try:
            client.ClientLogin(self.ui.usernameEdit.text(), self.ui.passwordEdit.text())
            self.service['googlePlusInst'] = client
            self.service['googlePlusUsername'] = self.ui.usernameEdit.text()
            self.service['googlePlusPassword'] = self.ui.passwordEdit.text()
            isAuth = True
        except gdata.service.BadAuthentication:
            self.ui.messageLabel.setText('Incorrect username or password.')
        except:
            self.ui.messageLabel.setText('Could not contact Google+ server.')


        self.service['auth'] = isAuth
        if isAuth:
            self.serviceModel.notifyAuthChanged()

        self.ui.loginContainer.setVisible(not isAuth)
        self.ui.messageLabel.setVisible(not isAuth)
        self.ui.successLabel.setVisible(isAuth)
        self.ui.albumSettings.setVisible(isAuth)
        if isAuth:
            self.ui.albumSettings.setFocus()

    def albumTextEdited(self, text):
        self.service['googlePlusAlbum'] = text
