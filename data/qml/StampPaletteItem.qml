// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

import "js/StampSpawning.js" as StampCode

Rectangle {

    property string serviceName: "Undefined"
    property string serviceIcon

    id: stampPaletteItem
    width: 100
    height: 100
    color: "#00000000"

    MouseArea {
        id: mouseArea
        anchors.fill: parent

        Column {
            spacing: 5
            anchors.fill: parent

            Rectangle {
                width: 100
                height: 80
                color: "#00000000"

                Image {
                    width: 65
                    height: 80
                    anchors.centerIn: parent
                    fillMode: Image.PreserveAspectFit
                    source: 'images/stampBackground.png'

                    Image {
                        id: icon
                        fillMode: Image.PreserveAspectFit
                        anchors.fill: parent
                        anchors.margins: 8
                        smooth: true
                        anchors.horizontalCenter: parent.horizontalCenter
                        source: serviceIcon
                    }
                }
            }
            Text {
                id: label
                color: "#3c3c3c"
                text: serviceName
                font.bold: true
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }

        states: State {
            name: "active"
            PropertyChanges { target: icon; opacity: 0.5 }
            PropertyChanges { target: label; opacity: 0.5 }
            when: mouseArea.pressed
        }

        transitions: Transition {
            PropertyAnimation { target: icon; property: "opacity"; duration: 200 }
            PropertyAnimation { target: label; property: "opacity"; duration: 200 }
        }

        onPressed: StampCode.createDraggable(mouse, stampPaletteItem)
        onPositionChanged: StampCode.moveSpawn(mouse)
        onReleased: StampCode.releaseSpawn()
    }


}
