# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ServiceInstructionsWidget.ui'
#
# Created: Sat Aug 18 17:50:23 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ServiceInstructionsWidget(object):
    def setupUi(self, ServiceInstructionsWidget):
        ServiceInstructionsWidget.setObjectName("ServiceInstructionsWidget")
        ServiceInstructionsWidget.resize(320, 300)
        ServiceInstructionsWidget.setMinimumSize(QtCore.QSize(320, 0))
        self.verticalLayout = QtGui.QVBoxLayout(ServiceInstructionsWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(ServiceInstructionsWidget)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(ServiceInstructionsWidget)
        QtCore.QMetaObject.connectSlotsByName(ServiceInstructionsWidget)

    def retranslateUi(self, ServiceInstructionsWidget):
        ServiceInstructionsWidget.setWindowTitle(QtGui.QApplication.translate("ServiceInstructionsWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ServiceInstructionsWidget", "<p>To add services, drag the stamps from the top onto the envelope. To remove any of the added services, simply drag the stamps off the envelope.</p>\n"
"<p><span style=\"font-weight:bold\">Note: </span>You may flip the envelope at any time by double-clicking it.</p>", None, QtGui.QApplication.UnicodeUTF8))

