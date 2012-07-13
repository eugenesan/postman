# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2012 Edward Apap schumifer@hotmail.com
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
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
