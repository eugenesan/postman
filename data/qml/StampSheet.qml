// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

Image {
    width: 130
    height: 400
    source: "images/stampSheet.png"
    smooth: true

    ListView {
        smooth: true
        interactive: false
        anchors.bottomMargin: 20
        anchors.topMargin: 25
        clip: true
        anchors.fill: parent
        delegate: Item {
            x: 5
            height: 110

            StampPaletteItem {
                serviceName: name
                serviceIcon: iconSource
            }
        }
        model: stampSheetModel
    }
}
