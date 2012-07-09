// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

Rectangle {
    property string label: "Push Button"
    property string foregroundColor: "white"

    id: button
    width: 120
    height: 30
    radius: height / 2
    smooth: true
    border.color: foregroundColor
    border.width: 1

    signal clicked

    Text {
        id: buttonLabel
        text: label
        font.bold: true
        font.pointSize: 9
        color: foregroundColor
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        anchors.fill: parent

        states: State {
            PropertyChanges { target: buttonLabel; anchors.topMargin: 3 }
            when: mouseArea.pressed
        }
    }

    MouseArea {
        id: mouseArea
        anchors.fill: parent
        onClicked: button.clicked()
    }
}
