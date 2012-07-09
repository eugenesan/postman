// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

Image {
    smooth: true
    anchors.fill: parent
    source: "images/envelopeFront.png"

    MouseArea {
        id: mouseArea
        anchors.fill: parent
        onDoubleClicked: {
            envelope.flipped = !envelope.flipped
        }

        onClicked: {
            servicesModel.deselectAllStamps()
        }
    }
}
