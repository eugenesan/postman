// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

ListView {
    orientation: ListView.Horizontal
    width: 400
    smooth: true
    interactive: false
    anchors.bottomMargin: 0
    anchors.topMargin: 20
    clip: false
    delegate: Item {
        x: 5
        height: 100
        width: 110

        StampPaletteItem {
            serviceName: name
            serviceIcon: iconSource
        }
    }
    model: stampSheetModel
}
