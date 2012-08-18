from BaseWorker import *

class GooglePlusWorker(BaseWorker):

    def __init__(self, parent = None):
        super(GooglePlusWorker, self).__init__(parent)

    def run(self):

        self.progressSignal.emit(self.stampConfig)

        if self.filesModel.count() == 0:
            return

        client = self.stampConfig['googlePlusInst']

        # create album name
        albumName = ''
        if 'googlePlusAlbum' in self.stampConfig:
            albumName = self.stampConfig['googlePlusAlbum'].rstrip()
        if len(albumName) == 0:
            albumName = 'Postman'


        # get/create an album
        try:
            album = None

            # get the list of available albums
            availableAlbums = client.GetFeed('http://picasaweb.google.com/data/feed/api/user/' + self.stampConfig['googlePlusUsername'] + '?kind=album&access=all')

            for entry in availableAlbums.entry:
                if entry.title.text == albumName:
                    if not album:
                        album = entry
                    elif int(entry.numphotos.text) > int(album.numphotos.text):
                        album = entry

            if not album:
                album = client.InsertAlbum(albumName, '')
        except:
            self.status = 'Failed, could not create album.'
            self.statusSignal.emit(self.stampConfig)
            self.doneSignal.emit(self.stampConfig)
            return

        progressStep = 1.0 / self.filesModel.count()

        for i in range(self.filesModel.count()):

            self.status = 'Uploading: ' + self.filesModel.filesList[i].filePath
            self.statusSignal.emit(self.stampConfig)

            imageFilename = self.filesModel.filesList[i].filePath.encode('UTF-8','ignore')
            imageTitle = self.filesModel.filesList[i].title.encode('UTF-8','ignore')
            imageDescription = self.filesModel.filesList[i].description.encode('UTF-8','ignore')

            if len(imageTitle) == 0:
                # title is required, use filename
                fileInfo = QtCore.QFileInfo(imageFilename)
                imageTitle = fileInfo.baseName()

            for r in range(self.retry):
                try:
                    client.InsertPhotoSimple(album, imageTitle, imageDescription, imageFilename)
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
