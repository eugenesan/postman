# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageDetailsWidget.ui'
#
# Created: Tue Oct  9 22:34:29 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ImageDetailsWidget(object):
    def setupUi(self, ImageDetailsWidget):
        ImageDetailsWidget.setObjectName("ImageDetailsWidget")
        ImageDetailsWidget.resize(320, 248)
        ImageDetailsWidget.setMinimumSize(QtCore.QSize(320, 0))
        self.verticalLayout = QtGui.QVBoxLayout(ImageDetailsWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.titleLabel = QtGui.QLabel(ImageDetailsWidget)
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.titleLabel)
        self.titleLineEdit = QtGui.QLineEdit(ImageDetailsWidget)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.titleLineEdit)
        self.descriptionLabel = QtGui.QLabel(ImageDetailsWidget)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.descriptionLabel)
        self.descriptionTextEdit = QTextEditDefaultText(ImageDetailsWidget)
        self.descriptionTextEdit.setObjectName("descriptionTextEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.descriptionTextEdit)
        self.tagsLineEdit = QtGui.QLineEdit(ImageDetailsWidget)
        self.tagsLineEdit.setObjectName("tagsLineEdit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.tagsLineEdit)
        self.tagsLabel = QtGui.QLabel(ImageDetailsWidget)
        self.tagsLabel.setObjectName("tagsLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.tagsLabel)
        self.tagsExampleLabel = QtGui.QLabel(ImageDetailsWidget)
        self.tagsExampleLabel.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tagsExampleLabel.setFont(font)
        self.tagsExampleLabel.setObjectName("tagsExampleLabel")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.tagsExampleLabel)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(ImageDetailsWidget)
        QtCore.QMetaObject.connectSlotsByName(ImageDetailsWidget)

    def retranslateUi(self, ImageDetailsWidget):
        ImageDetailsWidget.setWindowTitle(QtGui.QApplication.translate("ImageDetailsWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("ImageDetailsWidget", "Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionLabel.setText(QtGui.QApplication.translate("ImageDetailsWidget", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.tagsLabel.setText(QtGui.QApplication.translate("ImageDetailsWidget", "Tags:", None, QtGui.QApplication.UnicodeUTF8))
        self.tagsExampleLabel.setText(QtGui.QApplication.translate("ImageDetailsWidget", "ex. Postman, image uploader, flickr", None, QtGui.QApplication.UnicodeUTF8))

from QTextEditDefaultText import QTextEditDefaultText
