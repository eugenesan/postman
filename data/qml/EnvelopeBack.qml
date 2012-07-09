// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

Image {
    smooth: true
    anchors.fill: parent
    source: "images/envelopeFront.png"

    Text {
        Connections {
            target: imageListModel
            onDataChanged: instructionText.visible = imageListModel.count() === 0
        }

        id: instructionText
        color: "#c2c2c2"
        anchors.fill: parent
        text: 'Drag-and-Drop image files here.'
        font.bold: true
        anchors.rightMargin: 40
        anchors.leftMargin: 40
        wrapMode: Text.WordWrap
        font.pointSize: (parent.height / 14 > 8) ? (parent.height / 14) : 8
        smooth: true
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
    }

    MouseArea {
        id: mouseArea
        anchors.fill: parent
        onDoubleClicked: {
            envelope.flipped = !envelope.flipped
        }
    }
}
