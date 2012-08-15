from PySide import QtDeclarative


class QDeclarativeViewCustom(QtDeclarative.QDeclarativeView):

    def __init__(self, parent = None):
        super(QDeclarativeViewCustom, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        self.mainWindow.addFiles(event.mimeData().urls())
        
