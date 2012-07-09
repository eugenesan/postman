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
        id: flipButton
        x: 628
        y: 10
        width: 132
        height: 30
        anchors.right: parent.right
        anchors.top: parent.top
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
        y: 116
        anchors.left: parent.left
        anchors.leftMargin: 0
        anchors.verticalCenter: parent.verticalCenter

        states: State {
            name: "hidden"
            PropertyChanges { target: stampSheet; anchors.leftMargin: -width }
            when: envelope.side == Flipable.Back
        }

        transitions: Transition {
            SequentialAnimation {
                NumberAnimation { duration: 200 }
                PropertyAnimation { property: "anchors.leftMargin"; duration: 300; easing.type: Easing.InOutQuad }
            }
        }
    }

    Envelope {
        id: envelope
        width: 450
        anchors.verticalCenter: parent.verticalCenter
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
