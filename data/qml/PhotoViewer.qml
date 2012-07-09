// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

Rectangle {

    id: postcardViewer
    color: "#00000000"

    state: 'stackView'

    VisualDataModel
    {
        id: visualDataModel
        model: imageListModel
        delegate: PhotoDelegate { }
    }

    Rectangle {
        id: darkOverlay
        anchors.fill: parent
        color: "#df000000"

        Behavior on opacity {
            NumberAnimation { duration: 400 }
        }
    }

    GridView {
        id: gridPhotoView
        maximumFlickVelocity: 1750
        anchors.fill: parent
        anchors.topMargin: 90
        anchors.leftMargin: 20
        anchors.rightMargin: 20
        cellHeight: 240
        cellWidth: 240
        model: visualDataModel.parts.gridPart
        focus: true
        highlightFollowsCurrentItem: false

        highlight: Rectangle {
            id: highlightRectangle
            x: gridPhotoView.currentItem ? gridPhotoView.currentItem.x : 0
            y: gridPhotoView.currentItem ? gridPhotoView.currentItem.y : 0
            smooth: true
            width: 238
            height: 238
            color: "#56ffffff"
            border.width: 2
            border.color: "white"
            radius: 5
            opacity: visible ? 1.0 : 0.0

            Behavior on x { NumberAnimation { duration: 200; easing.type: Easing.InOutBounce } }
            Behavior on y { NumberAnimation { duration: 200; easing.type: Easing.InOutBounce } }

            Behavior on opacity { NumberAnimation { duration: 400; easing.type: Easing.InQuad } }
        }

        onCurrentItemChanged: mainInterface.highlightedPostcardIndexChanged(currentIndex)
    }

    Rectangle {
        id: gridHeader
        anchors {
            top: darkOverlay.top
            left: darkOverlay.left
            right: darkOverlay.right
        }

        opacity: darkOverlay.opacity
        height: 110
        gradient: Gradient {
            GradientStop {
                position: 0.390
                color: "#000000"
            }

            GradientStop {
                position: 1
                color: "#00000000"
            }
        }

        Text {
            anchors.fill: parent
            text: "Click to go back"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            color: "white"
            opacity: 0.6
        }

        Text {
            color: "#ffffff"
            text: "Postcards"
            anchors.topMargin: -55
            anchors.fill: parent
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            smooth: true
            font.pointSize: 22
            font.bold: true

            MouseArea {
                anchors.fill: parent
                anchors.bottomMargin: 50
                onClicked: postcardViewer.state = "stackView"
            }
        }
    }

    ScrollBar {
        width: 10
        height: gridPhotoView.height - 4
        anchors.left: gridPhotoView.right
        anchors.top: gridPhotoView.top
        flickable: gridPhotoView
        opacity: darkOverlay.opacity
    }

    PathView {
        id: stackPhotoView
        width: 0
        height: 0
        visible: false
        x: envelope.x + envelope.width / 2
        y: envelope.y + envelope.height / 2
        interactive: false
        pathItemCount: -1

        path: Path {
            PathLine { x: 1; y: 1 }
        }

        model: visualDataModel.parts.stackPart

        state: "stackInvisible"

        Timer {
            id: visibilityTimer
            running: true
            repeat: false;
            onTriggered: {
                stackPhotoView.visible = envelope.flipped
                visibilityTimer.running = false
            }
        }

        states: [
            State {
                name: "stackVisible"
                PropertyChanges { target: visibilityTimer; interval: 1; running: true }
                when: !envelope.flipped
            },
            State {
                name: "stackInvisible"
                PropertyChanges { target: visibilityTimer; interval: 600; running: true }
                when: envelope.flipped
            }
        ]
    }

    states: [
        State {
            name: "stackView"

            PropertyChanges { target: darkOverlay; opacity: 0.0 }
            PropertyChanges { target: gridPhotoView; visible: false }
        },
        State {
            name: "gridView"
            PropertyChanges { target: stackPhotoView; visible: false }

            PropertyChanges { target: darkOverlay; opacity: 1.0 }
            PropertyChanges { target: gridPhotoView; visible: true }
        }
    ]
}
