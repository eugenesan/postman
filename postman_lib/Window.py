# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from PySide.QtDeclarative import *

import logging
logger = logging.getLogger('postman_lib')

from . postmanconfig import *

class Window(object):
    def setupUi(self, MainWindow):
        loader = QUiLoader()
        uidir = QDir(get_data_path()+"/ui")
        loader.setWorkingDirectory(uidir)
        file = QFile(uidir.path() + "/PostmanWindow.ui")
        file.open(QFile.ReadOnly)
        widget = loader.load(file, self)
        widget.setWindowFlags(Qt.Widget)
        self.setCentralWidget(widget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(self)
        
        try:
            from postman import indicator
            # self is passed so methods of this class can be called from indicator.py
            # Comment this next line out to disable appindicator
            self.indicator = indicator.new_application_indicator(self)
        except ImportError:
            pass

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QApplication.translate("MainWindow", "MainWindow", None, QApplication.UnicodeUTF8))
