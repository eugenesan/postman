// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

Rectangle {
    id: progressBar
    property real progress : 0.0
    width: 300
    height: 35
    color: "#00000000"

    Rectangle {
        anchors.fill: parent
        radius: height / 2
        border.width: 1

        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#b4000000"
            }

            GradientStop {
                position: 1
                color: "#96000000"
            }
        }

        smooth: true
        border.color: "#ffffff"
    }

    Rectangle {
        radius: height / 2
        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#00c4ff"
            }

            GradientStop {
                position: 1
                color: "#23526f"
            }
        }
        anchors.verticalCenter: parent.verticalCenter
        smooth: true
        width: (progress > 0) ? (parent.height + (parent.width - parent.height) * progress) : 0
        height: parent.height

        Behavior on width {
            NumberAnimation { duration: 150; easing.type: Easing.InCubic }
        }
    }

    Rectangle {
        anchors.fill: parent
        radius: height / 2
        border.width: 2
        color: "#00000000"
        smooth: true
        border.color: "#7accff"
    }

    Text {
        id: progressText
        color: "#ffffff"
        text: (progress * 100).toFixed(0) + '%'
        font.bold: true
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        anchors.fill: parent
        font.pixelSize: 12
    }
}
