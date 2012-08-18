# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UbuntuOneConfigWidget.ui'
#
# Created: Sat Aug 18 11:02:21 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_UbuntuOneConfigWidget(object):
    def setupUi(self, UbuntuOneConfigWidget):
        UbuntuOneConfigWidget.setObjectName("UbuntuOneConfigWidget")
        UbuntuOneConfigWidget.resize(320, 469)
        UbuntuOneConfigWidget.setMinimumSize(QtCore.QSize(320, 0))
        self.verticalLayout = QtGui.QVBoxLayout(UbuntuOneConfigWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(UbuntuOneConfigWidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 90))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame.setStyleSheet("QFrame {\n"
"    background-image: url(/opt/extras.ubuntu.com/postman/share/postman/media/ubuntuOneLogo.png);\n"
"    background-repeat: none;\n"
"    background-origin: border-box;\n"
"    background-position: left center\n"
"}")
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(6, 6, 6, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(UbuntuOneConfigWidget)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.loginButton = QtGui.QPushButton(UbuntuOneConfigWidget)
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout.addWidget(self.loginButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.successLabel = QtGui.QLabel(UbuntuOneConfigWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.successLabel.setFont(font)
        self.successLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.successLabel.setWordWrap(True)
        self.successLabel.setObjectName("successLabel")
        self.verticalLayout_2.addWidget(self.successLabel)
        spacerItem3 = QtGui.QSpacerItem(0, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.volumeSettings = QtGui.QGroupBox(UbuntuOneConfigWidget)
        self.volumeSettings.setObjectName("volumeSettings")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.volumeSettings)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(self.volumeSettings)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.volumeEdit = QtGui.QLineEdit(self.volumeSettings)
        self.volumeEdit.setText("")
        self.volumeEdit.setObjectName("volumeEdit")
        self.horizontalLayout_3.addWidget(self.volumeEdit)
        self.verticalLayout_2.addWidget(self.volumeSettings)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)

        self.retranslateUi(UbuntuOneConfigWidget)
        QtCore.QMetaObject.connectSlotsByName(UbuntuOneConfigWidget)

    def retranslateUi(self, UbuntuOneConfigWidget):
        UbuntuOneConfigWidget.setWindowTitle(QtGui.QApplication.translate("UbuntuOneConfigWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("UbuntuOneConfigWidget", "<p>Ubuntu One is a personal cloud service operated by Canonical Ltd.</p>\n"
"<p>Click the <span style=\"font-style: italic\">Login...</span> button to login. If you are already logged in, you will not be prompted again to enter your e-mail and password.</p>\n"
"<p>Once logged in, please enter the <span style=\"font-style: italic\">Volume</span> name where files will be uploaded. If this field is left empty, it will default to <span style=\"font-style: italic\">Postman</span>.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.loginButton.setText(QtGui.QApplication.translate("UbuntuOneConfigWidget", "Login...", None, QtGui.QApplication.UnicodeUTF8))
        self.successLabel.setText(QtGui.QApplication.translate("UbuntuOneConfigWidget", "Ubuntu One authorized Postman successfully.", None, QtGui.QApplication.UnicodeUTF8))
        self.volumeSettings.setTitle(QtGui.QApplication.translate("UbuntuOneConfigWidget", "Configure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("UbuntuOneConfigWidget", "Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.volumeEdit.setPlaceholderText(QtGui.QApplication.translate("UbuntuOneConfigWidget", "Postman", None, QtGui.QApplication.UnicodeUTF8))

