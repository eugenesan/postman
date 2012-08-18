import QtQuick 1.1

import "js/StampSpawning.js" as StampCode

Image {
    id: tableTop

    source: "images/tableTop.png"
    width: 770
    height: 360
    fillMode: Image.PreserveAspectCrop

    property string screenState
    onScreenStateChanged: mainInterface.screenStateChanged(screenState)

    Component.onCompleted: screenState = 'stampView'

    Connections {
        target: mainInterface
        onForceScreenChangeSignal: {
            if (screenState == 'stampView') {
                envelope.flipped = true
                photoViewer.state = 'stackView'
            }
        }
        onForceCreateStampSignal: {
            var name = mainInterface.getPendingStampName()
            var icon = mainInterface.getPendingStampIcon()

            StampCode.createStamp(name, icon)
        }
    }

    Button {
        id: deliveryButton
        width: 160
        height: 40
        foregroundColor: "#ffbea7"
        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#00ffffff"
            }

            GradientStop {
                position: 1
                color: "#a0000000"
            }
        }
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 30
        anchors.horizontalCenter: parent.horizontalCenter
        label: "Deliver"
        onClicked: {
            deliveryView.visible = true
            screenState = 'deliveryView'
            servicesModel.deliver()
        }

        Connections {
            target: imageListModel
            onDataChanged: deliveryButton.updateState()
        }

        Connections {
            target: servicesModel
            onAuthChanged: deliveryButton.updateState()
        }

        function updateState() {
            state = (imageListModel.count() > 0) && (servicesModel.allAuth()) ? "shown" : "hidden"
            //state = servicesModel.count() > 0 ? "shown" : "hidden"
        }

        state: "hidden"

        states: [
            State {
                name: "shown"
                PropertyChanges { target: deliveryButton; anchors.bottomMargin: 30 }
            },
            State {
                name: "hidden"
                PropertyChanges { target: deliveryButton; anchors.bottomMargin: -height * 1.25 }
            }
        ]

        transitions: [
            Transition {
                PropertyAnimation { property: "anchors.bottomMargin"; duration: 200; easing.type: Easing.OutQuad }
            }
        ]
    }

    StampSheet {
        id: stampSheet
        width: parent.width
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top

        states: State {
            name: "hidden"
            PropertyChanges { target: stampSheet; anchors.topMargin: -height }
            when: envelope.side == Flipable.Back
        }

        transitions: Transition {
            SequentialAnimation {
                NumberAnimation { duration: 200 }
                PropertyAnimation { property: "anchors.topMargin"; duration: 300; easing.type: Easing.InOutQuad }
            }
        }
    }

    Button {
        id: flipButton
        visible: false
        width: 132
        height: 30
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.margins: 15
        label: "Flip Envelope"
        foregroundColor: "#a0ffbea7"
        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#00ffffff"
            }

            GradientStop {
                position: 1
                color: "#a0000000"
            }
        }

        onClicked: {
            envelope.flipped = !envelope.flipped
        }
    }

    Envelope {
        id: envelope
        width: parent.width * 0.6
        anchors.verticalCenter: parent.verticalCenter
        anchors.verticalCenterOffset: stampSheet.height / 6
        anchors.horizontalCenter: parent.horizontalCenter

        onFlippedChanged: {
            if (envelope.flipped)
                tableTop.screenState = photoViewer.state
            else
                tableTop.screenState = 'stampView'
        }
    }

    PhotoViewer {
        id: photoViewer
        anchors.fill: parent

        onStateChanged: {
            if (envelope.flipped)
                tableTop.screenState = state
        }
    }


    DeliveryViewer {
        id: deliveryView
        visible: false
        opacity: visible ? 1.0 : 0.0
    }


}
