from PySide import QtGui

class QTextEditDefaultText(QtGui.QTextEdit):

    def __init__(self, parent = None):
        super(QTextEditDefaultText, self).__init__(parent)

        self._defaultText = ''
        self._emptyState = True
        self._ignoreFlag = False
        
        # create stylesheet color
        textColor = self.palette().text().color()
        textColor.setAlpha(128)
        strColor = 'rgba(' + str(textColor.red()) + ',' + str(textColor.green()) + ',' + str(textColor.blue()) + ',' + str(textColor.alpha()) + ')'
        self._styleSheet = 'QTextEdit { color: ' + strColor + ' }'

    def setDefaultText(self, text):
        self._defaultText = text

        if self._emptyState:
            self.setStyleSheet(self._styleSheet)
            self._ignoreFlag = True
            self.blockSignals(True)
            self.setText(self._defaultText)
            self.blockSignals(False)
            self._ignoreFlag = False

    def defaultText(self):
        return self._defaultText

    def focusInEvent(self, event):
        if self._emptyState:
            self.blockSignals(True)
            self.clear()
            self.blockSignals(False)
            self.setStyleSheet('')

        super(QTextEditDefaultText, self).focusInEvent(event)

    def focusOutEvent(self, event):
        if self._emptyState:
            self.setDefaultText(self._defaultText)

        super(QTextEditDefaultText, self).focusOutEvent(event)

    def keyPressEvent(self, event):
        super(QTextEditDefaultText, self).keyPressEvent(event)

        self.setStyleSheet('')
        self._emptyState = len(self.toPlainText()) == 0

    def setText(self, text):
        prevEmptyState = self._emptyState
        prevText = ''
        if not self._emptyState:
            prevText = self.toPlainText()

        if not self._ignoreFlag:          
            self._emptyState = (len(text) == 0)
            if self._emptyState:
                self.setStyleSheet(self._styleSheet)
            else:
                self.setStyleSheet('')
        
        if self._emptyState:
            # this will trigger a signal
            if (not self._ignoreFlag) and (text != prevText):
                super(QTextEditDefaultText, self).setText('')

            self.blockSignals(True)
            super(QTextEditDefaultText, self).setText(self._defaultText)
            self.blockSignals(False)
        else:
            super(QTextEditDefaultText, self).setText(text)
  
        #if (not self._ignoreFlag) and (prevEmptyState) and (prevEmptyState != self._emptyState) and (text == self._defaultText):
        #    self.textChanged.emit()
