#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import MainWindow

from PySide import QtGui

def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Postman")
    
    mainWindow = MainWindow.MainWindow()
    mainWindow.show()
    
    # get arguments
    for a in sys.argv:
        index = a.find('-s')
        if index == 0:
            service = a[2:]
            mainWindow.addStamp(service)

    sys.exit(app.exec_())
