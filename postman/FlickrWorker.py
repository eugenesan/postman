from PySide import QtCore

import flickrapi

from BaseWorker import *

class FlickrWorker(BaseWorker):
    
    key = '391fb6763fe0b5011cf52638067e0fed'
    secret = '369f46a112452186'
    
    def __init__(self, parent = None):
        super(FlickrWorker, self).__init__(parent)
    
    def run(self):

        self.progressSignal.emit(self.stampConfig)
        
        if self.filesModel.count() == 0:
            return
        
        progressStep = 1.0 / self.filesModel.count()
        
        flickrInstance = self.stampConfig['flickrInst']
        
        for i in range(self.filesModel.count()):
            
            self.status = 'Uploading: ' + self.filesModel.filesList[i].filePath
            self.statusSignal.emit(self.stampConfig)
            
            imageFilename = self.filesModel.filesList[i].filePath.encode('UTF-8','ignore')
            imageTitle = self.filesModel.filesList[i].title.encode('UTF-8','ignore')
            imageDescription = self.filesModel.filesList[i].description.encode('UTF-8','ignore')
            
            for r in range(self.retry):
                try:
                    flickrInstance.upload(filename=imageFilename, title=imageTitle, description=imageDescription)
                    break
                except:
                    if r == self.retry - 1:
                        self.status = 'Failed'
                        self.statusSignal.emit(self.stampConfig)
                        self.doneSignal.emit(self.stampConfig)
                        return

            self.progress = self.progress + progressStep
            self.progressSignal.emit(self.stampConfig)
        
        self.status = 'Done'
        self.result = True
        self.statusSignal.emit(self.stampConfig)
        self.doneSignal.emit(self.stampConfig)
        