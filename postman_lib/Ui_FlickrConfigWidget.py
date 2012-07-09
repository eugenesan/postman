# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FlickrConfigWidget.ui'
#
# Created: Sun Jul  8 19:13:31 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FlickrConfigWidget(object):
    def setupUi(self, FlickrConfigWidget):
        FlickrConfigWidget.setObjectName("FlickrConfigWidget")
        FlickrConfigWidget.resize(320, 350)
        FlickrConfigWidget.setMinimumSize(QtCore.QSize(320, 0))
        self.verticalLayout = QtGui.QVBoxLayout(FlickrConfigWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(FlickrConfigWidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 55))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame.setStyleSheet("QFrame {\n"
"    background-image: url(/opt/extras.ubuntu.com/postman/share/postman/media/flickrLogo.png);\n"
"    background-repeat: none;\n"
"    background-origin: border-box;\n"
"    background-position: left center\n"
"}")
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.instructionLabel = QtGui.QLabel(FlickrConfigWidget)
        self.instructionLabel.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.instructionLabel.setWordWrap(True)
        self.instructionLabel.setMargin(6)
        self.instructionLabel.setObjectName("instructionLabel")
        self.verticalLayout_2.addWidget(self.instructionLabel)
        spacerItem = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.authButton = QtGui.QPushButton(FlickrConfigWidget)
        self.authButton.setObjectName("authButton")
        self.horizontalLayout.addWidget(self.authButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.successLabel = QtGui.QLabel(FlickrConfigWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.successLabel.setFont(font)
        self.successLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.successLabel.setObjectName("successLabel")
        self.verticalLayout_2.addWidget(self.successLabel)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(FlickrConfigWidget)
        QtCore.QMetaObject.connectSlotsByName(FlickrConfigWidget)

    def retranslateUi(self, FlickrConfigWidget):
        FlickrConfigWidget.setWindowTitle(QtGui.QApplication.translate("FlickrConfigWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.instructionLabel.setText(QtGui.QApplication.translate("FlickrConfigWidget", "<p>Flickr is an image hosting and video hosting website owned by Yahoo!</p>\n"
"Clicking the <span style=\" font-style:italic;\">Authorize...</span> button will launch your default web browser so that you can authorize Postman to upload photos to your Flickr account. After granting permissions, click the <span style=\" font-style:italic;\">Confirm</span> button to complete the process.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.authButton.setText(QtGui.QApplication.translate("FlickrConfigWidget", "Authorize...", None, QtGui.QApplication.UnicodeUTF8))
        self.successLabel.setText(QtGui.QApplication.translate("FlickrConfigWidget", "Flickr authorized Postman successfully.", None, QtGui.QApplication.UnicodeUTF8))

