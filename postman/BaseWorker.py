from PySide import QtCore

class BaseWorker(QtCore.QThread):
    
    progressSignal = QtCore.Signal(dict)
    statusSignal = QtCore.Signal(dict)
    doneSignal = QtCore.Signal(dict)
    
    def __init__(self, parent=None):
        super(BaseWorker, self).__init__(parent)
        
        # initialize some variables
        self.retry = 4
        self.result = False
        self.progress = 0.0
        self.status = ''