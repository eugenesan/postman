# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowdownWidget.ui'
#
# Created: Mon Aug 27 21:36:55 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ShowdownWidget(object):
    def setupUi(self, ShowdownWidget):
        ShowdownWidget.setObjectName("ShowdownWidget")
        ShowdownWidget.resize(269, 350)
        ShowdownWidget.setMaximumSize(QtCore.QSize(16777215, 350))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ShowdownWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.messageContainer = QtGui.QFrame(ShowdownWidget)
        self.messageContainer.setStyleSheet("QWidget {\n"
"    background-color: rgb(255, 85, 0);\n"
"}")
        self.messageContainer.setObjectName("messageContainer")
        self.verticalLayout = QtGui.QVBoxLayout(self.messageContainer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.messageContainer)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.messageContainer)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtGui.QLabel(self.messageContainer)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_4 = QtGui.QLabel(self.messageContainer)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.verticalLayout_2.addWidget(self.messageContainer)

        self.retranslateUi(ShowdownWidget)
        QtCore.QMetaObject.connectSlotsByName(ShowdownWidget)

    def retranslateUi(self, ShowdownWidget):
        ShowdownWidget.setWindowTitle(QtGui.QApplication.translate("ShowdownWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ShowdownWidget", "Ubuntu App Showdown", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ShowdownWidget", "<p>This application was created as part of the Ubuntu App Showdown competition. If you like this application and would like to see further development, please support <span style=\'font: bold\'>Postman</span> by voting.</p>\n"
"<p>To vote, click the link below and scroll down to the <span style=\'font: bold\'>Postman</span> entry. Give a rating (the higher, the better!), and click <span style=\'font: italic\'>Done</span> at the bottom of the page.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ShowdownWidget", "<style>a { color: white; }</style>\n"
"<a href=\"http://www.surveymonkey.com/s/P56YNQ9\">Vote now!</a>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ShowdownWidget", "Voting ends on the 29 August 2012. This message will not appear after that date.", None, QtGui.QApplication.UnicodeUTF8))

