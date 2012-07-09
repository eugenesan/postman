# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

from . postmanconfig import *

class AboutDialog(object):
    def setupUi(self, Dialog):
        loader = QUiLoader()
        uidir = QDir(get_data_path() + "/ui")
        loader.setWorkingDirectory(uidir)
        file = QFile(uidir.path() + "/AboutPostmanDialog.ui")
        file.open(QFile.ReadOnly)
        lwidget = loader.load(file, self)
        lwidget.setWindowFlags(Qt.Widget)
        layout = QVBoxLayout()
        layout.addWidget(lwidget)
        self.setLayout(layout)
        
        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QApplication.translate("About", "About", None, QApplication.UnicodeUTF8))

