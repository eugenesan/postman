from PySide import QtGui

from postman_lib import Ui_UbuntuOneConfigWidget


class UbuntuOneConfigWidget(QtGui.QWidget):
    
    def __init__(self, parent = None):
        super(UbuntuOneConfigWidget, self).__init__(parent)

        self.ui = Ui_UbuntuOneConfigWidget.Ui_UbuntuOneConfigWidget()
        self.ui.setupUi(self)
        
        self.ui.loginButton.clicked.connect(self.loginButtonClicked)
        self.ui.volumeEdit.textEdited.connect(self.volumeTextEdited)

    def setServiceModel(self, model):
        self.serviceModel = model

    def setService(self, service):
        
        # add and initialize non existing parameters
        if not 'auth' in service:
            service['auth'] = False
  
        isAuth = service['auth']

        self.ui.loginButton.setVisible(not isAuth)
        self.ui.successLabel.setVisible(isAuth)
        self.ui.volumeSettings.setVisible(isAuth)

        if 'ubuntuOneVolume' in service:
            self.ui.volumeEdit.setText(service['ubuntuOneVolume'])
        
        # save the reference to the service
        self.service = service
    
    def loginButtonClicked(self):
        
        from gobject import MainLoop
        from dbus.mainloop.glib import DBusGMainLoop
        from ubuntuone.platform.credentials import CredentialsManagementTool

        DBusGMainLoop(set_as_default=True)
        loop = MainLoop()

        def loginQuit(result):
            loop.quit()
            self.service['ubuntuOneInst'] = result
            self.service['auth'] = result != None
            if self.service['auth']:
                self.serviceModel.notifyAuthChanged()

        cd = CredentialsManagementTool()
        d = cd.login()
        d.addCallbacks(loginQuit)

        loop.run()

        isAuth = self.service['auth']
        self.ui.loginButton.setVisible(not isAuth)
        self.ui.successLabel.setVisible(isAuth)
        self.ui.volumeSettings.setVisible(isAuth)
        if isAuth:
            self.ui.volumeEdit.setFocus()
    
    def volumeTextEdited(self, text):
        self.service['ubuntuOneVolume'] = text

