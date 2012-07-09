from PySide import QtCore
from PySide import QtGui

from FlickrWorker import *
from UbuntuOneWorker import *

class ServicesModel(QtCore.QAbstractListModel):
    
    selectionChangedSignal = QtCore.Signal(int)
    authChanged = QtCore.Signal()
    uploadFinishedSignal = QtCore.Signal()

    def __init__(self, parent = None):
        QtCore.QAbstractListModel.__init__(self, parent)

        self.servicesList = list()

        self.selectedStampUid = -1
        self.stampUidCounter = -1
        
        # set roles
        self.ServiceNameRole = QtCore.Qt.UserRole + 1
        self.ServiceIconRole = QtCore.Qt.UserRole + 2
        self.ServiceProgressRole = QtCore.Qt.UserRole + 3
        self.ServiceStatusRole = QtCore.Qt.UserRole + 4
        
        roles = dict()
        roles[self.ServiceNameRole] = 'serviceName'
        roles[self.ServiceIconRole] = 'serviceIcon'
        roles[self.ServiceProgressRole] = 'serviceProgress'
        roles[self.ServiceStatusRole] = 'serviceStatus'
        self.setRoleNames(roles)

    @QtCore.Slot(str, result=int)
    def createStamp(self, serviceName):
        self.stampUidCounter += 1

        serviceEntry = dict()
        serviceEntry['uid'] = self.stampUidCounter
        serviceEntry['name'] = serviceName
        
        self.beginInsertRows(QtCore.QModelIndex(), len(self.servicesList), len(self.servicesList))
        self.servicesList.append(serviceEntry)
        self.endInsertRows()
        
        self.notifyAuthChanged()
        
        top = self.createIndex(len(self.servicesList) - 1, 0, 0)
        bottom = self.createIndex(len(self.servicesList) - 1, 0, 0)
        self.dataChanged.emit(top, bottom)

        return self.stampUidCounter
    
    @QtCore.Slot(int)
    def destroyStamp(self, uid):
        item = self.getByUid(uid)
        row = self.servicesList.index(item)
        
        self.beginRemoveRows(QtCore.QModelIndex(), row, row)
        self.servicesList.remove(self.getByUid(uid))
        self.endRemoveRows()

        self.deselectAllStamps()
        
        self.notifyAuthChanged()

    @QtCore.Slot(int)
    def setSelectedStamp(self, uid):
        if uid != self.selectedStampUid:
            self.selectedStampUid = uid
            self.selectionChangedSignal.emit(self.selectedStampUid)

    @QtCore.Slot()
    def deselectAllStamps(self):
        self.selectedStampUid = -1
        self.selectionChangedSignal.emit(self.selectedStampUid)
    
    @QtCore.Slot(result=int)
    def selectedStamp(self):
        return self.selectedStampUid

    @QtCore.Slot(result=bool)
    def allAuth(self):
        if len(self.servicesList) == 0:
            return False

        for s in self.servicesList:
            if ('auth' in s) and (s['auth'] == True):
                continue
            else:
                return False

        return True
    
    def notifyAuthChanged(self):
        self.authChanged.emit()
    
    def getByUid(self, uid):
        for s in self.servicesList:
            if s['uid'] == uid:
                return s

        return None
    
    def rowCount(self, parent = QtCore.QModelIndex()):
        return len(self.servicesList)
    
    def data(self, index, role):

        if not index.isValid():
            return None

        if role == self.ServiceNameRole:
            return self.servicesList[index.row()]['name']
        elif role == self.ServiceIconRole:
            serviceName = self.servicesList[index.row()]['name']
            return self.stampsModel.getStampByName(serviceName).iconSource
        elif role == self.ServiceProgressRole:
            if 'worker' in self.servicesList[index.row()]:
                worker = self.servicesList[index.row()]['worker'] 
                if worker != None:
                    return worker.progress
                else:
                    return 0.0
            else:
                return 0.0
        elif role == self.ServiceStatusRole:
            if 'worker' in self.servicesList[index.row()]:
                worker = self.servicesList[index.row()]['worker'] 
                if worker != None:
                    return worker.status
                else:
                    return ''
            else:
                return ''

        return None
    
    @QtCore.Slot(result=int)
    def count(self):
        return len(self.servicesList)
    
    @QtCore.Slot()
    def deliver(self):
        # assign workers to every service
        for s in self.servicesList:
            # create a worker
            if s['name'] == 'Flickr':
                worker = FlickrWorker()
            elif s['name'] == 'Ubuntu One':
                worker = UbuntuOneWorker()

            worker.filesModel = self.filesModel
            worker.stampConfig = s
            worker.progressSignal.connect(self.progressChanged)
            worker.statusSignal.connect(self.progressChanged)
            worker.doneSignal.connect(self.workerDone)
            s['worker'] = worker

        # emit data changed event for all items
        top = self.createIndex(0, 0, 0)
        bottom = self.createIndex(len(self.servicesList) - 1, 0, 0)
        self.dataChanged.emit(top, bottom)
        
        # start from the first worker
        self.currentWorkerIndex = 0
        if len(self.servicesList) > self.currentWorkerIndex:
            self.servicesList[self.currentWorkerIndex]['worker'].start()
    
    @QtCore.Slot(dict)
    def progressChanged(self, s):
        index = self.servicesList.index(s)

        top = self.createIndex(index, 0, 0)
        bottom = self.createIndex(index, 0, 0)
        self.dataChanged.emit(top, bottom)

    @QtCore.Slot(dict)
    def workerDone(self, s):
        worker = s['worker']

        if worker.result:
            self.tray.showMessage(QtCore.QCoreApplication.applicationName(), s['name'] + ' service uploaded all files successfully', QtGui.QSystemTrayIcon.Information)
        else:
            self.tray.showMessage(QtCore.QCoreApplication.applicationName(), s['name'] + ' service failed to uploaded some of the files', QtGui.QSystemTrayIcon.Critical)
        
        # go to the next worker
        self.currentWorkerIndex += 1
        if len(self.servicesList) > self.currentWorkerIndex:
            self.servicesList[self.currentWorkerIndex]['worker'].start()
        else:
            self.uploadFinishedSignal.emit()
    
    @QtCore.Slot()
    def stopUploads(self):
        runningThread = self.servicesList[self.currentWorkerIndex]['worker']         
            
