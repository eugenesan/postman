from PySide import QtCore
from PySide import QtGui

from postman_lib import Ui_ImageDetailsWidget

class ImageDetailsWidget(QtGui.QWidget):

    def __init__(self, parent = None):
        super(ImageDetailsWidget, self).__init__(parent)
        
        self.ui = Ui_ImageDetailsWidget.Ui_ImageDetailsWidget()
        self.ui.setupUi(self)
        
        self.ui.titleLineEdit.setPlaceholderText('No Title')
        self.ui.descriptionTextEdit.setDefaultText('No Description')
        self.ui.tagsLineEdit.setPlaceholderText('No Tags')
        
        self.ui.titleLineEdit.textChanged.connect(self.titleChangedSlot)
        self.ui.descriptionTextEdit.textChanged.connect(self.descriptionChangedSlot)
        self.ui.tagsLineEdit.textChanged.connect(self.tagsChangedSlot)
        
        self.currentIndex = -1
        
    @QtCore.Slot(int)
    def highlightedIndexChanged(self, index):
        self.currentIndex = index
        
        # load file details into UI if index is valid
        if self.currentIndex > -1 and self.currentIndex < self.fileDetailsModel.rowCount():
            self.ui.titleLineEdit.setText(self.fileDetailsModel.filesList[index].title)
            self.ui.descriptionTextEdit.setText(self.fileDetailsModel.filesList[index].description)
            self.ui.tagsLineEdit.setText(self.fileDetailsModel.filesList[index].tags)
        else:
            self.ui.titleLineEdit.clear()
            self.ui.descriptionTextEdit.clear()
            self.ui.tagsLineEdit.clear()
        
    def titleChangedSlot(self, title):
        if self.currentIndex > -1 and self.currentIndex < self.fileDetailsModel.rowCount():
            self.fileDetailsModel.filesList[self.currentIndex].title = title

    def descriptionChangedSlot(self):
        if self.currentIndex > -1 and self.currentIndex < self.fileDetailsModel.rowCount():
            self.fileDetailsModel.filesList[self.currentIndex].description = self.ui.descriptionTextEdit.toPlainText()

    def tagsChangedSlot(self, tags):
        if self.currentIndex > -1 and self.currentIndex < self.fileDetailsModel.rowCount():
            self.fileDetailsModel.filesList[self.currentIndex].tags = tags
        
