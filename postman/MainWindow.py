from PySide import QtGui
from PySide import QtDeclarative

import os

from postman_lib import helpers
from postman_lib import postmanconfig

from postman_lib import Ui_MainWindow

# services imports
from ServiceInstructionsWidget import *
from FlickrConfigWidget import *
from UbuntuOneConfigWidget import *

from AddImagesWidget import *
from ImageDetailsWidget import *
from FileDetailsModel import *
from FileDetails import *
from ServicesModel import *
from Interface import *

import Stamps


class MainWindow(QtGui.QMainWindow):
     
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)

        self.ui.declarativeView.mainWindow = self
        self.ui.declarativeView.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)
        self.ui.declarativeView.viewport().setAcceptDrops(True)

        desktopCenter = QtGui.QApplication.desktop().geometry().center()
        topLeft = QtCore.QPoint(desktopCenter.x() - self.width() / 2, desktopCenter.y() - self.height() / 2)
        self.move(topLeft)

        self.tray = QtGui.QSystemTrayIcon(self)
        self.tray.show()

        # create docking window
        self.dockWindow = QtGui.QDockWidget('', self)
        self.dockWindow.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dockWindow)
        
        self.serviceInstructionsWidget = ServiceInstructionsWidget()

        self.interface = Interface()
        self.interface.screenStateChangedSignal.connect(self.screenChanged)
        
        self.setupStampsModel()
        self.fileDetailsModel = FileDetailsModel(self)
        self.servicesModel = ServicesModel()
        self.servicesModel.stampsModel = self.stampsModel
        self.servicesModel.selectionChangedSignal.connect(self.stampSelectionChanged)
        self.servicesModel.filesModel = self.fileDetailsModel
        self.servicesModel.tray = self.tray

        # create widgets
        self.addImagesWidget = AddImagesWidget()
        self.addImagesWidget.mainWindow = self

        self.imageDetailsWidget = ImageDetailsWidget()
        self.imageDetailsWidget.fileDetailsModel = self.fileDetailsModel
        self.interface.highlightedPostcardIndexChangedSignal.connect(self.imageDetailsWidget.highlightedIndexChanged)
        
        self.validExtensions = ['bmp', 'png', 'jpg', 'jpeg']
        
        self.initializeQmlScene()
        
    def setupStampsModel(self):
        self.stampsModel = Stamps.StampListModel()
        self.stampsModel.addStamp(Stamps.Stamp('Flickr', 'images/stamps/flickrIcon.png', FlickrConfigWidget()))
        self.stampsModel.addStamp(Stamps.Stamp('Ubuntu One', 'images/stamps/ubuntuOneIcon.png', UbuntuOneConfigWidget()))

    def initializeQmlScene(self):
        self.rootContext = self.ui.declarativeView.rootContext()
        self.rootContext.setContextProperty('stampSheetModel', self.stampsModel)
        self.rootContext.setContextProperty('servicesModel', self.servicesModel)
        self.rootContext.setContextProperty('imageListModel', self.fileDetailsModel)
        self.rootContext.setContextProperty('mainInterface', self.interface)

        self.ui.declarativeView.setSource(QtCore.QUrl.fromLocalFile(postmanconfig.get_data_path() + "/qml/main.qml"))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        self.addFiles(event.mimeData().urls())   

    def addFiles(self, urls):
        # files cannot be added while delivering files
        if self.currentScreen == 'deliveryView':
            return

        fileList = []
        
        for u in urls:
            # if it's a file simply add to the list
            localFile = u.toLocalFile()
            if not localFile:
                continue

            # check if it is a file or a directory
            fileInfo = QtCore.QFileInfo(localFile)
            if fileInfo.isFile():
                if self.isValidFile(localFile):
                    fileList.append(localFile)
            elif fileInfo.isDir():
                dirIter = QtCore.QDirIterator(localFile, QtCore.QDir.Files | QtCore.QDir.NoDotAndDotDot, QtCore.QDirIterator.Subdirectories)

                while dirIter.hasNext():
                    dirIter.next()
                    if self.isValidFile(dirIter.filePath()):
                        fileList.append(dirIter.filePath())

        for f in fileList:
            self.fileDetailsModel.addItem(FileDetails(f))
        
        # switch to photo view
        self.interface.forceScreenChange('stackView')

    def isValidFile(self, filepath):
        fileInfo = QtCore.QFileInfo(filepath)
        if fileInfo.isFile():
            # check extension
            if fileInfo.suffix() in self.validExtensions:
                return True

        return False
    
    def addStamp(self, service):
        # get icon for this service
        stamp = self.stampsModel.getStampByName(service)
        if stamp != None:
            self.interface.createStamp(service, stamp.iconSource)
    
    def stampSelectionChanged(self, uid):
        self.loadConfigWidget()
    
    def loadConfigWidget(self):
        selectedUid = self.servicesModel.selectedStampUid
        if selectedUid == -1:
            self.dockWindow.setWindowTitle('Service Configuration')
            self.dockWindow.setWidget(self.serviceInstructionsWidget)
        else:
            service = self.servicesModel.getByUid(selectedUid)
            serviceName = service['name']
            configWidget = self.stampsModel.getStampByName(serviceName).configWidget
            configWidget.setServiceModel(self.servicesModel)
            configWidget.setService(service)

            self.dockWindow.setWindowTitle(serviceName + ' Configuration')
            self.dockWindow.setWidget(configWidget)

    def screenChanged(self, screen):
        self.currentScreen = screen

        if screen == 'stackView':
            self.dockWindow.setWindowTitle('Add Images')
            self.dockWindow.setWidget(self.addImagesWidget)
        elif screen == 'gridView':
            self.dockWindow.setWindowTitle('Image Details')
            self.dockWindow.setWidget(self.imageDetailsWidget)
        elif screen == 'stampView':
            self.dockWindow.setWindowTitle('Service Configuration')
            self.loadConfigWidget()
        elif screen == 'deliveryView':
            self.dockWindow.setWindowTitle('Delivery')
            self.dockWindow.setWidget(None)
