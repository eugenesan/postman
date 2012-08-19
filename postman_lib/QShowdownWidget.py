from PySide import QtGui
from PySide import QtCore

import Ui_ShowdownWidget


class QShowdownWidget(QtGui.QWidget):

    def __init__(self, parent = None):
        super(QShowdownWidget, self).__init__(parent)

        self.ui = Ui_ShowdownWidget.Ui_ShowdownWidget()
        self.ui.setupUi(self)

        # only display message if <= 29th August 2012
        latestDateTime = QtCore.QDateTime(QtCore.QDate(2012, 8, 29), QtCore.QTime(23, 59, 59))
        showMessage = QtCore.QDateTime.currentDateTime() < latestDateTime

        self.ui.messageContainer.setVisible(showMessage)
