// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

Component {

    Item {
        height: 125
        width: serviceListView.width

        Rectangle {
            anchors.fill: parent
            anchors.margins: 8
            color: "#50000000"
            radius: 20
            smooth: true
            border.color: "#32ffffff"

            Image {
                id: icon
                source: 'images/stampBackground.png'
                width: 65
                height: 80
                anchors.left: parent.left
                anchors.leftMargin: 15
                anchors.verticalCenter: parent.verticalCenter
                smooth: true
                fillMode: Image.PreserveAspectFit

                Image {
                    source: serviceIcon
                    anchors.fill: parent
                    smooth: true
                    anchors.margins: 8
                    fillMode: Image.PreserveAspectFit
                }
            }

            Text {
                id: name
                anchors.left: icon.right
                anchors.leftMargin: 20
                anchors.top: parent.top
                anchors.topMargin: 15
                text: serviceName
                font.pointSize: 15
                font.bold: true
                color: "white"
            }

            ProgressBar {
                id: progressbar
                height: 25
                progress: serviceProgress
                anchors.left: name.right
                anchors.leftMargin: 20
                anchors.top: parent.top
                anchors.topMargin: 15
                anchors.right: parent.right
                anchors.rightMargin: 20
            }

            Text {
                id: status
                color: "#b4ffffff"
                text: serviceStatus
                clip: true
                font.pointSize: 9
                anchors.left: icon.right
                anchors.leftMargin: 20
                anchors.bottom: icon.bottom
                anchors.topMargin: 15
                anchors.right: parent.right
                anchors.rightMargin: 20
            }
        }
    }
}
