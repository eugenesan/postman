from PySide import QtCore

class FileDetailsModel(QtCore.QAbstractListModel):

    def __init__(self, parent = None):
        QtCore.QAbstractListModel.__init__(self, parent)
        
        self.filesList = list()

        # set roles
        self.FilePathRole = QtCore.Qt.UserRole + 1
        self.TitleRole = QtCore.Qt.UserRole + 2
        self.DescriptionRole = QtCore.Qt.UserRole + 3

        roles = dict()
        roles[self.FilePathRole] = 'filePath'
        roles[self.TitleRole] = 'title'
        roles[self.DescriptionRole] = 'description'
        self.setRoleNames(roles)

    def addItem(self, item):
        # if file already exists, do nothing
        if self.itemExists(item):
            return
        
        self.beginInsertRows(QtCore.QModelIndex(), len(self.filesList), len(self.filesList))
        self.filesList.append(item)
        self.endInsertRows()
        
        top = self.createIndex(len(self.filesList) - 1, 0, 0)
        bottom = self.createIndex(len(self.filesList) - 1, 0, 0)
        self.dataChanged.emit(top, bottom)

    @QtCore.Slot(result=int)
    def count(self):
        return len(self.filesList)

    def rowCount(self, parent = QtCore.QModelIndex()):
        return len(self.filesList)
    
    def data(self, index, role):

        if not index.isValid():
            return None

        if role == self.FilePathRole:
            return self.filesList[index.row()].filePath
        elif role == self.TitleRole:
            return self.filesList[index.row()].title
        elif role == self.DescriptionRole:
            return self.filesList[index.row()].description

        return None

    @QtCore.Slot(int)
    def remove(self, row, parent = QtCore.QModelIndex()):
        self.beginRemoveRows(QtCore.QModelIndex(), row, row)
        del self.filesList[row]
        self.endRemoveRows()
        
        top = self.createIndex(row, 0, 0)
        bottom = self.createIndex(row, 0, 0)
        self.dataChanged.emit(top, bottom)

        return True

    def itemExists(self, item):
        # identify duplicates by file path
        for f in self.filesList:
            if f.filePath == item.filePath:
                return True

        return False