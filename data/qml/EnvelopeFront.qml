// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

Image {
    id: image1
    smooth: true
    anchors.fill: parent
    source: "images/envelopeFront.png"

    Image {
        id: stamp
        y: 257
        width: parent.width * 0.35
        fillMode: Image.PreserveAspectFit
        anchors.left: parent.left
        anchors.leftMargin: parent.width * 0.1
        anchors.bottom: parent.bottom
        anchors.bottomMargin: parent.width * 0.1
        opacity: 0.400
        smooth: true
        source: "images/postmanStamp.png"
        rotation: 3
    }

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
