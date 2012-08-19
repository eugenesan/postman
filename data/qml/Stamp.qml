// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

import "js/StampDraggable.js" as StampCode

Image {
    property string serviceName: "Undefined"
    property string serviceIcon
    property int serviceUid: -1

    id: stamp
    source: 'images/stampBackground.png'
    width: 65
    height: 80
    scale: 0
    focus: selectionBox.visible

    Component.onCompleted: state = "grabbed"

    Connections {
        target: servicesModel
        onSelectionChangedSignal: {
            selectionBox.visible = servicesModel.selectedStamp() === stamp.serviceUid
        }
    }

    function checkStatus() {
        StampCode.checkStatus()
    }

    Rectangle {
        id: selectionBox
        color: "#00000000"
        radius: 4
        anchors.rightMargin: -3
        anchors.leftMargin: -3
        anchors.bottomMargin: -3
        anchors.topMargin: -3
        smooth: true
        border.width: 2
        border.color: "#8000b7ff"
        anchors.fill: parent
    }

    Image {
        fillMode: Image.PreserveAspectFit
        anchors.fill: parent
        anchors.margins: 8
        source: serviceIcon
        smooth: true
    }

    MouseArea {
        anchors.fill: parent
        drag.target: stamp

        onPressed: {
            stamp.state = "grabbed"
            servicesModel.setSelectedStamp(stamp.serviceUid)
        }
        onReleased: checkStatus()
    }

    Keys.onDeletePressed: StampCode.destroyStamp()

    states: [
        State {
            name: "normal"
            PropertyChanges { target: stamp; scale: 1 }
        },
        State {
            name: "shrunk"
            PropertyChanges { target: stamp; scale: 0 }
        },
        State {
            name: "grabbed"
            PropertyChanges { target: stamp; scale: 1.2 }
        }
    ]

    transitions: [
        Transition {
            PropertyAnimation { property: "scale"; duration: 300; easing.type: Easing.OutBounce; easing.amplitude: 0.8 }
        },
        Transition {
            to: "shrunk"
            PropertyAnimation { property: "scale"; duration: 150; easing.type: Easing.InCubic; easing.amplitude: 0.8 }
        }
    ]
}
