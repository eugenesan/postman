// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

Rectangle {
    id: deliveryScreen
    anchors.fill: parent
    color: "#df000000"

    Connections {
        target: servicesModel
        onUploadFinishedSignal: deliveryControl.state = "deliveryStopped"
    }

    Behavior on opacity {
        NumberAnimation { duration: 400 }
    }

    ListView {
        id: serviceListView
        anchors.top: parent.top
        anchors.topMargin: 110
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.margins: 20

        model: servicesModel
        delegate: DeliveryDelegate { }
    }

    Rectangle {
        id: topFader
        anchors {
            top: deliveryScreen.top
            left: deliveryScreen.left
            right: deliveryScreen.right
        }

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
    }

    Text {
        color: "#ffffff"
        text: "Delivery"
        anchors.topMargin: -55
        anchors.fill: topFader
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        smooth: true
        font.pointSize: 22
        font.bold: true
    }

    Rectangle {
        id: bottomFader
        anchors {
            bottom: deliveryScreen.bottom
            left: deliveryScreen.left
            right: deliveryScreen.right
        }

        height: 150
        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#00000000"
            }
            GradientStop {
                position: 0.8
                color: "#000000"
            }
        }
    }

    Button {
        id: deliveryControl
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: parent.bottom
        anchors.margins: 15
        foregroundColor: "#c0ffffff"
        state: "deliveryOngoing"

        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#20ffffff"
            }

            GradientStop {
                position: 1
                color: "#00ffffff"
            }
        }

        states: [
            State {
                name: "deliveryOngoing"
                PropertyChanges { target: deliveryControl; label: "Stop" }
                PropertyChanges { target: deliveryControl; visible: false }
            },
            State {
                name: "deliveryStopped"
                PropertyChanges { target: deliveryControl; label: "Close" }
                PropertyChanges { target: deliveryControl; visible: true }
            }
        ]

        onClicked: {
            if (deliveryControl.state == "deliveryOngoing") {
                servicesModel.stopUploads()
                state = "deliveryStopped"
            }
            else {
                deliveryControl.state = "deliveryOngoing"
                parent.visible = false

                if (!envelope.flipped)
                    screenState = 'stampView'
                else
                    screenState = 'stackView'
            }
        }
    }
}
