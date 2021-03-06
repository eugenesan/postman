from PySide import QtGui
from PySide import QtCore

from postman_lib.Ui_AddImagesWidget import Ui_AddImagesWidget

class AddImagesWidget(QtGui.QWidget):

    def __init__(self, parent = None):
        super(AddImagesWidget, self).__init__(parent)
        
        self.ui = Ui_AddImagesWidget()
        self.ui.setupUi(self)
        
        self.ui.addImagesButton.clicked.connect(self.addImagesButtonClicked)
        
    
    def addImagesButtonClicked(self):
        fileNames, _ = QtGui.QFileDialog.getOpenFileNames(self, 'Add Images...', '', 'Images (*.png *.jpg *.jpeg *.bmp)')
        
        urls = list()
        for f in fileNames:
            urls.append(QtCore.QUrl.fromLocalFile(f))
        
        self.mainWindow.addFiles(urls)
        
