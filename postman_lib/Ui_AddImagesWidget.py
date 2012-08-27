# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddImagesWidget.ui'
#
# Created: Mon Aug 27 21:36:56 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AddImagesWidget(object):
    def setupUi(self, AddImagesWidget):
        AddImagesWidget.setObjectName("AddImagesWidget")
        AddImagesWidget.resize(320, 326)
        AddImagesWidget.setMinimumSize(QtCore.QSize(320, 0))
        self.gridLayout = QtGui.QGridLayout(AddImagesWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(AddImagesWidget)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.addImagesButton = QtGui.QPushButton(AddImagesWidget)
        self.addImagesButton.setObjectName("addImagesButton")
        self.horizontalLayout.addWidget(self.addImagesButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(AddImagesWidget)
        QtCore.QMetaObject.connectSlotsByName(AddImagesWidget)

    def retranslateUi(self, AddImagesWidget):
        AddImagesWidget.setWindowTitle(QtGui.QApplication.translate("AddImagesWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddImagesWidget", "<p>You may add images to your envelope by dragging files and folders from your computer onto this window. Alternatively, you may click the <span style=\"font-style:italic\">Add Images...</span> button below to browse for files.</p>\n"
"<p>Clicking on the stack of images will open the images in a grid. You may then enter metadata for each of the images.</p>\n"
"<p><span style=\"font-weight:bold\">Note: </span>Only some upload services will make use of the metadata.", None, QtGui.QApplication.UnicodeUTF8))
        self.addImagesButton.setText(QtGui.QApplication.translate("AddImagesWidget", "Add Images...", None, QtGui.QApplication.UnicodeUTF8))

