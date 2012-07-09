from PySide import QtCore

class Stamp(object):

    def __init__(self, name, iconSource, configWidget = None):
        self.name = name
        self.iconSource = iconSource
        self.configWidget = configWidget

class StampListModel(QtCore.QAbstractListModel):

    def __init__(self, parent = None):
        QtCore.QAbstractListModel.__init__(self, parent)

        self.stampList = list()

        # define model roles
        self.NameRole = QtCore.Qt.UserRole + 1;
        self.IconSourceRole = QtCore.Qt.UserRole + 2;

        roles = dict()
        roles[self.NameRole] = 'name'
        roles[self.IconSourceRole] = 'iconSource'
        self.setRoleNames(roles)

    def addStamp(self, stamp):
        self.beginInsertRows(QtCore.QModelIndex(), len(self.stampList) - 1, len(self.stampList) - 1)
        self.stampList.append(stamp)
        self.endInsertRows()

        topLeft = self.createIndex(len(self.stampList) - 1, 0, 0)
        bottomRight = self.createIndex(len(self.stampList) - 1, 0, 0)

        self.dataChanged.emit(topLeft, bottomRight)

    def rowCount(self, parent = QtCore.QModelIndex()):
        return len(self.stampList)

    def data(self, index, role):
        if not index.isValid():
            return None

        if role == self.NameRole:
            return self.stampList[index.row()].name
        elif role == self.IconSourceRole:
            return self.stampList[index.row()].iconSource

        return None
    
    def getStampByName(self, name):
        for s in self.stampList:
            if s.name == name:
                return s
        
        return None
        