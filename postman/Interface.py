from PySide import QtCore

class Interface(QtCore.QObject):

    highlightedPostcardIndexChangedSignal = QtCore.Signal(int)
    screenStateChangedSignal = QtCore.Signal(str)

    forceScreenChangeSignal = QtCore.Signal()
    forceCreateStampSignal = QtCore.Signal()

    @QtCore.Slot(int)
    def highlightedPostcardIndexChanged(self, index):
        self.highlightedPostcardIndexChangedSignal.emit(index)

    @QtCore.Slot(str)
    def screenStateChanged(self, state):
        self.screenStateChangedSignal.emit(state)

    def forceScreenChange(self, screen):
        self.forceScreenChangeSignal.emit()
    
    def createStamp(self, name, icon):
        self.pendingStampName = name
        self.pendingStampIcon = icon

        self.forceCreateStampSignal.emit()
    
    @QtCore.Slot(result=str)
    def getPendingStampName(self):
        return self.pendingStampName
    
    @QtCore.Slot(result=str)
    def getPendingStampIcon(self):
        return self.pendingStampIcon
