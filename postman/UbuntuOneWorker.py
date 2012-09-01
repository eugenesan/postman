import os

from PySide import QtCore

from BaseWorker import *

class UbuntuOneWorker(BaseWorker):
 
    def __init__(self, parent=None):
        super(UbuntuOneWorker, self).__init__(parent)
        
    def run(self):

        self.progressSignal.emit(self.stampConfig)

        if self.filesModel.count() == 0:
            return
        
        progressStep = 1.0 / self.filesModel.count()

        volume = ''
        if 'ubuntuOneVolume' in self.stampConfig:
            volume = self.stampConfig['ubuntuOneVolume'].rstrip().encode('UTF-8','ignore')
        if len(volume) == 0:
            volume = 'Postman'

        volume = volume.replace('\\', '/')
        if volume.startswith('/'):
            volume = volume[1:]
        if volume.endswith('/'):
            volume = volume[:-1]
        if len(volume) == 0:
            volume = 'Postman'
        
        # start by creating a volume
        for r in range(self.retry):
            success = self.createVolume(volume)
            if success:
                break
            elif r == self.retry - 1:
                self.status = 'Failed, could not create Ubuntu One volume.'
                self.statusSignal.emit(self.stampConfig)
                self.doneSignal.emit(self.stampConfig)
                return
        
        # now upload the files
        for i in range(self.filesModel.count()):
            
            self.status = 'Uploading: ' + self.filesModel.filesList[i].filePath
            self.statusSignal.emit(self.stampConfig)
            
            imageFilename = self.filesModel.filesList[i].filePath
            
            for r in range(self.retry):
                try:
                    local = imageFilename
                    
                    if len(volume) > 0:
                        remote = volume + '/' + os.path.basename(imageFilename)
                    else:
                        remote = os.path.basename(imageFilename)

                    self.uploadFile(local, remote)
                    break
                except:
                    if r == self.retry - 1:
                        self.status = 'Failed'
                        self.statusSignal.emit(self.stampConfig)
                        self.doneSignal.emit(self.stampConfig)
                        return

            self.progress += progressStep
            self.progressSignal.emit(self.stampConfig)
        
        self.status = 'Done'
        self.result = True
        self.statusSignal.emit(self.stampConfig)
        self.doneSignal.emit(self.stampConfig)
        
    def createVolume(self, name):
        import ubuntuone.couch.auth as auth
        import urllib

        try:
            base = "https://one.ubuntu.com/api/file_storage/v1/volumes/~/"
            auth.request(base + urllib.quote(name), http_method="PUT")
            return True
        except:
            return False

    def uploadFile(self, local, remote):
        import json
        import ubuntuone.couch.auth as auth
        import mimetypes
        import urllib
        
        # Create remote path (which contains volume path)
        base = "https://one.ubuntu.com/api/file_storage/v1/~/"
        answer = auth.request(base + urllib.quote(remote.encode('utf-8')),
                              http_method="PUT",
                              request_body='{"kind":"file"}')
        
        node = json.loads(answer[1])
        
        # Read info about local file
        data = bytearray(open(local, 'rb').read())
        size = len(data)
        content_type = mimetypes.guess_type(local)[0]
        content_type = content_type or 'application/octet-stream'
        headers = {"Content-Length": str(size),
                   "Content-Type": content_type}
        
        # Upload content of local file to content_path from original response
        base = "https://files.one.ubuntu.com"
        url = base + urllib.quote(node.get('content_path').encode('utf-8'), safe="/~")
        auth.request(url, http_method="PUT",
                     headers=headers, request_body=data)
