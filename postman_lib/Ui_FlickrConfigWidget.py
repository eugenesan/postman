# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FlickrConfigWidget.ui'
#
# Created: Mon Aug 27 21:45:13 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FlickrConfigWidget(object):
    def setupUi(self, FlickrConfigWidget):
        FlickrConfigWidget.setObjectName("FlickrConfigWidget")
        FlickrConfigWidget.resize(320, 478)
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
        self.verticalLayout_2.setContentsMargins(5, -1, 5, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.instructionLabel = QtGui.QLabel(FlickrConfigWidget)
        self.instructionLabel.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.instructionLabel.setWordWrap(True)
        self.instructionLabel.setMargin(6)
        self.instructionLabel.setObjectName("instructionLabel")
        self.verticalLayout_2.addWidget(self.instructionLabel)
        spacerItem = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.loginGroupBox = QtGui.QGroupBox(FlickrConfigWidget)
        self.loginGroupBox.setObjectName("loginGroupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.loginGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.usernameContainer = QtGui.QWidget(self.loginGroupBox)
        self.usernameContainer.setObjectName("usernameContainer")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.usernameContainer)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.usernameContainer)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.usernameEdit = QtGui.QLineEdit(self.usernameContainer)
        self.usernameEdit.setObjectName("usernameEdit")
        self.horizontalLayout_2.addWidget(self.usernameEdit)
        self.verticalLayout_3.addWidget(self.usernameContainer)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.authButton = QtGui.QPushButton(self.loginGroupBox)
        self.authButton.setObjectName("authButton")
        self.horizontalLayout.addWidget(self.authButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.loginGroupBox)
        self.successLabel = QtGui.QLabel(FlickrConfigWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.successLabel.setFont(font)
        self.successLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.successLabel.setObjectName("successLabel")
        self.verticalLayout_2.addWidget(self.successLabel)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(FlickrConfigWidget)
        QtCore.QMetaObject.connectSlotsByName(FlickrConfigWidget)

    def retranslateUi(self, FlickrConfigWidget):
        FlickrConfigWidget.setWindowTitle(QtGui.QApplication.translate("FlickrConfigWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.instructionLabel.setText(QtGui.QApplication.translate("FlickrConfigWidget", "<html><head/><body><p>Flickr is an image and video hosting website owned by Yahoo!</p><p>When logging in through Postman with a  <span style=\" font-style:italic;\">username</span> for the first time, clicking the <span style=\" font-style:italic;\">Login...</span> button will launch your default web browser so that you can authorize Postman to upload photos to your Flickr account. After granting permissions, click the <span style=\" font-style:italic;\">Confirm</span> button to complete the process.</p> <p>Subsequent logins with authorized  <span style=\" font-style:italic;\">usernames</span> will be automatic.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.loginGroupBox.setTitle(QtGui.QApplication.translate("FlickrConfigWidget", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FlickrConfigWidget", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.authButton.setText(QtGui.QApplication.translate("FlickrConfigWidget", "Login...", None, QtGui.QApplication.UnicodeUTF8))
        self.successLabel.setText(QtGui.QApplication.translate("FlickrConfigWidget", "Flickr authorized Postman successfully.", None, QtGui.QApplication.UnicodeUTF8))

