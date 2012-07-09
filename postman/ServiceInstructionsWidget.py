from PySide import QtGui

from postman_lib import Ui_ServiceInstructionsWidget


class ServiceInstructionsWidget(QtGui.QWidget):
    
    def __init__(self, parent = None):
        super(ServiceInstructionsWidget, self).__init__(parent)
        
        self.ui = Ui_ServiceInstructionsWidget.Ui_ServiceInstructionsWidget()
        self.ui.setupUi(self)
