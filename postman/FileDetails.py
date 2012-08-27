from PySide import QtCore

class FileDetails:

    def __init__(self, filePath):
        self.filePath = filePath
        self.title = ''
        self.description = ''
        self.tags = ''
