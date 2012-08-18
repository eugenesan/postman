# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PicasaConfigWidget.ui'
#
# Created: Sat Aug 18 17:17:12 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PicasaConfigWidget(object):
    def setupUi(self, PicasaConfigWidget):
        PicasaConfigWidget.setObjectName("PicasaConfigWidget")
        PicasaConfigWidget.resize(320, 543)
        PicasaConfigWidget.setMinimumSize(QtCore.QSize(320, 0))
        self.verticalLayout = QtGui.QVBoxLayout(PicasaConfigWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(PicasaConfigWidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 70))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame.setStyleSheet("QFrame {\n"
"    background-image: url(/opt/extras.ubuntu.com/postman/share/postman/media/picasaLogo.png);\n"
"    background-repeat: none;\n"
"    background-origin: border-box;\n"
"    background-position: left center\n"
"}")
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(6, 6, 6, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(PicasaConfigWidget)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.loginContainer = QtGui.QGroupBox(PicasaConfigWidget)
        self.loginContainer.setObjectName("loginContainer")
        self.formLayout_2 = QtGui.QFormLayout(self.loginContainer)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtGui.QLabel(self.loginContainer)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.loginContainer)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.usernameEdit = QtGui.QLineEdit(self.loginContainer)
        self.usernameEdit.setObjectName("usernameEdit")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.usernameEdit)
        self.passwordEdit = QtGui.QLineEdit(self.loginContainer)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.passwordEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.loginButton = QtGui.QPushButton(self.loginContainer)
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout.addWidget(self.loginButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.formLayout_2.setLayout(3, QtGui.QFormLayout.SpanningRole, self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.formLayout_2.setItem(2, QtGui.QFormLayout.SpanningRole, spacerItem3)
        self.verticalLayout_2.addWidget(self.loginContainer)
        self.messageLabel = QtGui.QLabel(PicasaConfigWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.messageLabel.setFont(font)
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setObjectName("messageLabel")
        self.verticalLayout_2.addWidget(self.messageLabel)
        self.successLabel = QtGui.QLabel(PicasaConfigWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.successLabel.setFont(font)
        self.successLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.successLabel.setWordWrap(True)
        self.successLabel.setObjectName("successLabel")
        self.verticalLayout_2.addWidget(self.successLabel)
        spacerItem4 = QtGui.QSpacerItem(0, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.albumSettings = QtGui.QGroupBox(PicasaConfigWidget)
        self.albumSettings.setObjectName("albumSettings")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.albumSettings)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(self.albumSettings)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.albumEdit = QtGui.QLineEdit(self.albumSettings)
        self.albumEdit.setText("")
        self.albumEdit.setObjectName("albumEdit")
        self.horizontalLayout_3.addWidget(self.albumEdit)
        self.verticalLayout_2.addWidget(self.albumSettings)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)

        self.retranslateUi(PicasaConfigWidget)
        QtCore.QMetaObject.connectSlotsByName(PicasaConfigWidget)

    def retranslateUi(self, PicasaConfigWidget):
        PicasaConfigWidget.setWindowTitle(QtGui.QApplication.translate("PicasaConfigWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PicasaConfigWidget", "<p>Picasa is an online image viewer and organizer.</p>\n"
"<p>Please enter your <span style=\"font-style: italic\">username</span> and  <span style=\"font-style: italic\">password</span> to log in.</p>\n"
"<p>Once logged in, enter the <span style=\"font-style: italic\">Album</span> name where files will be uploaded. If this field is left empty, it will default to <span style=\"font-style: italic\">Postman</span>.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.loginContainer.setTitle(QtGui.QApplication.translate("PicasaConfigWidget", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PicasaConfigWidget", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("PicasaConfigWidget", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.loginButton.setText(QtGui.QApplication.translate("PicasaConfigWidget", "Login...", None, QtGui.QApplication.UnicodeUTF8))
        self.messageLabel.setText(QtGui.QApplication.translate("PicasaConfigWidget", "Message here", None, QtGui.QApplication.UnicodeUTF8))
        self.successLabel.setText(QtGui.QApplication.translate("PicasaConfigWidget", "Picasa authorized Postman successfully.", None, QtGui.QApplication.UnicodeUTF8))
        self.albumSettings.setTitle(QtGui.QApplication.translate("PicasaConfigWidget", "Configure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PicasaConfigWidget", "Album", None, QtGui.QApplication.UnicodeUTF8))
        self.albumEdit.setPlaceholderText(QtGui.QApplication.translate("PicasaConfigWidget", "Postman", None, QtGui.QApplication.UnicodeUTF8))

